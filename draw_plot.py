from config import Config
import matplotlib.pyplot as plt


def show_plot(best_chromosome, inf_time=False):
    """
    for displaying plot.
    
    Parameters
    ----------
    best_chromosome : [numpy.ndarray]
        [numpy array of best chromosome in population of chromosomes]
    """

    plt.figure(num=1)
    plt.clf()
    plt.axis([Config.plt_ax_x_min, Config.plt_ax_x_max, Config.plt_ax_y_min,
        Config.plt_ax_y_max])

    _draw_path_points()
    _draw_obstacles()

    best_path_x = []
    best_path_y = []

    plt.annotate('Start Point', xy=(Config.path_points[int(best_chromosome[0])][0] 
        + Config.plt_tolerance, Config.path_points[int(best_chromosome[0])][1]))
    plt.annotate('Goal Point', xy=(Config.path_points[int(best_chromosome[-1])][0]
        + Config.plt_tolerance, Config.path_points[int(best_chromosome[-1])][1]))

    plt.text(x=Config.plt_ax_x_min, y=Config.plt_ax_y_max + Config.plt_tolerance, 
        s='Generation:(%s)'%(Config.generations))

    for element in best_chromosome:

        best_path_x.append(Config.path_points[int(element)][0])
        best_path_y.append(Config.path_points[int(element)][1])

    plt.plot(best_path_x, best_path_y, "g-")
    plt.draw()
    plt.savefig("./docs/images/"+str(Config.img_iter_no)+".png")
    Config.img_iter_no += 1
    if not inf_time:
        plt.pause(0.01)
    else:
        plt.show()


def _draw_path_points():
    """
    for displaying path points on plot.
    """

    node_x = []
    node_y = []

    for element in Config.path_points:
        node_x.append(element[0])
        node_y.append(element[1])

    plt.plot(node_x, node_y, "ko")


def _draw_obstacles():
    """
    for displaying obstacles on plot.
    """

    obs_1_x = [0.5, 2.5, 2.5, 0.5, 0.5]
    obs_1_y = [1.5, 1.5, 2.5, 2.5, 2.5]
    plt.fill(obs_1_x, obs_1_y, "r")

    plt.legend(('Path points', 'Obstacles'), loc='upper right', fontsize='small',
               numpoints=1, markerscale=0.5, labelspacing=1)

    obs_2_x = [3, 5.5, 6, 3.5, 3.5]
    obs_2_y = [4, 2.5, 3, 4.5, 4.5]
    plt.fill(obs_2_x, obs_2_y, "r")

    obs_3_x = [5.5, 6, 6, 5.5, 5.5]
    obs_3_y = [1, 1, 3, 2.5, 3]
    plt.fill(obs_3_x, obs_3_y, "r")

    obs_4_x = [8, 9, 9, 8, 8]
    obs_4_y = [2.5, 2.5, 5.5, 5.5, 2.5]
    plt.fill(obs_4_x, obs_4_y, "r")

    obs_5_x = [9, 12, 12, 9, 9]
    obs_5_y = [3.5, 3.5, 4.5, 4.5, 3.5]
    plt.fill(obs_5_x, obs_5_y, "r")

    obs_6_x = [10, 11, 11, 10, 10]
    obs_6_y = [2.5, 2.5, 3.5, 3.5, 2.5]
    plt.fill(obs_6_x, obs_6_y, "r")

    obs_7_x = [1.5, 2.5, 2.5, 1.5, 1.5]
    obs_7_y = [8.5, 8.5, 9.5, 9.5, 8.5]
    plt.fill(obs_7_x, obs_7_y, "r")

    obs_8_x = [2.5, 3.5, 3.5, 2.5, 2.5]
    obs_8_y = [8.5, 8.5, 10.5, 10.5, 8.5]
    plt.fill(obs_8_x, obs_8_y, "r")

    obs_9_x = [5, 6, 6, 5, 5]
    obs_9_y = [8.5, 8.5, 10.5, 10.5, 8.5]
    plt.fill(obs_9_x, obs_9_y, "r")

    obs_10_x = [8, 9, 9, 8, 8]
    obs_10_y = [6.5, 6.5, 10, 10, 6.5]
    plt.fill(obs_10_x, obs_10_y, "r")

    obs_11_x = [9, 11, 11, 9, 9]
    obs_11_y = [8.5, 8.5, 10, 10, 8.5]
    plt.fill(obs_11_x, obs_11_y, "r")

    obs_12_x = [11.5, 13, 13, 11.5, 11.5]
    obs_12_y = [8.5, 8.5, 10.5, 10.5, 8.5]
    plt.fill(obs_12_x, obs_12_y, "r")

    obs_13_x = [8, 15, 15, 8, 8]
    obs_13_y = [5.5, 5.5, 6.5, 6.5, 5.5]
    plt.fill(obs_13_x, obs_13_y, "r")

    obs_14_x = [0.5, 6.5, 6.5, 0.5, 0.5]
    obs_14_y = [5.5, 5.5, 6.5, 6.5, 5.5]
    plt.fill(obs_14_x, obs_14_y, "r")
