import random

#data of cards/ stuff realting to cards
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
    "club"    : "a",
    "diamond" : "b",
    "heart"   : "c",
    "spade"   : "d",
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
    "club"    : 1,
    "diamond" : 2,
    "heart"   : 3,
    "spade"   : 4,
}

#print_card
def print_card():
    number_value = (numberdic[random.randint(1,13)])
    suit_value = (numberdic[random.randint(14,17)])
    return [number_value, suit_value]


#win or lose
def check_flush(dc1, dc2, dc3, c1, c2):
    total_value = reversenumberdic[dc1[1]] + reversenumberdic[dc2[1]] + reversenumberdic[dc3[1]] + reversenumberdic[c1[1]] + reversenumberdic[c2[1]]
    if total_value.count("a") == 5:
        return "club flush"
    elif total_value.count("b") == 5:
        return "diamond flush"
    elif total_value.count("c") == 5:
        return "heart flush"
    elif total_value.count("d") == 5:
        return "spade flush"
def count_numbers(dc1, dc2, dc3, c1, c2):
    fill_a = dc1[0],dc2[0],dc3[0],c1[0],c2[0]
    fill = 0
    for i in fill_a:
        if fill_a.count(i) == 4:
            fill = fill + 2
        elif fill_a.count(i) == 3:
            fill = fill + 1
        if fill_a.count(i) == 2:
            fill = fill + 1
    match fill:
        case 8: return "4 of a kind"
        case 5: return "3 of a kind", "2 of a kind"
        case 4: return "2 of a kind", "2 of a kind"
        case 3: return "3 of a kind"
        case 2: return "2 of a kind"
def check_straight(dc1,dc2,dc3,c1,c2):
    fill_a = [reversenumberdic[dc1[0]],reversenumberdic[dc2[0]],reversenumberdic[dc3[0]],reversenumberdic[c1[0]],reversenumberdic[c2[0]]]
    fill_a.sort()
    for i in range(1,5):
        if fill_a[4] == fill_a[0]+4:
            return("straight")
        elif fill_a[i] == fill_a[i-1]+1:
            continue
        else:
            return("no straight")

def chose_call_fold():
    choce = ""
    while choce != "fold" and choce != "Fold" and choce != "call" and choce != "Call":
        choce = input("Do you Fold or Call? ")
    return choce
def score_win(dc1, dc2, dc3, c1, c2):
    total_score = 0
    flush = check_flush(dc1, dc2, dc3, c1, c2)
    count = count_numbers(dc1, dc2, dc3, c1, c2)
    straight = check_straight(dc1,dc2,dc3,c1,c2)
    if flush is not None:
        total_score = total_score + 6
    match count:
        case "4 of a kind": total_score = total_score + 8
        case "3 of a kind", "2 of a kind": total_score = total_score + 7
        case "2 of a kind", "2 of a kind": total_score = total_score + 3  
        case "3 of a kind": total_score = total_score + 4
        case "2 of a kind": total_score = total_score + 2
    if straight is not None:
        total_score = total_score + 5
    return total_score
def high_card(yc1, yc2, hc1, hc2):
    your_card = [reversenumberdic[yc1[0]],reversenumberdic[yc2[0]]]
    house_card = [reversenumberdic[hc1[0]],reversenumberdic[hc2[0]]]
    yc = sorted(your_card)
    hc = sorted(house_card)
    if yc[1]>hc[1]:
        print("You Win. It was close. Good call")
    elif yc[1]<hc[1]:
        print("You Lose. It was close. Good Luck Next Time")
    else:
        if yc1[1] == hc1[1]:
            if suitstrainth[yc1[1]] < suitstrainth[hc1[1]]:
                print("You Win. It was super close. Good call")
            else:
                print("You Lose. It was super close. Good Luck Next Time")
        elif yc2[1] == hc2[1]:
            if suitstrainth[yc2[1]] < suitstrainth[hc2[1]]:
                print("You Win. It was super close. Good call")
            else:
                print("You Lose. It was super close. Good Luck Next Time")
        elif yc1[1] == hc2[1]:
            if suitstrainth[yc1[1]] < suitstrainth[hc2[1]]:
                print("You Win. It was super close. Good call")
            else:
                print("You Lose. It was super close. Good Luck Next Time")
        else:
            if suitstrainth[yc2[1]] < suitstrainth[hc1[1]]:
                print("You Win. It was super close. Good call")
            else:
                print("You Lose. It was super close. Good Luck Next Time")
def call_fold(chose_call_fold):
    if chose_call_fold == "fold" or chose_call_fold == "Fold":
        print("You have folded, thus you lose automatically. The house had...")
        return "fold"

def call(dc1, dc2, dc3, yc1, yc2, hc1 ,hc2):
    your_score = score_win(dc1, dc2, dc3, yc1, yc2)
    house_score = score_win(dc1, dc2, dc3, hc1, hc2)
    if your_score > house_score:
        print("You Win. Good call")
    elif your_score < house_score:
        print("You Lose. Good Luck Next Time")
    elif your_score == house_score:
        high_card(yc1, yc2, hc1, hc2)



#playing game (wip - error: "folding/calling" is not completed)
def play_poker(options):
    if (options == "start") == True:
        #make cards
        card_list = []
        while len(card_list) < 7:
            a = print_card()
            if a not in card_list:
                card_list.insert(0,a)
        #card list
        dc1 = card_list[0]
        dc2 = card_list[1]
        dc3 = card_list[2]
        yc1 = card_list[3]        
        yc2 = card_list[4]
        hc1 = card_list[5]
        hc2 = card_list[6]    

        #3 base cards
        print("Starting Poker . . .")
        print(dc1)
        print(dc2)
        print(dc3)
        
        #your hand
        print("Your Hand")
        print(yc1)
        print(yc2)
       
        #you chose
        if call_fold(chose_call_fold()) is None:
            print("You call. The house had ...")
            print(hc1,hc2)
            call(dc1, dc2, dc3, yc1, yc2, hc1 ,hc2)
        else:
            print(hc1,hc2)

#start game while launch
options = "start"
while options == "start":
    play_poker(options)
    if options == "start":
        op = input("Do you want to continue? Type yes if so, else type no. ")
        match op:
            case "yes": options = "start"
            case "no": options = "stop"
