import ctypes
import ctypes.wintypes
from os import path
from torch.nn import BCELoss
import torch.nn.parallel
from torch.optim import Adam
import torch.utils.data
from torchvision.utils import *
import os
from Data.NeuralNetwork import *
from .Dataset import createDataloader
import time
import datetime
from PyQt5.QtCore import pyqtSignal, QThread
from PIL import Image

class Trainer(QThread):
    # Signals linked to main thread
    maxstepsSignal = pyqtSignal(int)
    maxepochsSignal = pyqtSignal(int)
    logSignal = pyqtSignal(str)
    epochtimeSignal = pyqtSignal(str)
    totaltimeSignal = pyqtSignal(str)
    stepSignal = pyqtSignal(int)
    epochSignal = pyqtSignal(int)
    trainImageSignal = pyqtSignal(Image.Image)
    testImageSignal = pyqtSignal(Image.Image)
    completeSignal = pyqtSignal()
    LossSignal = pyqtSignal(float, float)
    #discriminatorLossSignal = pyqtSignal(float)
    totaltraining = pyqtSignal(int)

    def __init__(self, epochs, dataset, user_session):
        QThread.__init__(self)
        self.discriminator = Discriminator()
        self.generator = Generator()
        self.epochs = int(epochs)
        self.dataset = dataset
        self.user_session = user_session

    def run(self):
        buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, 5, None, 0, buf)
        root = buf.value + '\\Athena'

        dataloader = createDataloader(self.dataset)
        self.logSignal.emit("Starting...\n")

        self.maxstepsSignal.emit(len(dataloader))
        self.maxepochsSignal.emit((self.epochs * len(dataloader)))

        # Populate the GAN's weights
        self.generator.apply(self.weights_init)
        self.discriminator.apply(self.weights_init)

        # Trainer the DCGANs
        criterion = BCELoss()
        optimize_discriminate = Adam(self.discriminator.parameters(), lr=0.0002, betas=(0.5, 0.999))
        optimize_generate = Adam(self.generator.parameters(), lr=0.0002, betas=(0.5, 0.999))

        # Check for a saved GAN
        if path.exists(root + '/%s/Save/ATHENA_GAN.tar' % self.user_session):
            checkpoint = torch.load(root + '/%s/Save/ATHENA_GAN.tar' % self.user_session)
            self.generator.load_state_dict(checkpoint['Generator'])
            self.discriminator.load_state_dict(checkpoint['Discriminator'])
            optimize_generate.load_state_dict(checkpoint['optimizerG_state_dict'])
            optimize_discriminate.load_state_dict(checkpoint['optimizerD_state_dict'])
            self.generator.eval()
            self.discriminator.eval()
        #Creating Lists for Histogram data
        total_training = int((len(dataloader) * self.epochs))
        # ===Training Epochs===
        for epoch in range(self.epochs):
            for i, trainData in enumerate(dataloader, 0):
                # *Epoch start time*
                start = time.time()
                current_training = int((total_training - ((total_training/(epoch + 1)) -  i)))
                # Creation of train and test data .3 seconds
                trainData, _ = trainData
                noise = torch.randn(trainData.size()[0], 100, 1, 1)
                testData = self.generator(noise)
                ones = torch.ones(trainData.size()[0])
                # Train & Optimize Discriminator
                self.discriminator.zero_grad()

                # Criterion run at an average of .3 seconds
                error_train = criterion(self.discriminator(trainData), ones)
                error_test = criterion(self.discriminator(testData.detach()), torch.zeros(trainData.size()[0]))

                error_discriminate = error_train + error_test

                # Error & optimize 1 second
                error_discriminate.backward()
                optimize_discriminate.step()

                # Train & Optimize Generator 1.5 seconds
                self.generator.zero_grad()

                error_generate = criterion(self.discriminator(testData), ones)
                error_generate.backward()
                optimize_generate.step()

                # Save trainData and testData images every 100 steps .002 seconds
                # Get User Document Folder
                self.emit_image(trainData, self.trainImageSignal, normalize=True)
                self.emit_image(testData.data, self.testImageSignal, normalize=True)

                # *Epoch end time*
                end = time.time()

                # ===Log Update===
                # Calculating the training time
                epoch_time = datetime.timedelta(seconds=((len(dataloader) - i) * (end - start)))
                training_Time = epoch_time * (self.epochs - epoch)

                # Print the loss Data & time to completion
                self.logSignal.emit('[%d/%d][%d/%d] Discriminator Loss: %.4f Generator Loss: %.4f' % (epoch + 1, self.epochs, i + 1, len(dataloader), error_discriminate.item(), error_generate.item()))
                self.logSignal.emit("Estimated Time to Epoch Completion: {:0>8}".format(str(epoch_time)))
                self.logSignal.emit("Estimated Time to Trainer Completion: {:0>8}\n".format(str(training_Time)))
                self.epochtimeSignal.emit("{:0>8}".format(str(epoch_time)))
                self.totaltimeSignal.emit("{:0>8}".format(str(training_Time)))
                self.stepSignal.emit(i + 1)
                self.epochSignal.emit((epoch * len(dataloader)) + i + 1)
                self.totaltraining.emit(total_training)
                self.LossSignal.emit(error_generate.item(), error_discriminate.item())

            #Save an image file at the completion of each Epoch
            if not os.path.exists(root + '/%s/Results' % self.user_session):
                os.makedirs(root + '/%s/Results' % self.user_session)
            if not os.path.exists(root + './%s/Results/real' % self.user_session):
                os.makedirs(root + '/%s/Results/real' % self.user_session)
            if not os.path.exists(root + '/%s/Results/Fake' % self.user_session):
                os.makedirs(root + '/%s/Results/Fake' % self.user_session)
            save_image(trainData,
                       '%s/real_samples_epoch_%03d.bmp' % (root + "/%s/Results/Real" % self.user_session, epoch),
                       normalize=True)
            save_image(testData.data,
                       '%s/fake_samples_epoch_%03d.bmp' % (root + "/%s/Results/Fake" % self.user_session, epoch),
                       normalize=True)
            # Save the GAN state
            if not os.path.exists(root + '/%s/Save' % self.user_session):
                os.makedirs(root + '/%s/Save' % self.user_session)
            torch.save({
                'Generator': self.generator.state_dict(),
                'Discriminator': self.discriminator.state_dict(),
                'optimizerD_state_dict': optimize_discriminate.state_dict(),
                'optimizerG_state_dict': optimize_generate.state_dict()},root + '/%s/Save/ATHENA_GAN.tar' % self.user_session)

        self.completeSignal.emit()

    # Initialize all its weights in neural network
    def weights_init(self, m):
        classname = m.__class__.__name__
        if classname.find('Conv') != -1:
            m.weight.data.normal_(0.0, 0.02)
        elif classname.find('BatchNorm') != -1:
            m.weight.data.normal_(1.0, 0.02)
            m.bias.data.fill_(0)

    # Convert created image arrays to image
    def emit_image(self, tensor, signal, nrow=8, padding=2,
                   normalize=False, range=None, scale_each=False, pad_value=0):

        # Take tensor and create a image with the grid size and padding between each image
        grid = make_grid(tensor, nrow=nrow, padding=padding, pad_value=pad_value,
                         normalize=normalize, range=range, scale_each=scale_each)
        # Convert grid to a ndarray with image notations
        ndarr = grid.mul(255).clamp(0, 255).byte().permute(1, 2, 0).cpu().numpy()
        # Emit and convert ndarray to a Pillow Image
        signal.emit(Image.fromarray(ndarr))