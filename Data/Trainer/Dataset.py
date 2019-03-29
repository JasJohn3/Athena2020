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

    return DataLoader(get_dataset(dataset='cifar10', transform=transform, path=''), batch_size=batchSize, shuffle=True, num_workers=0)  # We use dataLoader to get the images of the training set batch by batch.


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


def get_dataset(dataset='', train=True, transform=None, target_transform=None, download=True, path='Datasets'):
    root = os.path.join(path, dataset)

    if dataset == 'cifar10':
        return CIFAR10(root=root,
                       train=train,
                       transform=transform,
                       target_transform=target_transform,
                       download=download)

    elif dataset == 'cifar100':
        return CIFAR100(root=root,
                        train=train,
                        transform=transform,
                        target_transform=target_transform,
                        download=download)

    elif dataset == 'mnist':
        return MNIST(root=root,
                     train=train,
                     transform=transform,
                     target_transform=target_transform,
                     download=download)

    elif dataset == 'stl10':
        return STL10(root=root,
                     split='train' if train else 'test',
                     transform=transform,
                     target_transform=target_transform,
                     download=download)

    elif dataset == 'lsun':
        return LSUN(root=root,
                    classes='train' if train else 'test',
                    transform=transform)

    elif dataset == 'imagenet':
        if train:
            root = os.path.join(root, 'train')
        else:
            root = os.path.join(root, 'val')

        return ImageFolder(root=root,
                           transform=transform,
                           target_transform=target_transform)