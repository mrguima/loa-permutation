from classes.Player import Player
from classes.Character import Character, ClassName
from classes.Argos import create_argos_runs
from pandas import DataFrame


if __name__ == "__main__":
    p1 = Player("Mylanbuza1", Character(ClassName.ARCANIST), 3)
    p2 = Player("Mylanbuza2", Character(ClassName.ARCANIST), 1)
    p3 = Player("Mylanbuza3", Character(ClassName.ARCANIST), 1)
    p4 = Player("Mylanbuza4", Character(ClassName.ARCANIST), 1)
    p5 = Player("Mylanbuza5", Character(ClassName.ARCANIST), 1)
    p6 = Player("Mylanbuza6", Character(ClassName.ARCANIST), 1)
    p7 = Player("Mylanbuza7", Character(ClassName.ARCANIST), 1)
    p8 = Player("Mylanbuza8", Character(ClassName.ARCANIST), 1)

    players = [
        Player("IceDragon", 1, 3),
        Player("Acqua", 1, 2),
        Player("Alysson", 1, 2),
        Player("Makise", 1, 3),
        Player("camihira", 1, 3),
        Player("Cryss", 1, 3),
        Player("André", 1, 3),
        Player("PedroW", 1, 1),
        Player("Altatrola", 1, 3),
        Player("Laykon", 1, 1),
        Player("BaBayaGa", 2, 2),
        Player("Fidu", 1, 3),
        Player("Mike", 1, 2),
    ]

    runs = create_argos_runs(players, 2, 6)

    formatted_data = [
        (
            "-",
            [
                "CARRY",
                "CARRY",
                "ALT",
                "ALT",
                "ALT",
                "ALT",
                "ALT",
                "ALT",
            ],
        )
    ]

    for index, run in enumerate(runs):
        current_players = []
        for player in run.carries:
            current_players.append(player.name)

        for player in run.alts:
            current_players.append(player.name)

        while len(current_players) < 8:
            current_players.append("")

        formatted_data.append((f"RUN_{index + 1}", current_players))

    df = DataFrame.from_dict(dict(formatted_data))
    df.to_excel("Argos.xlsx", sheet_name="Party Runs", index=False)

    # for run in argosRuns:
    #     print("----Run----")
    #     print("Mains:")
    #     for player in run.carries:
    #         print(player.name)

    #     print("Alts:")
    #     for player in run.alts:
    #         print(player.name)
