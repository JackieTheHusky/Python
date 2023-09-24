import random
import time
# op: starting Goal => easy, normal, hard, Impoosible
def into():
    print("Hi, welcome. This is going to be a simple game of texas hold'em, however, YOU won't be the only one playing('v')")
    time.sleep(1)
    print("Not only am I your wonderful dealer, I shall also be betting and calling with you")
    time.sleep(1)
    print("My only goal and the way to stop this endless grind will be when you lose all your coin ('v'). So be prepared.")
    time.sleep(1)
    print("Anyways, GL. I wish you have fun? Why else you try this")
    print("")
    time.sleep(1)
def starting_text():
    difficulty = input("Easy, Normal, Hard or Impossable ").strip()
    print("")
    match difficulty:
        case "Easy"|"easy":
            time.sleep(1)
            print("Starting simple I see. I don't fault you there. ")
            return(0)
        case "Normal"|"normal":
            time.sleep(1)
            print("Let's play this gamble shall we. ")
            return(1)
        case "Hard"|"hard":
            time.sleep(1)
            print("Oh ho ho. I see this isn't the first time is it ")
            return(2)
        case "impossable"|"Impossable":
            print("Ngl, This is legit impossible... ")
            time.sleep(1)
            double_check = input("You sure? ")
            if double_check == "yes" or double_check == "Yes":
                time.sleep(1)
                print("Cool, don't cry about it to me then")
                return(3)
            else:
                time.sleep(1)
                print("Wise decision")
                print("")
                starting_text()
        case "impossible"|"Impossible":
            print("Stickler for accuracy I see.")
            time.sleep(1)
            print("Ngl, This is legit impossible...")
            time.sleep(1)
            double_check = input("You sure? ")
            if double_check == "yes" or double_check == "Yes":
                time.sleep(1)
                print("Cool, don't cry about it to me then")
                return(3)
            else:
                time.sleep(1)
                print("Wise decision")
                print("")
                starting_text()
        case _ :
            time.sleep(1)
            print("Try that again. You probably misspelled something there. Not that I have the right to judge")
            starting_text()
# OP: Brain of dealer 
def brain_power(difficulty):
    match difficulty:
        case 0:
            return [random.randint(0,4),random.randint(0,4),random.randint(0,4)] 
        case 1:
            return[random.randint(0,3),random.randint(0,3),random.randint(0,3)]
        case 2:
            return[random.randint(0,2),random.randint(0,2),random.randint(0,2)]
        case 3:
            return[random.randint(0,1),random.randint(0,1),random.randint(0,1)]

#OP scoring
numberdic = {
    1 : "ace",
    2 : "2",
    3 : "3",
    4 : "4",
    5 : "5",
    6 : "6",
    7 : "7",
    8 : "8",
    9 : "9",
    10 : "10",
    11 : "jack",
    12 : "queen",
    13 : "king",
    14 : "club",
    15 : "diamond",
    16 : "heart",
    17 : "spade"
    }
reversenumberdic = {
    "club"    : .0002,
    "diamond" : .004,
    "heart"   : .06,
    "spade"   : .8,
    "ace" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "jack" : 11,
    "queen" : 12,
    "king" : 13
    }
suitstrainth = {
    "club"    : "a",
    "diamond" : "b",
    "heart"   : "c",
    "spade"   : "d",
}
#compnets:
def card_value(card):
    card_number = reversenumberdic[card[0]] + reversenumberdic[card[1]]
    return(card_number)
def high_card(c1,c2,hc1,hc2):
    fill_a = [card_value(c1),card_value(c2),card_value(hc1),card_value(hc2)]
    if max(fill_a) == card_value(c1) or max(fill_a) == card_value(c2):
        return "High Card"
