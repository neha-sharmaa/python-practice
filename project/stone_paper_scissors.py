import random

comp_turn = random.randint(1,3)
#print(comp_turn)

def game_win(comp_turn, you):
    if(comp_turn == you): 
            return None
        elif(comp_turn == 1):
            if(you == 2):
                return True
            elsi

  '''  elif(comp_turn == 1) and (you == 3):
        return False
    elif(comp_turn == 2) and (you == 2):
        return None
    elif(comp_turn == 2) and (you == 3):
        return True
    elif(comp_turn == 2) and (you == 1):
        return True
    elif(comp_turn == 3) and (you == 3):
        return None
    elif(comp_turn == 3) and (you == 2):
        return True
    else:
        return False'''

    you = input("choose from any one snake(1), water(2), gun(3)?")
    print(you)

    a = game_win(comp_turn, you)
    print(a)
    if (a == None):
        print("Game is tie")
    elif(a == True):
        print("you win")
    else:
        print("you loose")