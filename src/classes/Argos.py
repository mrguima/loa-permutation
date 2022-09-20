import random

from typing import List
from classes.Player import Player


class ArgosRun:
    alts: List[Player]
    carries: List[Player]

    def __init__(self):
        self.alts = []
        self.carries = []


def create_argos_runs(
    players: List[Player], max_carries: int, max_carried: int
) -> List[ArgosRun]:
    all_argos_runs = []

    random.shuffle(players)

    while len(players) > 0:
        argos_run = ArgosRun()

        players_with_mains = [player for player in players if player.main]

        while len(argos_run.carries) < max_carries:
            if len(players_with_mains) > 0:
                argos_run.carries.append(players_with_mains[0])
                players_with_mains[0].main = None
                players_with_mains.pop(0)
            else:
                break

        argos_carries = [player.name for player in argos_run.carries]

        players_with_alts = [
            player
            for player in players
            if player.alt > 0 and player.name not in argos_carries
        ]

        while len(argos_run.alts) < max_carried:
            if len(players_with_alts) > 0:
                argos_run.alts.append(players_with_alts[0])
                players_with_alts[0].alt = players_with_alts[0].alt - 1
                players_with_alts.pop(0)
            else:
                break

        all_argos_runs.append(argos_run)
        players_with_characters = [
            player for player in players if player.alt > 0 or player.main
        ]
        players = players_with_characters

    return all_argos_runs
