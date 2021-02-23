from cnn_functions import LeNet5
import matplotlib.pyplot as plt
from matplotlib.pyplot import pcolor
from fileIO import openMNIST
import numpy as np
import pandas as pd
from functions import train_cnn, eval_cnn
from cnn_functions import LeNet5
from cnn_functions import CustomNet
from cnn_functions import linear_comb
from plots_and_stuff import plotTrainTestPerformance

def go(train, test):
    print('i am running')
    print('---')
    x_train, y_train = openMNIST(train)
    x_test, y_test = openMNIST(test)

    # reshape and flip data to have it in matrix format
    x_train = x_train.reshape(-1, 28, 28, order='C')
    x_train = np.flip(x_train[:], 1)
    x_test = x_test.reshape(-1, 28, 28, order='C')
    x_test = np.flip(x_test[:], 1)
    # confirmation plots
    # print(y_test[600])
    # fig = pcolor(x_test[600], cmap='gist_gray')
    # plt.show()
    # print('LeNet5')
    # lenet = LeNet5()
    # model, _ = train_cnn(lenet,x_train, y_train)
    # acc = eval_cnn(model,x_test, y_test)
    # print(acc)
    # print('CustomNet')
    # custom = CustomNet()
    # model, _ = train_cnn(custom, x_train, y_train)
    # acc = eval_cnn(model,x_test, y_test)
    # print(acc)
    print('linear ensample')
    linear_co = linear_comb()
    model, train_acc, test_acc = train_cnn(linear_co, x_train, y_train, x_test, y_test, track_train_test_acc=True)
    acc = eval_cnn(model, x_test, y_test)
    print('accuracy on testing:', acc)
    plotTrainTestPerformance(train_acc, test_acc, 'Epochs')


if __name__ == "__main__":
    # local path
    train = 'data/mnist_train.csv'
    test = 'data/mnist_test.csv'
    go(train,test)
