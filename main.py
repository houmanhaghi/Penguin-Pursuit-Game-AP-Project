import os
import sys
from pages.login import login
from pages.start_menu import start_menu
from pages.one_player_game import one_player_game
from pages.two_player_game import two_player_game
from pages.score_table import score_table



def main():
    player_information = login()
    player_command = start_menu()

    if player_command == 'one_player_game':
        one_player_game()
    elif player_command == 'two_player_game':
        two_player_game()
    elif player_command == 'score_table':
        score_table()


if __name__ == '__main__':
    main()