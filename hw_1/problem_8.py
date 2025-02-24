import sys

import matplotlib
matplotlib.use("TkAgg")  # Use a GUI backend
import matplotlib.pyplot as plt
import numpy as np

if len(sys.argv) < 2:
    ARG = 4
else:
    ARG = int(sys.argv[1])


def normalize_vectors(u, v):
    magnitude = np.sqrt(u**2 + v**2)
    magnitude[magnitude == 0] = 1  # Avoid division by zero
    u_norm = u / magnitude
    v_norm = v / magnitude
    return u_norm, v_norm, magnitude


def compute_displacement_field(x, y, u11, u12, u21, u22)->[float, float]:
    """
    Assumes probability strategy is at row 1 for player 1 and col 2 for player 2.
    u11...u22 arrays  of the utilities [player1, player2] for each strategy. For
    example u12 is the strategy of the first row and 2nd column.
    TODO document this better
    """
    u = []
    v = []

    for x_temp, y_temp in zip(x,y):
        temp_u = []
        temp_v = []
        for xi,yi in zip(x_temp,y_temp):

            e_util_p1_r1 = u11[0]*yi + u12[0]*(1-yi) # Expected utility for player 1, row 1
            e_util_p1_r2 = u21[0]*yi + u22[0]*(1-yi) # Expected utility for player 1, row 2
            util_p1 = xi * e_util_p1_r1 + (1-xi) * e_util_p1_r2 # Actual utility for player 1
            
            ri = max(0,  e_util_p1_r1 - util_p1)
            ri_prime = max(0, e_util_p1_r2 - util_p1)
            ui = (xi + ri) / (1 + ri_prime)
            ui = ui - xi
            temp_u.append(ui)
            
            e_util_p2_r1 = u11[1]*xi + u21[1]*(1-xi)  # Expected utility for player 2, col 1
            e_util_p2_r2 = u12[1]*xi + u22[1]*(1-xi)  # Expected utility for player 2, col 2
            util_d = yi * e_util_p2_r1 + (1-yi) * e_util_p2_r2 # Actual utility for diving

            ri = max(0, e_util_p2_r1 - util_d)
            ri_prime = max(0, e_util_p2_r2 - util_d)
            vi = (yi + ri) / (1 + ri_prime)
            vi = vi - yi
            temp_v.append(vi)
            
        u.append(temp_u)
        v.append(temp_v)

    u = np.array(u)
    v = np.array(v)
    return u, v


def add_subplot(axes, i, scatter_x, scatter_y, u11, u12, u21, u22, x_label, y_label, title):
    x, y = np.meshgrid(np.linspace(0, 1, 20),  
                   np.linspace(0, 1, 20)) 
    

    u, v = compute_displacement_field(x, y, u11, u12, u21, u22)
    u,v, magnitude = normalize_vectors(u,v)
    if ARG == 4:
        axes[i].pcolormesh(x, y, magnitude, cmap="RdYlBu", shading='auto', alpha=0.5)
    
    axes[i].scatter(scatter_x, scatter_y, color="black")
    if ARG >= 3:
        axes[i].quiver(x,y,u,v)
    axes[i].set_xlabel(x_label)
    axes[i].set_ylabel(y_label)
    axes[i].set_title(title)
    axes[i].set_xlim(-0.1, 1.1)
    axes[i].set_ylim(-0.1, 1.1)

if __name__ == "__main__":

    

    fig, axes = plt.subplots(1,3)

    add_subplot(axes, 0, [1], [1],
                 [-3,-3], [0,-3],[-3,0], [-2,-2], 
                 "Probability Player 1: Confess", "Probability Player 2: Confess", "Prisoner's Dilemma")
    
    add_subplot(axes, 1, [0, 0.9090, 1], [1, 0.9090, 0],
                [0,0], [10,1], [1,10], [0,0], 
                "Probability Player 1: Insist", "Probability Player 2: Insist", "Insist-Accept")
    
    add_subplot(axes, 2, [0, 0.5, 1], [1, 0.5, 0],
            [-2,-2], [4,0], [0,4], [2,2],
            "Probability Player 1: Hawk", "Probability Player 2: Hawk", "Hawk-Dove")



    plt.show(block=True)