def check_straight(dc1,dc2,dc3,dc4,dc5,c1,c2):
    fill_a = [reversenumberdic[dc1[0]],reversenumberdic[dc2[0]],reversenumberdic[dc3[0]],reversenumberdic[dc4[0]],reversenumberdic[dc5[0]],reversenumberdic[c1[0]],reversenumberdic[c2[0]]]
    fill_a.sort()
    fill_b = [fill_a[0]]
    while fill_a.count(reversenumberdic[c1[0]]) >= 2:
        fill_a.remove(reversenumberdic[c1[0]])
    while fill_a.count(reversenumberdic[c2[0]]) >= 2:
        fill_a.remove(reversenumberdic[c2[0]])
    a = len(fill_a)
    for i in range(1,a):
        if fill_a[i]==fill_a[i-1]+1:
            fill_b.append(fill_a[i])
        else:
            fill_b=[] 
    if len(fill_b)>= 5:
        return fill_b
def dupe_cards(dc1,dc2,dc3,dc4,dc5,c1,c2):
    filla = [dc1[0],dc2[0],dc3[0],dc4[0],dc5[0],c1[0],c2[0]]
    b = []
    c = []
    for i in range(7):
        a = 0
        for j in range(7):
            if filla[i] == filla[j]:
                a = a+1
        if a>=2:
            b.append([filla[i],a])
            for k in b:
                if k not in c:
                    c.append(k)
    if len(c) == 1:
        if filla[5] in c[0] or filla[6] in c[0]:
            match c[0][1]:
                case 2: total_score = 2 
                case 3: total_score = 4
                case 4: total_score = 8 
            return total_score
    if len(c) >= 2:
        fillb = [fillc[0] for fillc in c]
        fille = [fillc[1] for fillc in c]
        if (filla[5] in fillb) or (filla[6] in fillb):
            if max(fille) == 2:
                total_score = 3
            elif max(fille) == 3:
                total_score = 7
            elif max(fille) == 4:
                c = fille.index(4)
                if fillb[c] == filla[5] or fillb[c] == filla[6]:
                    total_score = 8
                else:
                    fille.remove(4)
                    match max(fille):
                        case 2: total_score = 2 
                        case 3: total_score = 4
            return total_score
def check_flush(dc1,dc2,dc3,dc4,dc5,c1,c2):
    filla = suitstrainth[dc1[1]]+suitstrainth[dc2[1]]+suitstrainth[dc3[1]]+suitstrainth[dc4[1]]+suitstrainth[dc5[1]]+suitstrainth[c1[1]]+suitstrainth[c2[1]]
    if filla.count(suitstrainth[c1[1]]) >= 5:
        return c1[1]
    elif filla.count(suitstrainth[c2[1]]) >= 5:
        return c2[1]
def print_card():
    number_value = (numberdic[random.randint(1,13)])
    suit_value = (numberdic[random.randint(14,17)])
    return [number_value, suit_value]
#list:
def create_list_straight(dc1,dc2,dc3,dc4,dc5,c1,c2):
    a = check_straight(dc1,dc2,dc3,dc4,dc5,c1,c2)
    fill_a = [dc1,dc2,dc3,dc4,dc5,c1,c2]
    fill_b = []
    for i in range(len(a)):
        for j in range(7):
            if a[i] == reversenumberdic[fill_a[j][0]]:
                fill_b.append(fill_a[j])
    return fill_b
def sorts(c):
    return reversenumberdic[c[0]]
def create_list_flush(dc1,dc2,dc3,dc4,dc5,c1,c2):
    a = check_flush(dc1,dc2,dc3,dc4,dc5,c1,c2)
    fill_a = [dc1,dc2,dc3,dc4,dc5,c1,c2]
    fill_b = []
    for i in range(7):
        if fill_a[i][1] == a:
            fill_b.append(fill_a[i])
    fill_b.sort(key=sorts)
    return fill_b
#THE SCORING
def scoring(dc1,dc2,dc3,dc4,dc5,c1,c2):
    total_score = 0
    flush = check_flush(dc1,dc2,dc3,dc4,dc5,c1,c2)
    straight = check_straight(dc1,dc2,dc3,dc4,dc5,c1,c2)
    dupe = dupe_cards(dc1,dc2,dc3,dc4,dc5,c1,c2)
    if flush is not None and straight is not None:
        straight_flush_list = []
        straight_list = create_list_straight
        for i in len(straight_list):
            if straight_list[i][1] == flush:
                straight_flush_list.append(straight_list[i])
            else:
                straight_flush_list = []
        if len(straight_flush_list) >= 5:
            total_score = 9
            if reversenumberdic[straight_flush_list[0][0]] == 13:
                total_score = 10
                return total_score
            return total_score
    elif dupe is not None:
        total_score = dupe
    if flush is not None and straight is None:
        if total_score <= 5:
            total_score = 6
            return total_score
    elif flush is None and straight is not None:
        if total_score <= 4:
            total_score = 5
    return total_score
