import matplotlib
matplotlib.use("TkAgg")  # Use a GUI backend
import matplotlib.pyplot as plt


if __name__ == "__main__":

    fig, axes = plt.subplots(1,3)

    axes[0].scatter([1], [1])
    axes[0].set_xlabel("Probability Player 1: Confess")
    axes[0].set_ylabel("Probability Player 2: Confess")
    axes[0].set_title("Prisoner's Dilemma")

    axes[1].scatter([0.9090], [0.9090])
    axes[1].set_xlabel("Probability Player 1: Insist")
    axes[1].set_ylabel("Probability Player 2: Insist")
    axes[1].set_title("Insist-Accept")


    axes[2].scatter([0.5], [0.5])
    axes[2].set_xlabel("Probability Player 1: Hawk")
    axes[2].set_ylabel("Probability Player 2: Hawk")
    axes[2].set_title("Hawk-Dove")


    for i in range(3):
        axes[i, ].set_xlim(0, 1.1)
        axes[i, ].set_ylim(0, 1.1)

    plt.show(block=True)