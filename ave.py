from config import Config
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import mean

def average_plot(ave):

    plt.figure
    plt.clf()
    plt.plot(ave)
    plt.draw()
    plt.title('Average Fitness each Generation')
    plt.ylabel('Average Fitness')
    plt.xlabel('Generation')
    plt.show()

    plt.savefig("./docs/images/average"+str(Config.img_iter_no)+".png")