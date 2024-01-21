import sys

class Player:
    def __init__(self, name, health, score):
        self.name = name
        self.health = health
        self.score = score

class Card:
    def __init__(self, damage):
        self.damage = damage

class A(Card):
    pass

class B(Card):
    pass

class C(Card):
    pass

def initialize_players():
    try:
        s1, s2 = map(str, input().split())
        player1 = Player(s1, 0, 0)
        player2 = Player(s2, 0, 0)
        return player1, player2
    except ValueError:
        print('Invalid Command.')
        sys.exit(1)

def initialize_health():
    try:
        h1, h2 = map(int, input().split())
        return h1, h2
    except ValueError:
        print('Invalid Command.')
        sys.exit(1)

def initialize_cards():
    try:
        d1, d2, d3 = map(int, input().split())
        A.damage = d1
        B.damage = d2
        C.damage = d3
        return A, B, C
    except ValueError:
        print('Invalid Command.')
        sys.exit(1)

def play_round(player1, player2, card1, card2):
    if card1.damage > card2.damage:
        player1.score += 1
    elif card2.damage > card1.damage:
        player2.score += 1
    player1.health -= card2.damage
    player2.health -= card1.damage

def main():
    player1, player2 = initialize_players()
    h1, h2 = initialize_health()
    A, B, C = initialize_cards()

    for _ in range(3):
        player_card1, player_card2 = map(str, input().split())
        if player_card1 == 'A':
            card1 = A
        elif player_card1 == 'B':
            card1 = B
        else:
            card1 = C
        if player_card2 == 'A':
            card2 = A
        elif player_card2 == 'B':
            card2 = B
        else:
            card2 = C
        play_round(player1, player2, card1, card2)

    print(f"{player1.name} -> Score: {player1.score}, Health: {player1.health}")
    print(f"{player2.name} -> Score: {player2.score}, Health: {player2.health}")

if __name__ == "__main__":
    main()
# 1. **Use Functions:** Consider breaking down your code into functions to encapsulate specific functionalities.

# 2. **Avoid Global Variables:** Instead of using global variables for `player1` and `player2`, pass them as arguments to functions or create them within the functions.

# 3. **Handle Invalid Input Gracefully:** Add more informative messages when input validation fails.

# 4. **Use Descriptive Variable Names:** Choose more descriptive variable names to improve code readability.

# These changes make the code more modular, readable, and handle invalid input more gracefully.