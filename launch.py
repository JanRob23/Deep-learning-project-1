from typing import Coroutine
from CNNs import LeNet5
import matplotlib.pyplot as plt
from matplotlib.pyplot import pcolor
from fileIO import openMNIST
import numpy as np
import pandas as pd
from functions import train_cnn, eval_cnn, crossvalidationCNN, train_linear_models_plus_average, test_model
from CNNs import LeNet5
from CNNs import CustomNet
from linear_nets import linear_one, linear_two, linear_three, linear_four, linear_five
from plots_and_stuff import plotTrainTestPerformance
import time

def go(train, test):
    print('i am running')
    print('---')
    x_train, y_train, x_test, y_test = reshape_data(train, test)




    #-----------LeNet 5 ---------------
    # print('LeNet5 default')
    # sets = {'learning_rate':0.0005, 'l2': 0}
    # leNet = LeNet5()
    # test_model(leNet, x_train, y_train, x_test, y_test, sets)
    #
    # print('LeNet5 learning rate: 0.01')
    # sets = {'learning_rate':0.01, 'l2': 0}
    # leNet = LeNet5()
    # test_model(leNet, x_train, y_train, x_test, y_test, sets)
    #
    print('LeNet5 l2: 0.002')
    sets = {'learning_rate':0.0005, 'l2': 0.002}
    leNet = LeNet5()
    test_model(leNet, x_train, y_train, x_test, y_test, sets)
    #
    # print('LeNet5 drop: 0.25')
    # sets = {'learning_rate':0.0005, 'l2': 0}
    # leNet = LeNet5(drop= True)
    # test_model(leNet, x_train, y_train, x_test, y_test, sets)
    #
    # print('CustomNet')
    # sets = {'learning_rate':0.0005, 'l2': 0}
    # custom = CustomNet()
    # test_model(custom, x_train, y_train, x_test, y_test, sets)





    # epoch_eval_single(leNet, x_train, y_train, x_test, y_test)
    # # cross_val(lenet, x_train, y_train, x_test, y_test)
    # test_model(leNet, x_train, y_train, x_test, y_test)


    #----------- CustomNet --------------#
    # print('CustomNet')
    # custom = CustomNet()

    # epoch_eval_single(custom, x_train, y_train, x_test, y_test)
    # # cross_val(custom, x_train, y_train, x_test, y_test)
    # test_model(custom, x_train, y_train, x_test, y_test)


    #----------- Linear --------------#
    print("Linear Nets, best Hyperparameters")
    train_linear_models_plus_average(x_train, y_train, x_test, y_test, track_train_test_acc=True)

    # cross_val(linear_one(dropout=0.25), x_train, y_train, x_test, y_test)
    # cross_val(linear_two(dropout=0.25), x_train, y_train, x_test, y_test)
    # cross_val(linear_three(dropout=0.25), x_train, y_train, x_test, y_test)
    # cross_val(linear_four(dropout=0.25), x_train, y_train, x_test, y_test)
    # cross_val(linear_five(dropout=0.25), x_train, y_train, x_test, y_test)


def reshape_data(train, test):
    x_train, y_train = openMNIST(train)
    x_test, y_test = openMNIST(test)

    # reshape and flip data to have it in matrix format
    x_train = x_train.reshape(-1, 28, 28, order='C')
    x_train = np.flip(x_train[:], 1)
    x_test = x_test.reshape(-1, 28, 28, order='C')
    x_test = np.flip(x_test[:], 1)
    return x_train, y_train, x_test, y_test

def confirmation_plots(x_test, y_test):
    print(y_test[600])
    fig = pcolor(x_test[600], cmap='gist_gray')
    plt.show()

def epoch_eval_single(model, x_train, y_train, x_test, y_test):
    model, train_acc, test_acc = train_cnn(model ,x_train, y_train, x_test, y_test, track_train_test_acc=True, epochs= 100)
    acc = eval_cnn(model,x_test, y_test)
    print(acc)
    plotTrainTestPerformance(train_acc, test_acc, 'Epochs')

def cross_val(model, x_train, y_train, x_test, y_test):
    start = time.time()
    train_acc, test_acc, m_list, change = crossvalidationCNN(model, x_train, y_train, 5)
    plotTrainTestPerformance(train_acc, test_acc, change, m_list)
    end = time.time()
    print("cross_val took: ", (start-end))

if __name__ == "__main__":
    # local path
    train = 'data/mnist_train.csv'
    test = 'data/mnist_test.csv'
    go(train,test)

