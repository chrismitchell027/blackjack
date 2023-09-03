from Cards import *

# OBJECTS AND VARIABLES
# create deck and shuffle it
deck = Deck()
deck.shuffle()

# create player and dealer hands
player_hand = Hand()
dealer_hand = Hand()


# FUNCTIONS
# returns score as int given Hand() instance
def get_hand_score(hand):
    score = 0
    aces = 0
    for card in hand.cards:
        if card.rank == "Jack":
            score += 11
        elif card.rank == "Queen":
            score += 12
        elif card.rank == "King":
            score += 13
        elif card.rank == "Ace":
            score += 1
            aces += 1
        else:
            score += int(card.rank)
    
    # check if aces should be counted as 1 or 11 points
    while aces > 0 and score > 21:
        score -= 10
        aces -= 1
    
    return score

# prints the player's cards
def print_player_hand():
    score = get_hand_score(player_hand)
    
    print(f"Your hand [{score}]:\n{player_hand}\n")

# prints the dealer's cards
def print_dealer_hand(only_one = False):
    if only_one:
        print("Dealer's hand [?]:")
        print(f"-> {dealer_hand.cards[-1]}")
        if len(dealer_hand.cards) > 1:
            for x in range(len(dealer_hand.cards) - 1):
                print('-> ????????\n')
    else:
        score = get_hand_score(dealer_hand)
        print(f"Dealer's hand [{score}]:")
        print(dealer_hand)
        print()

# returns player input regarding hitting/standing as a string
def get_player_action():
    return input("Hit or Stand? (hit/stand)\n").lower()

# resets the cards
def reset_game():
    deck.reset()
    deck.shuffle()
    player_hand.reset()
    dealer_hand.reset()

# checks if player wants to play again
def end_game():
    choice = input("Play again? (yes/no)\n").lower()
    if choice == 'yes':
        print()
        for x in range(15):
            print("-",end='')
        print()

        reset_game()
        game_loop()

# main game loop
def game_loop():

    # deal initial cards
    player_hand.draw(deck.deal())
    dealer_hand.draw(deck.deal())
    player_hand.draw(deck.deal())
    dealer_hand.draw(deck.deal())

    # print initial player cards and one dealer card
    print_player_hand()
    print_dealer_hand(True) # True makes it print only 1

    # player's turn
    while True:
        player_action = get_player_action()
        print()
        if player_action == 'hit':
            for x in range(15):
                print('-',end='')
            print()

            player_hand.draw(deck.deal())
            print_player_hand()
            print_dealer_hand(only_one=True)


        if player_action == 'stand':
            break

        # check for bust
        if get_hand_score(player_hand) > 21:
            print("Bust!\nYou lost!")
            end_game()
            break
    
    # dealer's turn (draws until score >= 17)
    print_dealer_hand()
    while get_hand_score(dealer_hand) < 17:
        dealer_hand.draw(deck.deal())
        print_dealer_hand()

    # determine winner
    dealer_score = get_hand_score(dealer_hand)
    player_score = get_hand_score(player_hand)

    if dealer_score > 21: # check for dealer bust
        print("Dealer Bust!\nYou win!")

    elif dealer_score == player_score: # check for push (draw)
        print("Push.")
        
    elif dealer_score < player_score: # check if player won
        print("You win!")
    
    else: # dealer won
        print("Dealer won!\nYou lost!")

    print(f"Your score: {player_score}\nDealer score: {dealer_score}\n")

    end_game()

# start game
game_loop()