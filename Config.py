import math as ma
import numpy as np

path_points = [[1, 11], [1, 8], [4, 11], [4, 8], [7, 11], [7, 8], [10.5, 11], [9.5, 7.5], [12, 8], [14, 7.5],
 [14, 11], [7, 5], [5, 5], [1, 5], [1, 3], [1, 1], [4.5, 2],  [7, 1], [9.5, 1], [9.5, 3], [11.5, 1], [14, 1],
 [14, 3], [14, 5], [9.5, 5], [11.5, 3]]
npts = len(path_points)
pop_max = 100
crossover_rate = 0.8
mutation_rate = 0.01
"change so user is able to input start and end node"
start_index = int(input("Choose the starting point:"))
end_index = int(input("Choose the end point:"))
print("Starting Point is:", start_index)
print("End Point is:", end_index)
generations = 0
prev_best_fitness = 0
nobs = 14
nbits = ma.log10(npts) / ma.log10(2)
x =  int(((nobs+2)*nbits)/nbits)
chr_len = int(x)
stop_criteria = 0
stop_generation = False
img_iter_no = 1
plt_tolerance = -1
plt_ax_x_min = -1.0
plt_ax_x_max = 18.0
plt_ax_y_min = -1
plt_ax_y_max = 18.0


def define_links():
    """
    This function defines the links b/w path points
    
    Returns
    -------
    [numpy.ndarray]
        [Every path point has a number of allowed connection with other path 
        points. Those allowed connections are defined below. During calculation
        of fitness of population if two consecutive path points are connected
        then the fitness of that chromosome increases]
    """

    link = -1 * np.ones((26, 5))



    link[0][0] = 0
    link[0][1] = 1
    link[0][2] = 2
    link[1][0] = 1
    link[1][1] = 3
    link[2][0] = 2
    link[2][1] = 3
    link[2][2] = 4
    link[3][0] = 3
    link[3][1] = 1
    link[3][2] = 2
    link[3][3] = 5
    link[4][0] = 4
    link[4][1] = 2
    link[4][2] = 5
    link[4][3] = 6
    link[5][0] = 5
    link[5][1] = 3
    link[5][2] = 4
    link[5][3] = 11
    link[6][0] = 6
    link[6][1] = 4
    link[6][2] = 10
    link[7][0] = 7
    link[7][1] = 8
    link[7][2] = 9
    link[8][0] = 8
    link[8][1] = 9
    link[8][2] = 7
    link[9][0] = 9
    link[9][1] = 8
    link[9][2] = 10
    link[9][3] = 7
    link[10][0] = 10
    link[10][1] = 9
    link[10][2] = 6
    link[11][0] = 11
    link[11][1] = 12
    link[11][2] = 17
    link[11][3] = 5
    link[12][0] = 12
    link[12][1] = 13
    link[12][3] = 11
    link[13][0] = 13
    link[13][1] = 14
    link[13][3] = 12
    link[14][0] = 14
    link[14][1] = 16
    link[15][0] = 15
    link[15][1] = 16
    link[16][0] = 16
    link[16][1] = 15
    link[16][2] = 14
    link[17][0] = 17
    link[17][1] = 18
    link[17][2] = 11
    link[18][0] = 18
    link[18][1] = 17
    link[18][2] = 20
    link[18][3] = 19
    link[19][0] = 19
    link[19][1] = 20
    link[19][2] = 18
    link[20][0] = 20
    link[20][1] = 19
    link[20][2] = 21
    link[20][3] = 25
    link[20][4] = 18
    link[21][0] = 21
    link[21][1] = 22
    link[21][2] = 25
    link[21][3] = 20
    link[22][0] = 22
    link[22][1] = 25
    link[22][2] = 23
    link[22][3] = 21
    link[23][0] = 23
    link[23][1] = 24
    link[23][2] = 22
    link[24][0] = 24
    link[24][1] = 23
    link[25][0] = 25
    link[25][1] = 21
    link[25][2] = 22
    link[25][3] = 20

    return link
