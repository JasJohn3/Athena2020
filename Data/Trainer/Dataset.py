from torchvision.transforms import *
from torchvision.datasets import *
from torch.utils.data import DataLoader
import ctypes.wintypes
import os

def createDataloader():
    # Setting some hyperparameters
    batchSize = 64  # We set the size of the batch.
    imageSize = 64  # We set the size of the generated images (64x64).

    # We create a list of transformations (scaling, tensor conversion, normalization) to apply to the input images.
    transform = Compose([Resize(imageSize), ToTensor(), Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),])

    dataset = CIFAR10(root='./Data', download=True, transform=transform)  # We download the training set in the ./Data folder and we apply the previous transformations on each image.

    return DataLoader(dataset, batch_size=batchSize, shuffle=True, num_workers=0)  # We use dataLoader to get the images of the training set batch by batch.

def loadImage():
    # Setting some hyperparameters
    batchSize = 3  # We set the size of the batch.
    imageSize = 64  # We set the size of the generated images (64x64).

    #Get User Document Folder
    buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(None, 5, None, 0, buf)

    try:
        os.mkdir(buf.value + '\\Athena')
    except OSError:
        pass

    return DataLoader(ImageFolder(root=buf.value + '\\Athena',
                                  transform=Compose([Resize(imageSize),
                                                                      ToTensor(),
                                                                      Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])),
                      batch_size=batchSize,
                      shuffle=True,
                      num_workers=0)

def get_data(args, train_flag=True):
    transform = Compose([
        Scale(args.image_size),
        CenterCrop(args.image_size),
        ToTensor(),
        Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),])

    if args.dataset in ['imagenet', 'folder', 'lfw']:
        dataset = ImageFolder(root=args.dataroot,
                              transform=transform)

    elif args.dataset == 'lsun':
        dataset = LSUN(db_path=args.dataroot,
                       classes=['bedroom_train'],
                       transform=transform)

    elif args.dataset == 'cifar10':
        dataset = CIFAR10(root=args.dataroot,
                          download=True,
                          train=train_flag,
                          transform=transform)

    elif args.dataset == 'cifar100':
        dataset = CIFAR100(root=args.dataroot,
                           download=True,
                           train=train_flag,
                           transform=transform)

    elif args.dataset == 'mnist':
        dataset = MNIST(root=args.dataroot,
                        download=True,
                        train=train_flag,
                        transform=transform)

    else:
        raise ValueError("Unknown dataset %s" % (args.dataset))
    return DataLoader(dataset, batch_size=dataset.__sizeof__(), shuffle=True, num_workers=0)