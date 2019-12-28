import random
from numpy.random import choice

# Line of each game
NotreDame = 3.5
PennState = 7.0
LSU = 13.5
Clemson = 2.0

## Will be taking a random number between 0 and 56 (feasibly one will not score more than 56 points) and then add the spread
## If greater than 28 than the favorite wins, otherwise the underdog

# ND_ISU = ['Notre Dame', 'Iowa State']

def ND_ISU():
    rand_Num = random.randint(1,57)
    rand_ND = rand_Num + NotreDame
    if rand_ND > 28:
        print("Notre Dame")
    else:
        print("Iowa State")

def PSU_MEM():
    rand_Num = random.randint(1,57)
    rand_PSU = rand_Num + PennState
    if rand_PSU > 28:
        print("Penn State")
    else:
        print("Memphis")
        
def LSU_OKLA():
    rand_Num = random.randint(1,57)
    rand_LSU = rand_Num + LSU
    if rand_LSU > 28:
        print("LSU")
    else:
        print("Oklahoma")
        
def CLEM_OSU():
    rand_Num = random.randint(1,57)
    rand_Clem = rand_Num + Clemson
    if rand_Clem > 28:
        print("Clemson")
    else:
        print("Ohio State")


def main():
  ND_ISU()
  PSU_MEM()
  LSU_OKLA()
  CLEM_OSU()
  
if __name__== "__main__":
  main()

