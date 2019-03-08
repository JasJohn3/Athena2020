from torch.nn import *


class Discriminator(Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.main = Sequential(
            Conv2d(3, 64, 4, 2, 1, bias=False),
            LeakyReLU(0.2, inplace=True),
            Conv2d(64, 128, 4, 2, 1, bias=False),
            BatchNorm2d(128),
            LeakyReLU(0.2, inplace=True),
            Conv2d(128, 256, 4, 2, 1, bias=False),
            BatchNorm2d(256),
            LeakyReLU(0.2, inplace=True),
            Conv2d(256, 512, 4, 2, 1, bias=False),
            BatchNorm2d(512),
            LeakyReLU(0.2, inplace=True),
            Conv2d(512, 1, 4, 1, 0, bias=False),
            Sigmoid()
        )

    def forward(self, input):
        output = self.main(input)
        return output.view(-1)