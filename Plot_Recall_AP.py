import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    size = 5
    x = np.arange(size)
    # a = np.random.random(size)
    # b = np.random.random(size)
    # c = np.random.random(size)

    Recall = [0.981, 0.950, 0.852,  0.904, 0.909]
    Recall = np.array(Recall)
    AP = [0.983, 0.898, 0.761, 0.763, 0.821]
    AP = np.array(AP)
    fig = plt.figure(1)

    ax = fig.add_subplot(111)

    total_width, n = 0.8, 3
    width = total_width / n
    x = x - (total_width - width) / 2

    plt.bar(x, Recall, width=width, label='Recall',color=['blue'])
    plt.bar(x + width, AP, width=width, label='AP',color=['green'])
    plt.xlabel("Defect types")
    plt.ylabel("Performance")

    # plt.xticks(labels=('normal', 'brokenend', 'brokenpick', 'felter', 'oilstains', 'sundries'))
    labels=['normal','brokenpick', 'felter', 'sundries', 'brokenend', 'oilstains']
    ax.set_xticklabels(labels)
    # plt.bar(x + 2 * width, c, width=width, label='c')
    plt.legend()
    plt.show()

