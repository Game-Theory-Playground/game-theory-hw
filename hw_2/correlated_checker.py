"""
Given a 2-player game utilities (u) and probability distribution (p), 
determines if the equalities for coarse correlated equilibrium
and correlated equilibrium hold true.

"""

########## CHANGE THESE BASED ON PROBLEM ##########

# Utility
u = [
    [(-100,-100), (1,-1)],
    [(-1,1), (0,0)],
]

# Probability
p = [
    [0, 0.5],
    [0.5, 0]
]



########## Coarse Correlated ##########
player1_strats = len(u[1])
player2_strats = len(u)
prob_count = len(p) * len(p[1])
is_CCE = True

# Utilities 
u1 = 0
u2 = 0
for i in range(player1_strats):
    for j in  range(player2_strats):
        u1 += u[i][j][0] * p[i][j]
        u2 += u[i][j][1] * p[i][j]
    
print("------ Coarse Correlated Equilibrium ------")
print(f"> Player 1 Utility: {u1}")
print(f"> Player 2 Utility: {u2}")

print(f"> Player 1 Inequalities:")
# Player 1  Inequalities 
for i in range(player1_strats):
    right = 0
    for j in range(player2_strats):
        for k in range(player2_strats):
            right += u[i][j][0] * p[k][j]
    print(f"       {u1} ≥? {right}")
    is_CCE = is_CCE and u1 >= right 
    
print(f"> Player 2 Inequalities:") 
for i in range(player2_strats):
    right = 0
    for j in range(player1_strats):
        for k in range(player2_strats):
            right += u[j][i][1] * p[j][k]
    print(f"       {u2} ≥? {right}")
    is_CCE = is_CCE and u2 >= right 
  


print(f"> This is {'' if is_CCE else 'Not '}a Coarse Correlated Equilibrium!")



# ########## Correlated ##########
is_CE = True

print("\n------  Correlated Equilibrium ------")

print(f"> Player 1 Inequalities:")
for i in range(player1_strats):
    for j in range(player1_strats):
        if i == j:
            continue

        left = 0
        right = 0

        for k in range(player2_strats):
            left += u[i][k][0] * p[i][k]
            right += u[j][k][0] * p[i][k]
        print(f"       {left} ≥? {right}")
        is_CE = is_CE and left >= right 

print(f"> Player 2 Inequalities:")
for i in range(player2_strats):
    for j in range(player2_strats):
        if i == j:
            continue

        left = 0
        right = 0

        for k in range(player1_strats):
            left += u[k][i][1] * p[k][i]
            right += u[k][j][1] * p[k][i]
        print(f"       {left} ≥? {right}")
        is_CE = is_CE and left >= right 


print(f"> This is {'' if is_CE else 'Not '}a Correlated Equilibrium!")

