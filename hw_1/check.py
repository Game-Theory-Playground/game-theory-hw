import numpy as np
import matplotlib.pyplot as plt


x, y = np.meshgrid(np.linspace(0, 1, 20), np.linspace(0, 1, 20))

u = []
v = []

for x_temp, y_temp in zip(x,y):
    temp_u = []
    temp_v = []
    for xi,yi in zip(x_temp,y_temp):

        e_util_kr = 1 - 2*yi  # Expected utility for kick right
        e_util_kl = -1 + 2*yi # Expected utility for kick left
        util_k = xi * e_util_kr + (1-xi) * e_util_kl # Actual utility for kicking
        
        ri = max(0,  e_util_kr - util_k)
        ri_prime = max(0, e_util_kl - util_k)
        ui = (xi + ri) / (1 + ri_prime)
        ui = ui - xi
        temp_u.append(ui)
        
        e_util_dr = -1 + 2*xi  # Expected utility for dive right
        e_util_dl = 1 - 2*xi # Expected utility for dive left
        util_d = yi * e_util_dr + (1-yi) * e_util_dl # Actual utility for diving

        ri = max(0, e_util_dr - util_d)
        ri_prime = max(0, e_util_dl - util_d)
        vi = (yi + ri) / (1 + ri_prime)
        vi = vi - yi
        temp_v.append(vi)
        
    u.append(temp_u)
    v.append(temp_v)

u = np.array(u)
v = np.array(v)

magnitude = np.sqrt(u**2 + v**2)

fig, ax = plt.subplots(figsize=(6,6))
background = ax.pcolormesh(x, y, magnitude, cmap="RdYlBu", shading='auto')
fig.colorbar(background, label="Strategy Adjustment Magnitude")
ax.quiver(x, y, u, v, color="black")
ax.scatter([0.5], [0.5], color="white", edgecolors="black", s=100, label="Nash Equilibrium")

ax.set_xlabel("P[kick right]")
ax.set_ylabel("P[dive right]")
ax.set_title("Penalty Shot Game")
ax.legend()
plt.show()