def player_win(dc1,dc2,dc3,dc4,dc5,pc1,pc2,hc1,hc2):
    player_score = scoring(dc1,dc2,dc3,dc4,dc5,pc1,pc2)
    house_score = scoring(dc1,dc2,dc3,dc4,dc5,hc1,hc2)
    if player_score > house_score:
        return 1
    elif player_score < house_score:
        return None
    elif player_score == house_score:
        if high_card(pc1,pc2,hc1,hc2) is not None:
            return 1
        else:
            return None

#THE GAME
def fold():
    time.sleep(1)
    choice = ""
    while (choice.lower() != "yes" and choice.lower() != "no"):
        choice = input("Do you wish to fold? Type 'yes' or 'no'. ").strip()
    return choice
def choicefrc():
    time.sleep(1)
    choice = ""
    while (choice.lower() != "fold" and choice.lower() != "raise" and choice.lower() != "call"):
       choice = input("Do you wish to fold, raise, or call? ").strip()
    return choice
def raises_repeat():
    bet = 0
    while bet < 10:
        bet = int(input("How much do you want to raise. It must be more then 10 ").strip())
    return bet
def raises(coin):
    time.sleep(1)
    bet = raises_repeat()
    while coin - bet < 0:
        if bet > coin:
            print(f"Ah, sneaky, but you have {coin} amount to work with, so don't even try it.")
            bet = raises_repeat()
            time.sleep(1)
    while coin - bet >= 0:
        if coin - bet == 0:
            cho = ""
            while(cho.lower() != "yes" and cho.lower() != "no"):
                cho = input("Are you willing to go all in. This bet will leave you at 0 coins. ").strip()
                if cho.lower() == "yes":
                    time.sleep(1)
                    print("O, Ok then")
                    return None
                else:
                    print("Ah, I see. Let me ask again.")
                    time.sleep(1)
                    bet = raises_repeat()
        else:
            cho = ""
            while(cho.lower() != "yes" and cho.lower() != "no"):
                cho = input(f"You will have {coin-bet} left. Will this be ok? ").strip()
                if cho.lower() == "yes":
                    print("O, Ok then")
                    time.sleep(1)
                    return bet
                else:
                    print("Ah, I see. Let me ask again.")
                    time.sleep(1)
                    bet = raises_repeat()
    return bet
def starting():
    choice = ""
    cho = ""
    time.sleep(1)
    print("To start, you will have to give a min bet of 10 coins")
    while(choice.lower() != "yes" and choice.lower() != "no"):
        choice = input("Will this be ok? ").strip()
        if choice.lower() == "no":
            print("This will imply that you want this to end.")
            cho = ""
            while(cho.lower() != "yes" and cho.lower() != "no"):
                cho = input("Are you sure? ").strip()
                if cho.lower() == "yes":
                    print("O, Ok then")
                    time.sleep(1)
                    return "yes"
                else:
                    print("Ah, I see. Let me ask again.")
                    time.sleep(1)
                    choice = ""
        elif choice.lower() == "yes":
            print("Ah ok, let's get to it")
            time.sleep(1)
            return "no"
