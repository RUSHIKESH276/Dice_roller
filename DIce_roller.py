import random
players=[]
first_six=False
print("Enter number of players")
p1=int(input())
print("Enter names of",p1,"players")
i=1
while i<=p1:
    nm=input()
    players.append(nm)
    i=i+1
player_index=0
while True:
    print("\nPlease play your turn:",players[player_index])
    input("Press Enter to Roll the Dice")
    score=random.randint(1,6)
    print("You rolled:",score)
    if score==6 and first_six==False:
        print("Please repeat your turn")
        first_six=True
    elif score==6 and first_six==True:
        print(players[player_index],"wins!")
        break
    else:
        player_index=player_index+1
        first_six=False
        if player_index==p1:
            player_index=0