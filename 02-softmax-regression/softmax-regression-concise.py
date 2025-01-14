"""
------------------------------------------------------------------------
Softmax简洁实现
------------------------------------------------------------------------
"""
# 导入库
import torch
from torch import nn
from d2l import torch as d2l
# 加载Fashion MNIST数据集，并设置每个批次的样本数为256。这个函数返回训练集和测试集的数据迭代器。
batch_size = 256
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)

# PyTorch不会隐式地调整输入的形状。因此，
# 我们在线性层前定义了展平层（flatten），来调整网络输入的形状
net = nn.Sequential(nn.Flatten(), nn.Linear(784, 10))

def init_weights(m):
    '''
    初始化权重
    '''
    # 用于将线性层的权重初始化为均值为0、标准差为0.01的正态分布
    if type(m) == nn.Linear:
        nn.init.normal_(m.weight, std=0.01)
net.apply(init_weights)
# 定义损失函数和优化器
loss = nn.CrossEntropyLoss(reduction='none')
trainer = torch.optim.SGD(net.parameters(), lr=0.1)

num_epochs = 10
d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs, trainer)