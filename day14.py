import random
# def player():
#     initial = random.randint(1,6)
#     score = 0

#     for i in range(initial):
#         b = random.randint(1,6)
#         score=score+b
#     return score

# player1 = player() 
# player2 = player()  

# if player1 > player2:
#     print(f'player 1 wins with a score of {player1} and player 2 loses with a score of {player2}')
# elif player2 > player1:
#     print(f'player 2 wins with a score of {player2} and player 1 loses with a score of {player1}')
# else:
#     print(f'its a tie !!!!!! {player1}')    


# rpg game 
# role playing 

# player name : -

# once up on a atime in village there live a hero playername
# and in a cave there lice an enemy enemyname

# oneday they fought each other

# 1 player

# enemy


# playerhp= 100 
# enemyhp= 100

# 1 turn player x enemy , enemy x player


player = input('enter yppur player name:----')
enemy = random.choice(['dragon','goblin','orcs'])


playerhp = 100
enemyhp = 100
turn = 1

while playerhp>0 and enemyhp>0:
    print('turn',turn)
    playerdamage = random.randint(7,14)
    print(f'player attacked enemy and dealth damage of {playerdamage}')
    enemyhp = enemyhp - playerdamage
    print(f'enemyhp is :-- {enemyhp}')
    enemmydamage = random.randint(7,14)

    print(f'enemy attacked player and dealth damage of {enemmydamage}')
    playerhp = playerhp - enemmydamage

    print(f'playerhp is {playerhp}')
    turn = turn+1
    if playerhp < 0:
        print(f'player is dead {player}')
        break
    elif enemyhp < 0:
        print(f'player wins {player}')
        break


