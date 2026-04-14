from itertools import product
from numpy import random

"""The game is more or less complete. The only thing is that cards get chosen randomly from the deck each room. Therefore
cards from when you fled a room get shoveled into the deck randomly"""


#creating the deck
black_suits = ['♣', '♠']
red_suits = ['♥', '♦']
ranks_black = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
ranks_red = ['2','3','4','5','6','7','8','9','10']

deck = []
deck.extend(list(product(ranks_black, black_suits)))
deck.extend(list(product(ranks_red, red_suits)))

"I actually need to create a shoveled and ordered deck, since the order matters"
"because you can flee a room, and those cards need to be at the end"

# create an empty discard staple
discard = []

#create an empty weapon slot
weapon = []
weapon_cap = float('inf')

# Setting ranks to values and suits to classes
dict_rank_to_value = {'2':2, '3':3, '4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}


"""the following mechanic will actually not work, I need to take the first 4 cards"""

def form_room():
    global deck, room
    #create a random number in length of deck -1 to account for list index starting at 0
    room = []
    for i in range(4):
        rndm_nr = random.randint(len(deck)-1)
        room.append(deck.pop(rndm_nr))
    print()
    print ('your cards are:')
    print(room)

def choose_card():
    global discard, room, played_card
    #check for correct input
    choice = None
    while choice is None:
        try:
            #only set choice to number if correct number is entered
            
            choice = int(input("Choose a card (enter number): "))
            if choice not in range(1,len(room)+1):
                print("Invalid choice, try again.")
                choice = None
        except ValueError:
            print(f"Please enter a number from 1 - {len(room)}.")
    played_card = room[choice - 1]
    discard.append(room.pop(choice - 1))
    print()
    print(f'You played the card {played_card}')
    

""" Weapons needs to be added """
def card_effect():
    global health, weapon, weapon_cap
    if played_card[1] in black_suits:
        #if you have a weapon and the weapon cap is at least the rank of the card
        if len(weapon) > 0 and weapon_cap >= dict_rank_to_value.get(played_card[0]):
            #player must choose to use weapon or not
            choice = None
            while choice is None:
                try:
                    #only set choice to answer if correct letter is entered
                    choice = input("Do you want to use your weapon (y/n): ")
                    if choice not in ('y','n'):
                        print("Invalid choice, try again.")
                        choice = None
                except ValueError:
                    print(f"Please answer with y or n (yes/no)")
            #if player chooses to use weapon: subtract weapon strength from hit
            if choice == 'y':
                blocked_hit = dict_rank_to_value.get(played_card[0]) - dict_rank_to_value.get(weapon[0])
                #cant gain health from hits, min cap at 0
                if blocked_hit < 0:
                    blocked_hit = 0
                health = health - blocked_hit
                weapon_cap = dict_rank_to_value.get(played_card[0]) - 1
            #otherwise subtract full hit from health
            else:
                health = health - dict_rank_to_value.get(played_card[0])
        #if you dont have a weapon
        else:
            health = health - dict_rank_to_value.get(played_card[0])
        if health > 0:
            print(f'Your new health: {health}')
        else:
            loose()
    elif played_card[1] == '♥':
        health = health + dict_rank_to_value.get(played_card[0])
        #max health cap at 20
        if health > 20:
            health = 20
        print(f'Your new health: {health}')
    elif played_card[1] == '♦':
        weapon = played_card
        weapon_cap = float('inf')

def refill_room():
    global deck, room
    #1 Karte bleibt immer übrig
    if len(deck) == 1:
        room.append(deck.pop(0))
        win()
    else:  
        #create a random number in length of deck -1 to account for list index starting at 0
        for i in range(3):
            rndm_nr = random.randint(len(deck)-1)
            room.append(deck.pop(rndm_nr))
        print()
        print ('your new room is:')
        print(room)
        print()
        print(f'cards in deck:{len(deck)}')

def win():
    print ('Congrats, you won!!!')
    print(f'remaining cards: {room}')
    exit()

def loose():
    print('You lost all your health, try again!')
    exit()

def flee_or_play():
    choice = None
    while choice is None:
        try:
            #only set choice to answer if correct letter is entered
            choice = input("Do you want to play or flee (p/f): ")
            if choice not in ('p','f'):
                print("Invalid choice, try again.")
                choice = None
        except ValueError:
            print(f"Please answer with p or f (play/flee)")
    if choice == 'p':
        pass
    else:
        while room:
            deck.append(room.pop())

#starting the game
print("starting game")
health = 20
print(f'health = {health}')
form_room()
#playing the game
#mail loop runs forever 
#winning / loosing conditions defined in other functions
while True:
    flee_or_play()
    if len(room) == 0:
        form_room()
    else:
        pass
    while len(room) > 1:
        choose_card()
        card_effect()
        print()
        print(f'your healt: {health}')
        print(f'cards still in room: {room}')
        print(f'your weapon: {weapon}')
        print(f'your weapon cap:{weapon_cap}')
        
        
    refill_room()
