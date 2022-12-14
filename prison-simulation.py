import random
print("hello, prisoner game")
#make prisoners
prisoners=list(range(100))
#print(prisoners)

games=0
won_games=0
lost_games=0
#index of this list is a "box", value of index should match prisoner index
slip=list(range(100))
#number of played games
while games < 10000:
    #shuffle values in boxes...
    random.shuffle(slip)
    game_failed=False
    last_item = prisoners[-1]
    #game loop go through prisoner list
    for item in prisoners:
        k=0
        start_index = item
        #go through 50 boxes "indexes in slip list" looking for correct value
        while k < 50:
            if item == slip[start_index]:
                if item == last_item:
                    won_games +=1
                break
            #next index is the value in current index
            next_index = slip[start_index]
            start_index = next_index
            k +=1
            if k==50:
                game_failed=True
                #print("prisoner number:",item,"not found")
                break
        if game_failed == True:
            lost_games+=1
            #print("game failed")
            break
    games +=1

    percet=won_games/games
    if games == 10000:
        print("games won:",won_games,"win percent:", percet, "lost games:",lost_games)

