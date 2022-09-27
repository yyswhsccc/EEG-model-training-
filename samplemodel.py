import torch.nn as nn
import torch
import torch.functional as F
import torchvision
import torch.optim as optim
import torchvision.transforms as trans
import matplotlib.pyplot as plt
import numpy as np

class Net(nn.Module):
    def _init_(self):
        super(Net, self)._init_()
        # 2 convolutinoal layers, 1 pooling layer, 3 fully connected layers
        self.conv_layer1 = nn.Conv2d(9,5,6) #9 inputs and 5 outputs, 6x6 kernel
        self.pool = nn.MaxPool2d(2,2) #pooling over a (2,2) window
        self.conv_layer2 = nn.Conv2d(45,10,6) #9 inputs and 5 outputs, 6x6 kernel
        self.fullyconnect1 = nn.Linear(10*6*6,120)
        self.fullyconnect2 = nn.Linear(120,84)
        self.fullyconnect3 = nn.Linear(84,10)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv_layer1(x)))
        x = self.pool(torch.relu(self.conv_layer2(x)))
        x = x.view(-1, 10*6*6)
        x = torch.relu(self.fullyconnect1(x))
        x = torch.relu(self.fullyconnect2(x))
        x = self.fullyconnect3(x)
        return x

net = Net()
print(net)

'''criterion = nn.MSELoss()#loss function calculate mean squared error
optimizer = optim.SGD(net.parameters(),lr=0.1, momentum=0.9)#optimizer
 
def epoch():
    for epochs in range(1000): #train 1000 times
        running_loss = 0.0
        for i, data in enumerate(trainloader,0): #need to load training data here
            inputs, labels = data
            optimizer.zero_grad() 
            output = net(input)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            

# save the model
PATH = './samplemodel.pth'
torch.save(net.state_dict(),PATH)'''






