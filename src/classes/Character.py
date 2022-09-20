from enum import Enum


class ClassType(Enum):
    DPS = 1
    DPS_CRIT_SYNERGY = 2
    SUPPORT = 3


class ClassRole:
    classType: ClassType

    def __init__(self, classType):
        self.classType = classType


class ClassName(Enum):
    BERSERKER = ClassRole(ClassType.DPS)
    DESTROYER = ClassRole(ClassType.DPS)
    GUNLANCER = ClassRole(ClassType.DPS)
    PALADIN = ClassRole(ClassType.SUPPORT)

    ARCANIST = ClassRole(ClassType.DPS_CRIT_SYNERGY)
    BARD = ClassRole(ClassType.SUPPORT)
    SORCERESS = ClassRole(ClassType.DPS)

    DEATHBLADE = ClassRole(ClassType.DPS)
    SHADOWHUNTER = ClassRole(ClassType.DPS)

    GLAIVIER = ClassRole(ClassType.DPS_CRIT_SYNERGY)
    SCRAPPER = ClassRole(ClassType.DPS)
    SOULFIST = ClassRole(ClassType.DPS)
    STRIKER = ClassRole(ClassType.DPS_CRIT_SYNERGY)
    WARDANCER = ClassRole(ClassType.DPS_CRIT_SYNERGY)

    GUNSLINGER = ClassRole(ClassType.DPS_CRIT_SYNERGY)
    ARTILLERIST = ClassRole(ClassType.DPS)
    DEADEYE = ClassRole(ClassType.DPS_CRIT_SYNERGY)
    SHARPSHOOTER = ClassRole(ClassType.DPS)


class Character:
    className: ClassName

    def __init__(self, className):
        self.className = className