def houseraises():
    a = random.randint(1,int(str(coin-bet)[0]))
    b = len(str(coin-bet))
    raise_amount = a*pow(10,(b-1))
    print(f"I have decided to raise {raise_amount}")
    choice = ""
    while choice.lower() != "fold" and choice.lower() != "call" and choice.lower() != "match":
        choice = input("So do you wish to match my bet(call) or do you wish to fold. ").strip()
        if choice.lower() == "call" or choice.lower() == "match":
            cho = ""
            if coin-bet-raise_amount > 0:
                while cho.lower() != "yes" and cho.lower() != "no":
                    cho = input(f"Are you sure? You will have {coin-bet-raise_amount} left. ").strip()
                    if cho.lower() == "yes":
                        return raise_amount
                    else:
                        choice = ""
            else:
                while cho.lower() != "yes" and cho.lower() != "no":
                    cho = input(f"Are you sure? You will have to give everything you have? In other words, you'll be going all in. ").strip()
                    if cho.lower() == "yes":
                        return 0
                    else:
                        choice = ""
        elif choice.lower() == "fold":
            cho = ""
            while cho.lower() != "yes" and cho.lower() != "no":
                cho = input(f"Are you sure? The total pool is {2*bet}. ").strip()
            if cho.lower() == "yes":
                return None
            else:
                choice = ""
#  Start:
into()
print("How hard do you wish for this to be. Note this only impacts how I plays agaisnt you.")
difficulty = starting_text()
print("Well let's the game begin")
print("")
time.sleep(1)
print("You will start with 100 coins")
coin = 100
total_round = 0
print("Well. Let's start")
time.sleep(1)
#The Game
round = 0
just_end_it = "no"
while coin > 10 and just_end_it == "no":
    card_list = []
    while len(card_list) < 10:
        a = print_card()
        if a not in card_list:
            card_list.insert(0,a)
    #card list
    dc1 = card_list[0]
    dc2 = card_list[1]
    dc3 = card_list[2]
    dc4 = card_list[3]
    dc5 = card_list[4]
    pc1 = card_list[5]
    pc2 = card_list[6]
    hc1 = card_list[7]
    hc2 = card_list[8]
    #Start of Game
    just_end_it = starting()
    if just_end_it == "yes":
        break
    coin = coin - 10
    folding = "no"
    bet = 0
    #What the house does
    if round == 0:
        b = player_win(dc1,dc2,dc3,dc4,dc5,pc1,pc2,hc1,hc2)
        difficult = brain_power(difficulty)
    #Round loops 2 times
    while round < 3:
        print(f"You have {coin}.")
        shown_card_list = [card_list[0],card_list[2],card_list[3]]
        a = card_list[round+2]
        if a not in shown_card_list:
            shown_card_list.insert(0,a)
        time.sleep(1)
        print(f"There are {shown_card_list} on the table")
        print(f"In your hand you have {pc1, pc2}")
        time.sleep(1)
        #Pick Fold, Raise, Call
        ychoice = choicefrc()
        time.sleep(1)
        match ychoice:
            case "fold":
                print("O, ok")
                round = 4
                folding = "yes"
            case "raise":
                a = raises(coin)
                if round == 0:
                    print("O, someone is confident I see. Well, I wonder if that was a good idea.")
                    bet = bet + a
                elif round >= 1:
                    print("Ah, I bet you like what you are seeing.")
                    bet = bet + a
                if a == None:
                    round = 4
                    bet = coin
            case "call":
                print("O, I see. You have decided to call.")
                if difficult[round] == 0:
                    if b is None:
                        bets = houseraises()
                        if bets == None:
                            bet = coin
                            round = round + 4
                        round = round + 1
                    else:
                        print("I shall also call")
                        round = round + 1
                else:
                    if b == 1:
                        bets = houseraises()
                        if bets == None:
                            bet = coin
                            round = round + 4
                        round = round + 1
                    else:
                        print("I shall also call")
                        round = round + 1
    #End
    if round >= 3:
        if folding == "no":
            print("Calculating Win")
            time.sleep(3)
            if b == 1:
                print("You win")
                coin = coin + 2*bet + 20
            elif b is None:
                coin = coin - bet
        else:
            coin = coin - bet
            print(f"Because you folded, you lost {bet+10} coins. I wish you luck next time")
        #Continue?
        total_round = total_round + 1
        print(f"You have {coin} and you are had played {total_round} rounds.")
        c = input(f"Do you wish to continue? You have {coin} left ").strip()
        if c.lower() == "no":
            print("Ah, ok. I hope you had fun")
            just_end_it == "yes"
            break
        else:
            print("O. Ok. Very cool")
            round = 0
#Scoring
time.sleep(1)
print(f"At the end you had lasted {total_round} rounds, and had {coin}")
