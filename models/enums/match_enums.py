from enum import Enum


class MatchGenderEnum(str, Enum):
    male = "male"
    female = "female"


class MatchTypeEnum(str, Enum):
    odi = "ODI"  # One Day International


class MatchVictoryMethodEnum(str, Enum):
    innings = "innings"
    runs = "runs"
    wickets = "wickets"


class MatchTeamTypes(str, Enum):
    international = "international"
    club = "club"


class MatchOutcomeEnum(str, Enum):
    winner = "winner"
    draw = "draw"
    tie = "tie"
    no_result = "no result"
