# import random

# team1={
#     {'name1':'kushi',
#     'score':0},
#     {'name2':'anusha',
#     'score':0},
#     {'name3':'siri',
#     'score':0},
#     {'name4te':'muskan',
#     'score':0},
#     {'name5':'shabira',
#     'score':0},
#     {'name6':'sowjanya',
#     'score':0},
#     {'name7':'thapa',
#     'score':0},
#     {'name8':'jayasree',
#     'score':0},
#     {'name9':'somi',
#     'score':0},
#     {'name10':'sarika',
#     'score':0},
#     {'name11':'sathya',
#     'score':0}
# }
# team2={
#     {'name1':'preethi',
#     'score':0},
#     {'name2':'mamatha',
#     'score':0},
#     {'name3':'vishaka',
#     'score':0},
#     {'name4':'arthi',
#     'score':0},
#     {'name5':'dhanasree',
#     'score':0},
#     {'name6':'shuba',
#     'score':0},
#     {'name7':'rubina',
#     'score':0},
#     {'name8':'priyanka',
#     'score':0},
#     {'name9':'jhansi',
#     'score':0},
#     {'name10':'ruchi',
#     'score':0},
#     {'name11':'priya',
#     'score':0},
# }


import random
import randomshuffle
Atotal=[]
Btotal=[]
balls=["---------"]
list=[1,2,3,4,6]
out=["run out","catch out"]
print("choose teams\n")
teams={'team':["a","b","c","d","e","f","g","h","k","l","m"],'team':["anushu","shabbu","laddu","mahiks","manu","siri","janu","chinni","chinna","pavani"]}
keys=teams.keys
for keys in teams:
    print(keys)
def select_team(team):
    if team in teams:
        selected_team=team
        return selected_team
    else:
        selected_team==str(input("enter name"))
        return selected_team
first_team=str(input("\nenter 1st team choice:"))
firstTeam=select_team(first_team)
second_team=str(input("enter the second choice"))
secondTeam=select_team()
if secondTeam==firstTeam:
    print("this team is already choice by your ")
    secondTeam=str(input("..."))
    select_team(secondTeam)
else:
    pass
print("firstTeam")
print("secondTeam") 
players=[firstTeam,secondTeam]
print("start")
print("firstTeam")
# print("toss")
tosscall=["------"]
batball=["------"]
toss=input("enter what u want")
while toss:
    if toss in tosscall:
        print(toss)
        randomshuffle(tosscall)
        print(tosscall)
        break
    else:
        print("-----")
        #toss=input("----")
        continue
def tosstime(team_a,team_b):
    print(team_a)
    call=input("-----")
    try:
        if call not in batcall:
            print("----")
            #call=input("---")
    finally:
        print(team_a,call)
        if call=="bat":
            bating_team,bowling_team=teams[team_a],teams[team_b]
        elif call=="bowl":
            bating_team,bowling_team=teams[team_b],teams[team_a]
            return bating_team,bowling_team
def innings(bating_team,bowling_team,first_score):
    bating_team_list=teams[bating_team]
    bating_option=iter(bating_team_list)  
    on_strike=next(bating_option) 
    on_strike_scores=[]
    players_scores=[]
    wickets=10
    total=[]
    team_total=0
    bowling_options=teams[bowling_team][5:]
    for over in range(0,3):
        bowler=choice(bowling_options)
        print(on_strike,bowler)
        print("any key to respond")
    for ball in range(1,7):
        ball_delivered=choice(balls)
        played_for=choice(balls)
        if wickets==0 or team_total1>first_score:
            break
        elif ball_delivered==played_for:
            print(over,ball)
            print(bowler,on_strike)
            player_scores=sum(on_strike_scores)
            team_total=sum(total)
            out_player_scores={on_strike:players_scores}
            print(f'{batting_team} is at {team_team1}')
            print(out_player_scores)
            on_strik=next(batting_opti0ns)
            print(f'{on_strike} is on_strike')
            wickets-=1
            on_strike_scores=[0]
            time.sleep(2)

        else:
            print(f'{over}.{ball}',end="")
            start=time.time()
            input("")
            time_taken=end-start
            if time_taken<1:
                print("A sixx")
                total.append(6)
                on_strike_scores.append(6)
                player_scores=sum(on_strike_scores)
                team_total=sum(total)
                if team_total>first_scores:
                    break
            elif (time_taken>1) and (time_taken<1.5):
                print("boundaryy!!!")
                total.append(4)
                on_strike_scores.append(4)
                player_scores=sum(on_strike_scores)
                team_total=sum(total)
                if team_total>first_scores:
                    break
            elif (time_taken>2) and (time_taken<2.5):
                print("boundaryy!!!")
                total.append(2)
                on_strike_scores.append(2)
                player_scores=sum(on_strike_scores)
                team_total=sum(total)
                if team_total>first_scores:
                    break
            elif (time_taken>2.5) and (time_taken<3):
                print(f'{on_strike} duck the ball')
                total.append(0)
                on_strike_scores.append(0)
                player_scores=sum(on_strike_scores)
                team_total=sum(total)
                if team_total>first_scores:
                    break
            elif ((time_taken>1.5) and (time_taken<2)) or time_taken>3:
                print(f'{choice(out)} {bowler} has taken the wicket of {on_strike}')
                player_scores=sum(on_strike_scores)
                team_total=sum(total)
                out_player_scores={on_strike:player_scores}
                print(f'{batting_team} is at {team_total}')
                print(out_player_scores)
                on_strike=next(batting_options)
                wicket-=1
                on_strike_scores=[0]
                player_scores=[0]
            print(f'{batting_team} is at {team_total}')
            print(f'{on_strike} is at {player_scores}\n')
    return team_total

#game logic
if toss==tosscall[0]:
    toss_time(firstTeam,secondTeam)
    first_innings_total=innings(firstTeam.scondTeam,1000)#1000 is juat a big score
    print(f'{seconTeam} needs {first_innings_total} scores to win the match')
    second_innings_total=innings_seconTeam,firstTeam,first_innings_total
    if first_innings_total>second_innings_total:
        print(f'{firstTeam} has won the match')
    elif second_innings_total>first_innings_total:
        print(f'{seconTeam} has won the match')
    elif first_innings_total==second_innings_total:
        print('draw \n both teams scored same runs')
if toss==tosscall[1]:
    toss_time(secondTeam,firstTeam)
    first_innings_toral=innings(secondTeam,firsTeam,1000)
    print(f'{firstTeam} needs {first_innings_total} scores to won the match')
    second_innings_total=innings(firstTeam,secondTeam,first_innings_total)
    if first_innings_total>secong_innings_total:
        print(f'{firstTean} has won the match')
    elif second_innings_total>first_innings_total:
        print(f'{secondTeam} has won the match')
    elif first_innings_total==second_innings_total:
        print("drawww!!! \n both teams scored same runs")

    





            
            
            
            
                    
