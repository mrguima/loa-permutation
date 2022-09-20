import random

from typing import List
from classes.Character import ClassType
from classes.Player import Player


class PartyRun:
    support: Player
    dpses: List[Player]

    def __init__(self):
        self.support = None
        self.dpses = []


def create_std_party(players: List[Player]) -> List[PartyRun]:
    random.shuffle(players)
    supports = [
        player
        for player in players
        if player.main.className.value.classType == ClassType.SUPPORT
    ]
    dpses = [
        player
        for player in players
        if player.main.className.value.classType == ClassType.DPS
    ]
    dpses_crit = [
        player
        for player in players
        if player.main.className.value.classType == ClassType.DPS_CRIT_SYNERGY
    ]

    all_runs = []
    while (len(supports) + len(dpses) + len(dpses_crit)) > 0:
        party_run = PartyRun()

        if len(supports) > 0:
            party_run.support = supports[0]
            supports.pop(0)

        if len(dpses_crit) > 0:
            party_run.dpses.append(dpses_crit[0])
            dpses_crit.pop(0)

        classes_ended = False
        while len(party_run.dpses) < 3:
            if classes_ended:
                break
            different_class_added = False

            if len(dpses) <= 0:
                break
            classes_in_run = [player.main.className for player in party_run.dpses]

            names_in_run = [player.name for player in party_run.dpses]
            if party_run.support:
                names_in_run.append(party_run.support.name)

            for index, player in enumerate(dpses):
                if (
                    player.main.className in classes_in_run
                    or player.name in names_in_run
                ):
                    continue
                party_run.dpses.append(player)
                dpses.pop(index)
                different_class_added = True
                break

            if not different_class_added:
                classes_ended = True

        all_runs.append(party_run)

    return all_runs
