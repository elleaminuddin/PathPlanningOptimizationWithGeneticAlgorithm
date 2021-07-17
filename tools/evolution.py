from config import Config
import matplotlib.pyplot as plt

def evolution_plot(progress):

    plt.figure(num=2)
    plt.clf()
    plt.plot(progress)
    plt.draw()
    plt.title('Best Fitness each Generation')
    plt.ylabel('Best Fitness')
    plt.xlabel('Generation')
    plt.show()

    plt.savefig("./docs/images/best"+str(Config.img_iter_no)+".png")
