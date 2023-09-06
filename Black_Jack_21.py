### BLACK JACK 21點遊戲 ###

import random

Key = ("♠A","♠2","♠3","♠4","♠5","♠6","♠7",
       "♠8","♠9","♠10","♠J","♠Q","♠K",
       "♥A","♥2","♥3","♥4","♥5","♥6","♥7",
       "♥8","♥9","♥10","♥J","♥Q","♥K",
       "♦A","♦2","♦3","♦4","♦5","♦6","♦7",
       "♦8","♦9","♦10","♦J","♦Q","♦K",
       "♣A","♣2","♣3","♣4","♣5","♣6","♣7",
       "♣8","♣9","♣10","♣J","♣Q","♣K")

Value = (11,2,3,4,5,6,7,8,9,10,10,10,10,
11,2,3,4,5,6,7,8,9,10,10,10,10,
11,2,3,4,5,6,7,8,9,10,10,10,10,
11,2,3,4,5,6,7,8,9,10,10,10,10)

D = dict(zip(Key,Value))  #字典, 牌值

Cards = []  #牌庫
Dealer = []  #莊家
Player = []  #玩家
Dealer_Point = 0  #莊家點數
Player_Point = 0  #玩家點數

print("♠♥♦♣")  #遊戲開始

#洗牌
for i in range(len(Key)):
    Cards.append(Key[i])
random.shuffle(Cards)

##檢視牌庫
"""
print()
print(Cards)
print(D[Cards[2]])
"""

#發牌
print()
Player.append((Cards.pop()))
Player_Point += D[Player[-1]]
Dealer.append((Cards.pop()))
Dealer_Point += D[Dealer[-1]]
Player.append((Cards.pop()))
Player_Point += D[Player[-1]]

print("Dealer Hands:",Dealer,"\t","Ponint=", Dealer_Point)
print("Player Hands:",Player,"\t","Ponint=", Player_Point)

#Hit要牌 / Stand不要牌 / Surrender投降
print()
print("Hit or Stand or Surrender?")
Option = input()
while True:
    if Option == "Hit":
        Player.append((Cards.pop()))
        Player_Point += D[Player[-1]]
        if Player_Point <= 21:
            if len(Player) == 5:  #過五關
                print("Player Hands:",Player,"\t","Ponint=", Player_Point)
                Option = "Stand"
                continue
            print("Player Hands:",Player,"\t","Ponint=", Player_Point)
            print("Hit or Stand or Surrender?")
            Option = input()
        elif Player_Point > 21:
            if Player.count("♠A") > 0:
                Player[Player.index("♠A")]="♠A."
                Player_Point-= 10
                print("Player Hands:",Player,"\t","Ponint=", Player_Point)
                if len(Player) == 5:
                    Option = "Stand"
                    continue
                print("Hit or Stand or Surrender?")
                Option = input()
            elif Player.count("♥A") > 0:
                Player[Player.index("♥A")]="♥A."
                Player_Point-= 10
                print("Player Hands:",Player,"\t","Ponint=", Player_Point)
                if len(Player) == 5:
                    Option = "Stand"
                    continue
                print("Hit or Stand or Surrender?")
                Option = input()
            elif Player.count("♦A") > 0:
                Player[Player.index("♦A")]="♦A."
                Player_Point-= 10
                print("Player Hands:",Player,"\t","Ponint=", Player_Point)
                if len(Player) == 5:
                    Option = "Stand"
                    continue
                print("Hit or Stand or Surrender?")
                Option = input()
            elif Player.count("♣A") > 0:
                Player[Player.index("♣A")]="♣A."
                Player_Point-= 10
                print("Player Hands:",Player,"\t","Ponint=", Player_Point)
                if len(Player) == 5:
                    Option = "Stand"
                    continue
                print("Hit or Stand or Surrender?")
                Option = input()
            else:
                print("Player Hands:",Player,"\t","Ponint=", Player_Point)
                break
    elif Option == "Stand":
        while Dealer_Point < 17:  #未滿17點強迫莊家要牌
            Dealer.append((Cards.pop()))
            Dealer_Point += D[Dealer[-1]]
            if Dealer_Point > 21:  #爆牌時判斷莊家是否有A
                if Dealer.count("♠A") > 0:
                    Dealer[Dealer.index("♠A")]="♠A."
                    Dealer_Point-= 10
                elif Dealer.count("♥A") > 0:
                    Dealer[Dealer.index("♥A")]="♥A."
                    Dealer_Point-= 10
                elif Dealer.count("♦A") > 0:
                    Dealer[Dealer.index("♦A")]="♦A."
                    Dealer_Point-= 10
                elif Dealer.count("♣A") > 0:
                    Dealer[Dealer.index("♣A")]="♣A."
                    Dealer_Point-= 10
                elif len(Dealer) ==5:  #過五關
                    break
        print("Dealer Hands:",Dealer,"\t","Ponint=", Dealer_Point)
        break
    elif Option == "Surrender":
        print("YOU LOSE")
        break
    else:
        print("請輸入", "Hit(要牌) or Stand(不要牌) or Surrender(投降)")
        Option = input()

#判斷勝負  #PUSH平手
if Option != "Surrender":
    if len(Player) == 5:
        if Player_Point <= 21 :
            if len(Dealer) == 5:
                print("PUSH")
            elif Dealer_Point == 21:
                print("PUSH")
            else:
                print("YOU WIN")
        else:
            print("YOU LOSE")
    else:
        if Dealer_Point <= 21:
            if Player_Point <= 21:
                if Player_Point == 21 and len(Dealer) ==5:
                    print("PUSH")
                elif Player_Point > Dealer_Point and len(Dealer) !=5:
                    print("YOU WIN")
                elif Player_Point == Dealer_Point and len(Dealer) !=5:
                    print("PUSH")
                else:
                    print("YOU LOSE")
            else:
                print("YOU LOSE")
        else:
            print("YOU WIN")


#Play Again?


##檢視剩餘卡牌數
"""
print()
print(len(Cards))
"""