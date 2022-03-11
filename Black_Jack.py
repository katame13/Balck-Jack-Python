import sys
import random

def random_card():
    card = random.randint(1, 13)
    return card

def show_card(this_card):
    if this_card == 10:
        return "J"
    elif this_card == 11:
        return "Q"
    elif this_card == 12:
        return "K"
    elif this_card == 1 or 13:
        return "A"
    else:
        return (this_card)

def build_deck(suits, cards_in_suit):
    deck = []
    for suit in suits:
        for number in range (1, cards_in_suit):
            card = {"number" : number, "suit" : suit }
            deck.append (card)
    return deck

def shuffle (deck, y):
    left_deck = []
    right_deck = []
    for x in range (y):
        while deck:
            z=random.randint(1,2)
            if z == 1:
                right_deck.append (deck.pop())
            elif z == 2:
                left_deck.append (deck.pop())

        while left_deck or right_deck:
            z=random.randint(1,2)
            if z == 1 and left_deck:
                deck.append (left_deck.pop())
            elif z == 2 and right_deck:
                deck.append (right_deck.pop())

def get_and_print_sum (hand):
    total = 0
    for n in range (len(hand)):
        total = total+(hand [n]["number"])
    print("Adding to: " + str(total))
    return total

def check_sum(sum, my_hand, npc_hand, my_deck, suit):
    if sum  == 21:
        print ("Congragulations! You got Black Jack!")
        end_game(my_hand, npc_hand, suit)
        return "no"
    elif sum  > 21:
        print("Sorry, you busted.")
        end_game(my_hand, npc_hand, suit)
        return "no"
    elif sum  < 21:
        print("Would you like to draw another card?")
        draw_new = input().lower()
        if draw_new == "yes" or draw_new == "y":
            draw_again (sum, my_hand,npc_hand, my_deck, suit, draw_new)
        if draw_new =='no' or draw_new == "n":
            winner(npc_hand, my_hand, suit)
            end_game(my_hand, npc_hand, suit)
        return draw_new

def draw_again(total, my_hand, npc_hand, my_deck, suit, draw_new):
        while draw_new == "yes" or draw_new == "y":
            draw_hand(my_deck, my_hand, 1)
            print(my_hand)
            total=get_and_print_sum(my_hand)
            draw_new=check_sum(total, my_hand, npc_hand, my_deck, suit)

def get_sum_no_print(hand):
    total = 0
    for n in range (len(hand)):
        total = total+(hand [n]["number"])
    return total

def npc_draw (total, deck, hand,):
        while total <= 14:
            draw_hand (deck, hand, 1)
            total=get_sum_no_print(hand)

def winner (npc_hand, my_hand, suit):
    npc_total = get_sum_no_print(npc_hand)
    my_total = get_sum_no_print(my_hand)
    if npc_total > my_total and npc_total <= 21:
        print("Sorry, you lost.")
        end_game(my_hand, npc_hand, suit)
    elif npc_total < my_total and my_total <= 21:
        print("Congragulations! You won!")
        end_game(my_hand, npc_hand, suit)
    elif npc_total > 21 and my_total <= 21:
        print ("Congragulations! You won!")
        end_game(my_hand, npc_hand, suit)

def draw_hand (deck, hand, hand_size):
    for size in range (hand_size):
        hand.append (deck.pop (0))

def intro ():
    print("Hello! What is your name?")
    myName=input()
    print("Nice to meet you, "+myName+". Lets play black jack!")

def run_game(c_suit):
    my_deck = build_deck(c_suit, 13)
    my_hand = []
    npc_hand = []
    shuffle(my_deck, 60)
    draw_hand(my_deck, my_hand, 2)
    draw_hand(my_deck, npc_hand, 2)
    print (my_hand)
    print(npc_hand[0])
    get_and_print_sum(my_hand)
    npc_total=get_sum_no_print(npc_hand)
    npc_draw(npc_total, my_deck, npc_hand)
    npc_total=get_sum_no_print(npc_hand)
    my_sum = get_sum_no_print(my_hand)
    check_sum(my_sum, my_hand, npc_hand, my_deck, c_suit)
    winner(npc_hand, my_hand, c_suit)
    print(my_hand)
    print(my_sum)
    print(npc_hand)
    print (npc_total)

def end_game(my_hand, npc_hand, suit):
    print_results(my_hand, npc_hand)
    print("Would you like to play again?")
    cont=input().lower()
    if cont == "yes" or cont =="y":
        run_game(suit)
    else:
        quit()

def print_results (my_hand, npc_hand):
    print(my_hand)
    get_and_print_sum(my_hand)
    print(npc_hand)
    get_and_print_sum (npc_hand)


run_game(["Diamond", "Spade", "Heart", "Club"])
