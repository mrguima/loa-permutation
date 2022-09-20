from classes.Party import create_std_party
from pandas import DataFrame
from data import guild_players


if __name__ == "__main__":

    runs = create_std_party(guild_players)

    formatted_data = [("-", ["SUP", "DPS 1", "DPS 2", "DPS 3"])]
    for index, run in enumerate(runs):
        current_players = []
        current_players.append(
            f"{run.support.name} ({run.support.main.className.name})"
            if run.support
            else ""
        )

        for dps in run.dpses:
            current_players.append(
                f"{dps.name} ({dps.main.className.name})" if dps else ""
            )

        while len(current_players) < 4:
            current_players.append("")

        formatted_data.append((f"PT_{index + 1}", current_players))

    df = DataFrame.from_dict(dict(formatted_data))
    df.to_excel("Parties.xlsx", sheet_name="Party Runs", index=False)
