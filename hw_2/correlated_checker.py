"""
Outputs stuff

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
a1 = -100
c1 = -100
a2 = 1
d1 = -1
b1 = -1
c2 = 1
b2 = 0
d2 = 0

p1 = 0
p2 = 0.5
p3 = 0.5
p4 = 0


########## Coarse Correlated ##########

# Utilities 
u1 =  a1*p1 + a2*p2 + b1*p3 + b2*p4   # Player 1
u2 =  c1*p1 + d1*p2 + c2*p3 + d2*p4   # Player 2

# Inequalities
u1_right1 = a1 * (p1+p3) + a2 * (p2+p4)
u1_right2 = b1 * (p1+p3) + b2 * (p2+p4)

u2_right1 = c1 * (p1+p2) + c2 * (p3+p4)
u2_right2 = d1 * (p1+p2) + d2 * (p3+p4)

# Output
print("------ Coarse Correlated Equilibrium ------")
print(f"> Player 1 Utility: {u1}")
print(f"> Player 2 Utility: {u2}")
print(f"> Equilibriums:")
print(f"       {u1} ≥? {u1_right1}")
print(f"       {u1} ≥? {u1_right2}")
print(f"       {u2} ≥? {u2_right1}")
print(f"       {u2} ≥? {u2_right2}")
