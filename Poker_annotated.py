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
    "spade"   : "d"
    }
suitstrainth = {
    "club"    : 1,
    "diamond" : 2,
    "heart"   : 3,
    "spade"   : 4
}

#print_card(wip - error: has duplicates)
def print_card():
    number_value = (numberdic[random.randint(1,13)])
    suit_value = (numberdic[random.randint(14,17)])
    return [number_value, suit_value]


#house hand
def house_hand():
    hc1 = print_card()
    hc2 = print_card()
    print (hc1)
    print (hc2)


#win or lose (wip - missing: strights)
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
        case 5: return "2 of a kind", "2 of a kind"
        case 3: return "3 of a kind"
        case 2: return "2 of a kind"


#folding/calling (wip - missing: no winning or losing)
def chose_call_fold():
    choce = ""
    while choce != "fold" and choce != "Fold" and choce != "call" and choce != "Call":
        choce = input("Do you Fold or Call? ")
    return choce
def call_fold(chose_call_fold):
    if chose_call_fold == "fold" or chose_call_fold == "Fold":
        print("You have folded, thus you lose automatically. The house had...")
        return(house_hand())
    else:
        print("You call. The house had ...")
        return(house_hand())

    
#playing game (wip - error: "folding/calling" is not completed)
def play_poker(options):
    if (options == "start") == True:
        
        #3 base cards
        print("Starting Poker . . .")
        dc1 = print_card()
        dc2 = print_card()
        dc3 = print_card()
        print(dc1)
        print(dc2)
        print(dc3)
        
        #your hand
        print("Your Hand")
        yc1 = print_card()
        yc2 = print_card()
        print(yc1)
        print(yc2)
       
        #you chose
        chose_call_fold()
        
        #see if you win
        call_fold(chose_call_fold)
    else:
        print("game is over")

#start game while launch
options = "start"
while options == "start":
    play_poker(options)
    if options == "start":
        op = input("Do you want to continue? Type yes if so, else type no. ")
        match op:
            case "yes": options = "start"
            case "no": options = "stop"
