import random, time
from random import randint
from sys import exit

deck = []
player_1_cards = []
player_2_cards = []
player_3_cards = []
player_4_cards = []

player_1_name = []
player_2_name = []
player_3_name = []
player_4_name = []

########## Deck Created! --v ##########

def create_deck():
    global deck

    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["c", "d", "h", "s"]

    for v in values:
        for s in suits:
            deck.append(v)

    return deck

create_deck()


########## For shuffling and drawing cards from the deck ##########

def shuffle():
        global deck

        draw_card = random.shuffle(deck)

        return deck

def draw_random_card():
        global deck
        shuffle()

        draw = random.choice(deck)
        deck.remove(draw)

        return draw

########## Players ##########

class Player_1(object):

    def __init__(self, cards={}):
        self.cards = player_1_cards

    def deal_player_1(self):
        global player_1_cards

        while len(player_1_cards) != 5:
            add_card = draw_random_card()
            player_1_cards.append(add_card)

        self.player_1_name()

        return player_1_cards

    def player_1_name(self):
        global player_1_name
        player_1 = input("""

        What is Player 1's name?
        -----------------------> """)
        print(f"{player_1}")

        player_1_name = player_1

        return player_1_name

    def view_player_1(self):
        global player_1_cards
        global player_1_name

        print(f"""
        {player_1_name}'s cards are

                     ------------------------------------------------------------
                     {player_1_cards}
                     ------------------------------------------------------------
        """)

########## Player 2 ##########

class Player_2(object):

    def __init__(self, cards={}):
        self.cards = player_2_cards

    def deal_player_2(self):
        global player_2_cards

        while len(player_2_cards) != 5:
            add_card = draw_random_card()
            player_2_cards.append(add_card)

        self.player_2_name()

        return player_2_cards

    def player_2_name(self):
        global player_2_name
        player_2 = input("""

        What is Player 2's name?
        -----------------------> """)
        print(f"{player_2}")

        player_2_name = player_2

        return player_2_name

    def view_player_2(self):
        global player_2_cards

        print(f"""
        {player_2_name}'s cards are

                     ------------------------------------------------------------
                     {player_2_cards}
                     ------------------------------------------------------------
        """)

########## Player 3 ##########

class Player_3(object):

    def __init__(self, cards={}):
        self.cards = player_3_cards

    def deal_player_3(self):
        global player_3_cards

        while len(player_3_cards) != 5:
            add_card = draw_random_card()
            player_3_cards.append(add_card)

        self.player_3_name()

        return player_3_cards

    def player_3_name(self):
        global player_3_name
        player_3 = input("""

        What is Player 3's name?
        -----------------------> """)
        print(f"{player_3}")

        player_3_name = player_3

        return player_3_name

    def view_player_3(self):
        global player_3_cards

        print(f"""
        {player_3_name}'s cards are

                     ------------------------------------------------------------
                     {player_3_cards}
                     ------------------------------------------------------------
        """)

########## Player 4 ##########

class Player_4(object):

    def __init__(self, cards={}):
        self.cards = player_4_cards

    def deal_player_4(self):
        global player_4_cards

        while len(player_4_cards) != 5:
            add_card = draw_random_card()
            player_4_cards.append(add_card)

        self.player_4_name()

        return player_4_cards

    def player_4_name(self):
        global player_4_name
        player_4 = input("""

        What is Player 4's name?
        -----------------------> """)
        print(f"{player_4}")

        player_4_name = player_4

        return player_4_name

    def view_player_4(self):
        global player_4_cards

        print(f"""
        {player_4_name}'s cards are

                     ------------------------------------------------------------
                     {player_4_cards}
                     ------------------------------------------------------------
        """)

####### END PLAYERS #################


###### PLAYER TURN #####

def player_1_turn():
    global player_1_name

    player_1 = Player_1()

    print(f"-------------- START OF {player_1_name}'s TURN --------------")

    player = input("""Do you want to SCORE points, VIEW your cards, or ASK for a card?

    -------------------> """)

    if player == "SCORE" or player == "score":
        print("SCORE!")
    elif player == "VIEW" or player == "view":
        player_1.view_player_1()
        player_1_turn()
    elif player == "ASK" or player == "ask":
        player_1_ask()
    else:
        print("That must have been a typo, TRY AGAIN!")
        player_1_turn()

def player_2_turn():
    global player_2_name

    player_2 = Player_2()

    print(f"""

    -------------- START OF {player_2_name}'s TURN --------------

    """)

    player = input("""Do you want to SCORE points, VIEW your cards, or ASK for a card?

    -------------------> """)

    if player == "SCORE" or player == "score":
        print("SCORE!")
    elif player == "VIEW" or player == "view":
        player_2.view_player_2()
        player_2_turn()
    elif player == "ASK" or player == "ask":
        player_2_ask()
    else:
        print("That must have been a typo, TRY AGAIN!")
        player_2_turn()

