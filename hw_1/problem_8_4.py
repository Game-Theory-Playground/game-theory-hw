import matplotlib
matplotlib.use("TkAgg")  # Use a GUI backend
import matplotlib.pyplot as plt
import numpy as np

def compute_displacement_field(x,y)->[float, float]:

    return u, v

if __name__ == "__main__":

    fig, axes = plt.subplots(1,3)

    x, y = np.meshgrid(np.linspace(0, 1, 20),  
                   np.linspace(0, 1, 20)) 
    

    u = 1-x
    v = 1-y
    magnitude = np.sqrt(u**2 + v**2)
    axes[0].pcolormesh(x, y, magnitude, cmap="RdYlBu", shading='auto', alpha=0.5)
    axes[0].scatter([1], [1], color="black")
    axes[0].quiver(x,y,u,v)

    axes[0].set_xlabel("Probability Player 1: Confess")
    axes[0].set_ylabel("Probability Player 2: Confess")
    axes[0].set_title("Prisoner's Dilemma")

    u = 0.9090-x
    v = 0.9090-y
    magnitude = np.sqrt(u**2 + v**2)
    axes[1].pcolormesh(x, y, magnitude, cmap="RdYlBu", shading='auto', alpha=0.5)
    axes[1].scatter([0.9090], [0.9090], color="black")
    axes[1].quiver(x,y,u,v, color="blue")
    axes[1].set_xlabel("Probability Player 1: Insist")
    axes[1].set_ylabel("Probability Player 2: Insist")
    axes[1].set_title("Insist-Accept")


    u = 0.5-x
    v = 0.5-y
    magnitude = np.sqrt(u**2 + v**2)
    axes[2].pcolormesh(x, y, magnitude, cmap="RdYlBu", shading='auto', alpha=0.5)
    axes[2].scatter([0.5], [0.5], color="black")
    axes[2].quiver(x,y,u,v, color="blue")
    axes[2].set_xlabel("Probability Player 1: Hawk")
    axes[2].set_ylabel("Probability Player 2: Hawk")
    axes[2].set_title("Hawk-Dove")


    for i in range(3):
        axes[i, ].set_xlim(0, 1.1)
        axes[i, ].set_ylim(0, 1.1)

    plt.show(block=True)