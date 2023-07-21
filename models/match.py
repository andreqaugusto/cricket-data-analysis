from datetime import datetime

from sqlalchemy import Column, Date, Enum, Integer, String

from database import Base
from models.enums import (
    MatchGenderEnum,
    MatchOutcomeEnum,
    MatchTeamTypes,
    MatchTypeEnum,
    MatchVictoryMethodEnum,
)


# following https://cricsheet.org/format/json/#the-info-section
class Match(Base):
    __tablename__ = "matches"

    match_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    file_name = Column(String, nullable=True)
    season = Column(String)
    city = Column(String, nullable=True)
    venue = Column(String, nullable=True)
    date_started = Column(Date)
    event_name = Column(String, nullable=True)
    match_gender = Column(Enum(MatchGenderEnum))
    match_type = Column(Enum(MatchTypeEnum))
    match_result = Column(Enum(MatchOutcomeEnum))
    winner = Column(String, nullable=True)
    winner_by = Column(Enum(MatchVictoryMethodEnum), nullable=True)
    winner_margin = Column(Integer, nullable=True)
    winner_method = Column(String, nullable=True)
    number_of_overs = Column(Integer)
    number_of_balls_per_over = Column(Integer)
    match_team_1 = Column(String)
    match_team_2 = Column(String)
    team_type = Column(Enum(MatchTeamTypes))

    @classmethod
    def parse_from_data(cls, match_info: dict, file_name: str) -> "Match":
        """Creates a new Match object from a dictionary of match info"""

        # treating the outcomes
        outcome = match_info["outcome"]
        winner = None
        winner_by = None
        winner_margin = None
        winner_method = outcome.get("method", None)

        try:  # if the match was won by a team
            winner = outcome["winner"]
            by = outcome["by"].items()
        except KeyError:
            match_result = outcome["result"]
        else:
            match_result = MatchOutcomeEnum.winner
            winner_by = list(by)[0][0]
            winner_margin = list(by)[0][1]

        # since the event_name is not required in the JSON payload
        event_name = None

        if match_info.get("event", None):
            event_name = match_info["event"].get("name")

        # creating the object
        new_match_info = Match(
            season=match_info["season"],
            file_name=file_name,
            city=match_info.get("city", None),
            venue=match_info.get("venue", None),
            date_started=datetime.strptime(match_info["dates"][0], "%Y-%m-%d"),
            event_name=event_name,
            match_gender=match_info["gender"],
            match_type=match_info["match_type"],
            match_result=match_result,
            winner=winner,
            winner_by=winner_by,
            winner_margin=winner_margin,
            winner_method=winner_method,
            number_of_overs=match_info["overs"],
            number_of_balls_per_over=match_info["balls_per_over"],
            match_team_1=match_info["teams"][0],
            match_team_2=match_info["teams"][1],
            team_type=match_info["team_type"],
        )

        return new_match_info