def player_3_turn():
    global player_3_name

    player_3 = Player_3()

    print(f"-------------- END OF {player_3_name}'s TURN --------------")

    player = input("""Do you want to SCORE points, VIEW your cards, or ASK for a card?

    -------------------> """)

    if player == "SCORE" or player == "score":
        print("SCORE!")
    elif player == "VIEW" or player == "view":
        player_3.view_player_3()
        player_3_turn()
    elif player == "ASK" or player == "ask":
        player_3_ask()
    else:
        print("That must have been a typo, TRY AGAIN!")
        player_3_turn()

def player_4_turn():
    global player_4_name

    player_4 = Player_4()

    print(f"-------------- END OF {player_4_name}'s TURN --------------")

    player = input("""Do you want to SCORE points, VIEW your cards, or ASK for a card?

    -------------------> """)

    if player == "SCORE" or player == "score":
        print("SCORE!")
    elif player == "VIEW" or player == "view":
        player_4.view_player_4()
        player_4_turn()
    elif player == "ASK" or player == "ask":
        player_4_ask()
    else:
        print("That must have been a typo, TRY AGAIN!")
        player_4_turn()

##### PLAYER ASKSSSSSSSSSS #####
def player_1_ask():
    global player_1_cards
    global player_2_cards
    global player_3_cards
    global player_4_cards

    global player_1_name
    global player_2_name
    global player_3_name
    global player_4_name

    player_1 = Player_1()
    player_2 = Player_2()
    player_3 = Player_3()
    player_4 = Player_4()

    ask = input(f"""What player?

    {player_2_name}
    {player_3_name}
    {player_4_name}

    -------------------> """)

# If player 1 is asking player 2

    if ask == player_2_name:
        player_1.view_player_1()
        player_2.view_player_2()

        card = input("""

        What card?
        -------------------> """)

        if card in player_1_cards:
            print("YES!!")
            if f"{card}" in player_2_cards:
                print("YESSSS!!")
                take = player_2_cards.pop(player_2_cards.index(card))
                player_1_cards.append(take)
                print(f"""

                {player_1_name}'s cards are: {player_1_cards}

                {player_2_name}'s cards are: {player_2_cards}

                """)
            else:
                add_card = draw_random_card()
                player_1_cards.append(add_card)
                print(f"-------------- END OF {player_1_name}'s TURN --------------")
                player_2_turn()
        else:
            ask_again = input("""You HAVE to pick a card from your hand. You can VIEW your cards or press ENTER to ask againself.

            -------------------> """)

            if ask_again == "VIEW" or ask_again == "view":
                view_player_1()
                player_1_ask()

            else:
                player_1_ask()

# If player 1 is asking player 3

    elif ask == player_3_name:
        player_1.view_player_1()
        player_3.view_player_3()

        card = input("""

        What card?
        -------------------> """)

        if card in player_1_cards:
            print("YES!!")
            if f"{card}" in player_3_cards:
                print("YESSSS!!")
                take = player_3_cards.pop(player_3_cards.index(card))
                player_1_cards.append(take)
                print(f"""

                {player_1_name}'s cards are: {player_1_cards}

                {player_2_name}'s cards are: {player_2_cards}

                """)
            else:
                add_card = draw_random_card()
                player_1_cards.append(add_card)
                print(f"-------------- END OF {player_1_name}'s TURN --------------")
                player_2_turn()
        else:
            ask_again = input("""You HAVE to pick a card from your hand. You can VIEW your cards or press ENTER to ask againself.

            -------------------> """)

            if ask_again == "VIEW" or ask_again == "view":
                view_player_1()
                player_1_ask()

            else:
                player_1_ask()

# If player 1 is asking player 4

    elif ask == player_4_name:
        player_1.view_player_1()
        player_4.view_player_4()

        card = input("""

        What card?
        -------------------> """)

        if card in player_1_cards:
            print("YES!!")
            if f"{card}" in player_4_cards:
                print("YESSSS!!")
                take = player_4_cards.pop(player_4_cards.index(card))
                player_1_cards.append(take)
                print(f"""

                {player_1_name}'s cards are: {player_1_cards}

                {player_2_name}'s cards are: {player_2_cards}

                """)
            else:
                add_card = draw_random_card()
                player_1_cards.append(add_card)
                print(f"-------------- END OF {player_1_name}'s TURN --------------")
                player_2_turn()
        else:
            ask_again = input("""You HAVE to pick a card from your hand. You can VIEW your cards or press ENTER to ask againself.

            -------------------> """)

            if ask_again == "VIEW" or ask_again == "view":
                view_player_1()
                player_1_ask()

            else:
                player_1_ask()
    else:
        print("You must type in their name correctly!")
        player_1_ask()

########## END PLAYER 1 ASK ##########
########## PLAYER 2 ASK ##########

def player_2_ask():
    global player_1_cards
    global player_2_cards
    global player_3_cards
    global player_4_cards

    global player_1_name
    global player_2_name
    global player_3_name
    global player_4_name

    player_1 = Player_1()
    player_2 = Player_2()
    player_3 = Player_3()
    player_4 = Player_4()

    ask = input(f"""What player?

    {player_1_name}
    {player_3_name}
    {player_4_name}

    -------------------> """)

