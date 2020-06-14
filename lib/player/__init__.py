from lib.player.base_player import BasePlayer
from lib.player.player1 import Player1
from lib.player.player2 import Player2

PLAYERS = [
    Player1,
    Player2
]
def get(index):
    return PLAYERS[index - 1]