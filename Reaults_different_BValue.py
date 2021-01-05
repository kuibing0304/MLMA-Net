import numpy as np
import  pandas as pd
import matplotlib.pyplot as plt




if __name__ == '__main__':

    #Ploting the Scatter on the Cifar10 and Cifar100
    Param_B=[10, 8, 5, 2, 1, 0.5, 0.1, 0.05, 0.005]
    Total_loss=[0.732, 0.803, 0.956, 0.868, 0.741, 0.572, 0.596, 0.684, 0.767]
    mAP_value=[79.13, 74.53, 71.48, 74.23, 82.04, 85.98, 85.69, 84.06, 80.41]

    #
    # Cifar10_Top5=[0.997, 0.997, 0.998, 0.995, 0.994]
    # Params_Cifar10_Top5 = [5552, 5540, 5528, 5512, 5500]
    #
    #
    # Cifar100_Top1 =[0.731, 0.749, 0.796, 0.776, 0.753]
    # Params_Cifar100_Top1 = [5556, 5542, 5536, 5520, 5500]
    #
    #
    # Cifar100_Top5 = [0.928, 0.926, 0.929, 0.911116, 0.9122]
    # Params_Cifar100_Top5 = [5556, 5542, 5536, 5520, 5500]

    ax=plt.subplot()

    plt.scatter(Total_loss, mAP_value, c='blue', marker='s')
    plt.xlabel('Total_loss')
    plt.ylabel('mAP')

    ax.grid(True, linestyle='--', linewidth=0.5,color="r")
    for i, txt in enumerate(Param_B):
        ax.annotate(txt,(Total_loss[i], mAP_value[i]), xycoords='data', xytext=(+8.5, -8.5), textcoords='offset points')
    plt.show()


    print("Scatter ploting OK!")