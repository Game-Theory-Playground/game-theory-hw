"""
Given the game and probability distribution, determines
if equalities for coarse correlated equilibrium
and correlated equilibrium hold true.


Set the variables as shown below for...

Game Utility: 

        C        D
-----------------------
A   (a1, c1)  (a2, d1) 
B   (b1, c2)  (b2, d2)


Probabilities:

        C        D
-----------------------
A       p1      p2 
B       p3      p4


"""

########## CHANGE THESE BASED ON PROBLEM ##########

u = [
    [(-100,-100), (1,-1)],
    [(-1,1), (0,0)],
]

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
print(f"> Inequalities:")

# Player 1  Inequalities 
for i in range(player1_strats):
    right = 0
    for j in range(player2_strats):
        for k in range(player2_strats):
            right += u[i][j][0] * p[k][j]
    print(f"       {u1} ≥? {right}")
    is_CCE = is_CCE and u1 >= right 
    
# Player 2  Inequalities 
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
# Player 1 inequalities 
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

# # Inequalities
# player1_left1 = a1*p1 + a2*p2
# player1_right1 = b1*p1 + b2*p2

# player1_left2 = b1*p3 + b2*p4
# player1_right2 = a1*p3 + a2*p4

# player2_left1 = c1*p1 + c2*p3
# player2_right1 = d1*p1 + d2*p3

# player2_left2 = d1*p2 + d2*p4
# player2_right2 = c1*p2 + c2*p4

# is_CE = (player1_left1 >= player1_right1 
# and player1_left2 >= player1_right2 
# and player2_left1 >= player2_right1 
# and player2_left2 >= player2_right2)

# # Output
# print("\n------  Correlated Equilibrium ------")
# print(f"> Player 1 Inequalities:")
# print(f"       {player1_left1} ≥? {player1_right1}")
# print(f"       {player1_left2} ≥? {player1_right2}")
# print(f"> Player 2 Inequalities:")
# print(f"       {player2_left1} ≥? {player2_right1}")
# print(f"       {player2_left2} ≥? {player2_right2}")
# print(f"> This is {'' if is_CE else 'Not '}a Correlated Equilibrium!")

