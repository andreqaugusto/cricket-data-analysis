import json
from pathlib import Path

from database import managed_db_connection
from models import Delivery, Match, PlayerMatch


def load_data_into_db(file_path: Path | str) -> None:
    """Loads data into DB from a file path"""

    if isinstance(file_path, Path):
        file_path = str(file_path)

    assert file_path.endswith(".json"), "File must be a json file."

    file_name = file_path.split("/")[-1]

    # Open the JSON file
    with open(file_path, "r") as f:
        # Read the contents of the file
        data = json.load(f)

    # separate the match_info and innings_info
    match_info = data["info"]
    innings_info = data["innings"]

    match = _load_match_info(match_info=match_info, file_name=file_name)
    _load_players_info(match_info=match_info, match_id=match.match_id)  # type: ignore
    _load_innings_info(innings_info=innings_info, match_id=match.match_id)  # type: ignore


def _load_match_info(match_info: dict, file_name: str) -> Match:
    """Function that loads the match_info into the database"""

    with managed_db_connection() as db:
        match = Match.parse_from_data(match_info, file_name)
        db.add(match)
        db.commit()
        db.refresh(match)

    return match


def _load_players_info(match_info: dict, match_id: int) -> None:
    """Function that loads the players into the database using match_info"""

    with managed_db_connection() as db:
        players = PlayerMatch.parse_all_players_from_match(match_info=match_info, match_id=match_id)
        for player in players:
            db.add(player)
        db.commit()


def _load_innings_info(innings_info: list, match_id: int) -> None:
    """Function that loads the innings into the database"""

    with managed_db_connection() as db:
        deliveries = Delivery.parse_from_data(innings=innings_info, match_id=match_id)
        for delivery in deliveries:
            db.add(delivery)
        db.commit()
