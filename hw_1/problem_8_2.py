import matplotlib
matplotlib.use("TkAgg")  # Use a GUI backend
import matplotlib.pyplot as plt


if __name__ == "__main__":

    fig, axes = plt.subplots(2, 2)

    axes[0, 0].scatter([1], [1])
    axes[0, 0].set_xlabel("Probability Player 1: Confess")
    axes[0, 0].set_ylabel("Probability Player 2: Confess")
    axes[0, 0].set_title("Prisoner's Dilemma")
    axes[0, 0].set_xlim(0, 2)
    axes[0, 0].set_ylim(0, 2)

    plt.show(block=True)