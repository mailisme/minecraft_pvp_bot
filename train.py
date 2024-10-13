import numpy as np
import torch
import torch.nn as nn
import os

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
x = np.random.rand(100000)
y = 1-x

class test(nn.Module):
    def __init__(self, numClasses=7):
        super(test, self).__init__()
        self.classifier = nn.Sequential(
            nn.Linear(1, 1),
        )

    def forward(self, x):
        return self.classifier(x)


model = test()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

dataset = zip(x, y)
loss_function = nn.MSELoss()

for x, y in dataset:
    optimizer.zero_grad()
    y = torch.tensor([y], dtype=torch.float)

    # Wrap the float value in a Tensor using torch.tensor()
    output = model(torch.tensor([x], dtype=torch.float))

    loss = loss_function(output, y)

    print(loss)

    loss.backward()
    optimizer.step()

print(model(torch.tensor([1], dtype=torch.float)))
os.makedirs("output", exist_ok=True)
torch.save(model, "output/1-1.pt")