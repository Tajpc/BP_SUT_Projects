# file = open('result', 'w')
import sys
class player:
    def __init__(self, name, health, score):
        self.name = name
        self.health = health
        self.score = score

class card:
    def __init__(self, damage):
        self.damage = damage
class A(card):
    pass
class B(card):
    pass
class C(card):
    pass
class player1(player):
    pass
class player2(player):
    pass
player1.score = 0
player2.score = 0
try:
    s1, s2 = map(str, input().split())
    player1.name = s1
    player2.name = s2
except:
    # file.write('Invalid Command.')
    print('Invalid Command.')
    sys.exit(0)
try:
    h1, h2 = map(int, input().split())
    player1.health = h1
    player2.health = h2
except ValueError:
    # file.write('Invalid Command.')
    print('Invalid Command.')
    sys.exit(0)
try:
    d1, d2, d3 = map(int, input().split())
except ValueError:
    for i in range(3):
        player_card1, player_card2 = map(str, input().split())
    # file.write('Invalid Command.')
    print('Invalid Command.')
else:
    A.damage = d1
    B.damage = d2
    C.damage = d3
    for i in range(3):
        player_card1, player_card2 = map(str, input().split())
        if player_card1 == 'A':
            player_card1 = A
        elif player_card1 == 'B':
            player_card1 = B
        else:
            player_card1 = C
        if player_card2 == 'A':
            player_card2 = A
        elif player_card2 == 'B':
            player_card2 = B
        else:
            player_card2 = C
        if player_card1.damage > player_card2.damage:
            player1.score += 1
        elif player_card2.damage > player_card1.damage:
            player2.score += 1
        player1.health -= player_card2.damage
        player2.health -= player_card1.damage
    res1 = f"{player1.name} -> Score: {player1.score}, Health: {player1.health}"
    res2 = f"{player2.name} -> Score: {player2.score}, Health: {player2.health}"
    # file.write(res1)
    # file.write(res2)
    print(res1)
    print(res2)