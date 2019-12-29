Y = 20
X = 10

if not Y < 10:
    print("This statement is true")

C = 45
D = 55
if C > 45 and D > 29:
    print("This and gate is true")

if C >= 45 and D > 29:
    print("Now this and gate is true")

if not (Y < X and D > 2):
    print("The nand gate is true")

if (not(C > 49 ) or (D >69)):
    print("This or gate works properly")

if (Y == 22 and X == 11) or ((not(C == 46)) and (not(D == 57))):
    print ("This or gate also worked")
    


