from argparse import ArgumentParser, Namespace

from .factories import bingo_card_factory
from .models.player import Player
from .visualizers import bingo_card_visualizer

def _init_argparser() -> ArgumentParser:
    """
    Initialize the argument parser
    """
    ap = ArgumentParser()
    ap.add_argument('nr_players', help='Provide the number of players as a positive integer', type=int)
    return ap

def main(arguments: Namespace) -> int:
    """
    Main entry point of bingo
    """
    players = [
        Player(bingo_card_factory.create_standard_bingo_card())
        for _ in range(arguments.nr_players)
    ]
    bcv = bingo_card_visualizer.BingoCardASCIIVisualzier()
    bcv.visualize_multiple(*(player.bingo_card for player in players))
    return 0

if __name__ == "__main__":
    import sys
    ap = _init_argparser()
    sys.exit(main(ap.parse_args(sys.argv[1:])))
