from torch.nn import *


class Generator(Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.main = Sequential(
            ConvTranspose2d(100, 512, 4, 1, 0, bias=False),
            BatchNorm2d(512),
            ReLU(True),
            ConvTranspose2d(512, 256, 4, 2, 1, bias=False),
            BatchNorm2d(256),
            ReLU(True),
            ConvTranspose2d(256, 128, 4, 2, 1, bias=False),
            BatchNorm2d(128),
            ReLU(True),
            ConvTranspose2d(128, 64, 4, 2, 1, bias=False),
            BatchNorm2d(64),
            ReLU(True),
            ConvTranspose2d(64, 3, 4, 2, 1, bias=False),
            Tanh()
        )

    def forward(self, input):
        output = self.main(input)
        return output