# If player 2 is asking player 1

    if ask == player_1_name:
        player_2.view_player_2()
        player_1.view_player_1()

        card = input("""

        What card?
        -------------------> """)

        if card in player_2_cards:
            print("YES!!")
            if f"{card}" in player_1_cards:
                print("YESSSS!!")
                take = player_1_cards.pop(player_1_cards.index(card))
                player_2_cards.append(take)
                print(f"""

                {player_1_name}'s cards are: {player_1_cards}

                {player_2_name}'s cards are: {player_2_cards}

                """)
            else:
                add_card = draw_random_card()
                player_2_cards.append(add_card)
                print(f"""

                -------------- END OF {player_2_name}'s TURN --------------

                """)
                player_3_turn()
        else:
            ask_again = input("""You HAVE to pick a card from your hand. You can VIEW your cards or press ENTER to ask againself.

            -------------------> """)

            if ask_again == "VIEW" or ask_again == "view":
                view_player_2()
                player_2_ask()

            else:
                player_2_ask()

# If player 2 is asking player 3

    if ask == player_3_name:
        player_2.view_player_2()
        player_3.view_player_3()

        card = input("""

        What card?
        -------------------> """)

        if card in player_2_cards:
            print("YES!!")
            if f"{card}" in player_3_cards:
                print("YESSSS!!")
                take = player_3_cards.pop(player_3_cards.index(card))
                player_2_cards.append(take)
                print(f"""

                {player_1_name}'s cards are: {player_1_cards}

                {player_2_name}'s cards are: {player_2_cards}

                """)
            else:
                add_card = draw_random_card()
                player_2_cards.append(add_card)
                print(f"""

                -------------- END OF {player_2_name}'s TURN --------------

                """)
                player_3_turn()
        else:
            ask_again = input("""You HAVE to pick a card from your hand. You can VIEW your cards or press ENTER to ask againself.

            -------------------> """)

            if ask_again == "VIEW" or ask_again == "view":
                view_player_2()
                player_2_ask()

            else:
                player_2_ask()

# If player 2 is asking player 4

    if ask == player_4_name:
        player_2.view_player_2()
        player_4.view_player_4()

        card = input("""

        What card?
        -------------------> """)

        if card in player_2_cards:
            print("YES!!")
            if f"{card}" in player_4_cards:
                print("YESSSS!!")
                take = player_4_cards.pop(player_4_cards.index(card))
                player_2_cards.append(take)
                print(f"""

                {player_1_name}'s cards are: {player_1_cards}

                {player_2_name}'s cards are: {player_2_cards}

                """)
            else:
                add_card = draw_random_card()
                player_2_cards.append(add_card)
                print(f"""

                -------------- END OF {player_2_name}'s TURN --------------

                """)
                player_3_turn()
        else:
            ask_again = input("""You HAVE to pick a card from your hand. You can VIEW your cards or press ENTER to ask againself.

            -------------------> """)

            if ask_again == "VIEW" or ask_again == "view":
                view_player_2()
                player_2_ask()

            else:
                player_2_ask()

###### END PLAYER 2 ASK ######
def number_of_players():
    player_count = input("""
    Welcome to HELLLLLLLLL, as in HELL I mean water. We're playing GO FISH!!!

    How many human players are FISHING (and yes...computers can fish)?

    1: 1 human, 3 computers
    2: 2 humans, 2 computers
    3: 3 humans, 1 computer
    4: 4 humans
    5: Don't be a dipshit

    -----------------------> """)
    if player_count == "4":
        var_player_1 = Player_1()
        var_player_1.deal_player_1()

        var_player_2 = Player_2()
        var_player_2.deal_player_2()

        var_player_3 = Player_3()
        var_player_3.deal_player_3()

        var_player_4 = Player_4()
        var_player_4.deal_player_4()


    else:
        print("I told you NOT to be a dipshit, now you ruined the game.")
        exit(1)

    #return player_1_name, player_2_name, player_3_name, player_4_name

def random_start():

    choice = f"{randint(1,2)}"
    print(f"It will be Player {choice}'s turn")

    if choice == "1":
        player_1_turn()
    elif choice == "2":
        player_2_turn()
    else:
        print("Something is wrong with your random start!")

number_of_players()
random_start()
print(len(deck))


########### If you want to add a computer ##########

#    def deal_computer():
#        cCard_1 = computer_cards.append.DrawCard
#        cCard_2 = computer_cards.append.DrawCard
#        cCard_3 = computer_cards.append.DrawCard
#        cCard_4 = computer_cards.append.DrawCard
#        cCard_5 = computer_cards.append.DrawCard

#        print(f"""

#        return computer_cards

#    def deal_input():
#        dealing = input("""Press ENTER to deal the cards, press 'q' to QUIT

#        ------------------->

#        """)

    #    if dealing == 'q':
    #        exit(0)
#        elif dealing == 'r':
#            print("""
#            The rules of the game are simple.
#            """)
#        else:
#            deal_player()
#            deal_computer()
#            player_turn()

##################################
