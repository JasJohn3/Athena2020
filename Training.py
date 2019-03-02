from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.optim as optim
import torch.utils.data
import torchvision.datasets as dset
import torchvision.transforms as transforms
import torchvision.utils as vutils
from torch.autograd import Variable
import os
import Generator
import Discriminator
import Dialogues

def Train():
    #Dialogues.td.train_Button.setEnabled(False)
    # Setting some hyperparameters
    batchSize = 64  # We set the size of the batch.
    imageSize = 64  # We set the size of the generated images (64x64).

    # Creating the transformations
    transform = transforms.Compose([transforms.Resize(imageSize), transforms.ToTensor(),
                                    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5,
                                                                           0.5)), ])  # We create a list of transformations (scaling, tensor conversion, normalization) to apply to the input images.

    dataset = dset.CIFAR10(root='./data', download=True,
                           transform=transform)  # We download the training set in the ./data folder and we apply the previous transformations on each image.
    dataloader = torch.utils.data.DataLoader(dataset, batch_size=batchSize, shuffle=True,
                                             num_workers=0)  # We use dataLoader to get the images of the training set batch by batch.

    # Defining the weights_init function that takes as input a neural network m and that will initialize all its weights.
    def weights_init(m):
        classname = m.__class__.__name__
        if classname.find('Conv') != -1:
            m.weight.data.normal_(0.0, 0.02)
        elif classname.find('BatchNorm') != -1:
            m.weight.data.normal_(1.0, 0.02)
            m.bias.data.fill_(0)
    # Creating the generator
    netG = Generator.G()
    netG.apply(weights_init)
    # Creating the discriminator
    netD = Discriminator.D()
    netD.apply(weights_init)

    # Training the DCGANs
    criterion = nn.BCELoss()
    optimizerD = optim.Adam(netD.parameters(), lr=0.0002, betas=(0.5, 0.999))
    optimizerG = optim.Adam(netG.parameters(), lr=0.0002, betas=(0.5, 0.999))
    Total_Training = 2
    file = open("Neural Network Loss.txt", "w")

    for epoch in range(Total_Training):

        for i, data in enumerate(dataloader, 0):

            # 1st Step: Updating the weights of the neural network of the discriminator

            netD.zero_grad()

            # Training the discriminator with a real image of the dataset
            real, _ = data
            input = Variable(real)
            target = Variable(torch.ones(input.size()[0]))
            output = netD(input)
            errD_real = criterion(output, target)

            # Training the discriminator with a fake image generated by the generator
            noise = Variable(torch.randn(input.size()[0], 100, 1, 1))
            fake = netG(noise)
            target = Variable(torch.zeros(input.size()[0]))
            output = netD(fake.detach())
            errD_fake = criterion(output, target)

            # Backpropagating the total error
            errD = errD_real + errD_fake
            errD.backward()
            optimizerD.step()

            # 2nd Step: Updating the weights of the neural network of the generator

            netG.zero_grad()
            target = Variable(torch.ones(input.size()[0]))
            output = netD(fake)
            errG = criterion(output, target)
            errG.backward()
            optimizerG.step()

            # 3rd Step: Printing the losses and saving the real images and the generated images of the minibatch every 100 steps
            file = open("Neural Network Loss.txt", "a+")
            file.write('[%d/%d][%d/%d] Loss_D: %.4f Loss_G: %.4f\n' % (epoch, Total_Training, i, len(dataloader), errD.item(), errG.item()))
            file.close()
            # =====Append Loss to Loss Dialogue Box=====
            logTemp = '[%d/%d][%d/%d] Loss_D: %.4f Loss_G: %.4f\n' % (epoch, Total_Training, i, len(dataloader), errD.item(), errG.item())
            Dialogues.TrainingDialogue.updateLog(Dialogues.td, logTemp)

            print('[%d/%d][%d/%d] Loss_D: %.4f Loss_G: %.4f' % (epoch, Total_Training, i, len(dataloader), errD.item(), errG.item()))
            if i % 100 == 0:

                if not os.path.exists('./results'):
                    os.makedirs('./results')
                vutils.save_image(real, '%s/real_samples.png' % "./results", normalize=True)
                fake = netG(noise)
                vutils.save_image(fake.data, '%s/fake_samples_epoch_%03d.png' % ("./results", epoch), normalize=True)
