from classes.Character import Character, ClassName
from classes.Player import Player


guild_players = [
    # Paladin
    Player("Akas", Character(ClassName.PALADIN)),
    Player("Wuffbr", Character(ClassName.PALADIN)),
    Player("MeK", Character(ClassName.PALADIN)),
    # Bards
    Player("Czarmanski", Character(ClassName.BARD)),
    Player("Koffinha", Character(ClassName.BARD)),
    Player("Dotto", Character(ClassName.BARD)),
    Player("Fidu", Character(ClassName.BARD)),
    Player("Victor", Character(ClassName.BARD)),
    Player("Sasaho", Character(ClassName.BARD)),
    Player("Camihira", Character(ClassName.BARD)),
    # Deathblades
    Player("Predd", Character(ClassName.DEATHBLADE)),
    Player("Frnnn", Character(ClassName.DEATHBLADE)),
    Player("Daslayer", Character(ClassName.DEATHBLADE)),
    Player("Deizanos", Character(ClassName.DEATHBLADE)),
    Player("Icedragon", Character(ClassName.DEATHBLADE)),
    Player("Thaty", Character(ClassName.DEATHBLADE)),
    # SORCS
    Player("Ricota", Character(ClassName.SORCERESS)),
    Player("Angelsmith", Character(ClassName.SORCERESS)),
    Player("TheBlackii", Character(ClassName.SORCERESS)),
    Player("Camihira", Character(ClassName.SORCERESS)),
    Player("Saints", Character(ClassName.SORCERESS)),
    Player("Altatrola", Character(ClassName.SORCERESS)),
    # Gunlancer
    Player("Jankera", Character(ClassName.GUNLANCER)),
    Player("Mylambuza", Character(ClassName.GUNLANCER)),
    Player("Cyrkite", Character(ClassName.GUNLANCER)),
    Player("BKN", Character(ClassName.GUNLANCER)),
    # Soufist
    Player("Huanji", Character(ClassName.SOULFIST)),
    Player("Galfiana", Character(ClassName.SOULFIST)),
    # Wardancer
    Player("Laykon", Character(ClassName.WARDANCER)),
    Player("Myrtris", Character(ClassName.WARDANCER)),
    # Arti
    Player("Kotokorj", Character(ClassName.ARTILLERIST)),
    Player("Wuffbr", Character(ClassName.ARTILLERIST)),
    # Gunslinger
    Player("Lazas", Character(ClassName.GUNSLINGER)),
    Player("MeK", Character(ClassName.GUNSLINGER)),
    # Glaivier
    Player("Zolfric", Character(ClassName.GLAIVIER)),
    Player("Mytichunter", Character(ClassName.GLAIVIER)),
    Player("Neimi", Character(ClassName.GLAIVIER)),
    Player("Valorosa", Character(ClassName.GLAIVIER)),
    # Scrapper
    Player("Neimi", Character(ClassName.SCRAPPER)),
    Player("Sasaho", Character(ClassName.SCRAPPER)),
    Player("Babayaga", Character(ClassName.SCRAPPER)),
    # SH
    Player("Makise", Character(ClassName.SHADOWHUNTER)),
    # Zerk
    Player("Sisty", Character(ClassName.BERSERKER)),
    # Striker
    Player("Amestriano", Character(ClassName.STRIKER)),
    Player("Chicobandido", Character(ClassName.STRIKER)),
    # Arca
    Player("Aqua", Character(ClassName.ARCANIST)),
    # Deadeye
    Player("Vert", Character(ClassName.DEADEYE)),
    # Destroyer
    Player("Babayaga", Character(ClassName.DESTROYER)),
]

test_data = [
    Player("Teste SUP 1", Character(ClassName.BARD)),
    Player("Teste SUP 2", Character(ClassName.BARD)),
    Player("Teste SUP 3", Character(ClassName.BARD)),
    Player("Teste SUP 4", Character(ClassName.BARD)),
    Player("Teste SUP 5", Character(ClassName.BARD)),
    Player("Teste SUP 6", Character(ClassName.BARD)),
    Player("Teste SUP 7", Character(ClassName.BARD)),
    Player("Teste SUP 8", Character(ClassName.BARD)),
    Player("Teste DPS 1", Character(ClassName.SORCERESS)),
    Player("Teste DPS 2", Character(ClassName.DESTROYER)),
    Player("Teste DPS 3", Character(ClassName.GUNLANCER)),
    Player("Teste DPS 4", Character(ClassName.SORCERESS)),
    Player("Teste DPS 5", Character(ClassName.DEATHBLADE)),
    Player("Teste DPS 6", Character(ClassName.SHADOWHUNTER)),
    Player("Teste DPS 7", Character(ClassName.SCRAPPER)),
    Player("Teste DPS 8", Character(ClassName.SOULFIST)),
    Player("Teste DPS CRIT 1", Character(ClassName.ARCANIST)),
    Player("Teste DPS CRIT 2", Character(ClassName.GLAIVIER)),
    Player("Teste DPS CRIT 3", Character(ClassName.STRIKER)),
    Player("Teste DPS CRIT 4", Character(ClassName.WARDANCER)),
    Player("Teste DPS CRIT 5", Character(ClassName.GUNSLINGER)),
    Player("Teste DPS CRIT 6", Character(ClassName.DEADEYE)),
    Player("Teste DPS CRIT 7", Character(ClassName.GUNSLINGER)),
    Player("Teste DPS CRIT 8", Character(ClassName.DEADEYE)),
]
