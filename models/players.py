from sqlalchemy import Column, Integer, String, UniqueConstraint

from database import Base


# following https://cricsheet.org/format/json/#the-info-section
class PlayerMatch(Base):
    __tablename__ = "players_in_matches"
    __table_args__ = (UniqueConstraint("match_id", "player_registry", name="_match_player_uc"),)

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    match_id = Column(Integer)
    player_name = Column(String)
    player_team = Column(String)
    player_registry = Column(String, nullable=True)

    @classmethod
    def parse_all_players_from_match(cls, match_info: dict, match_id: int) -> list["PlayerMatch"]:
        """Creates PlayerMatch objects for all the players in a match"""
        all_players = []
        teams = match_info["players"]

        # cricsheet does not require this field
        registries = match_info.get("registry", None)

        if registries:
            all_people_registries: dict = registries["people"]

        for team in teams:
            for player in teams[team]:
                player_registry = None
                if registries:
                    player_registry = all_people_registries.get(player, None)  # type: ignore

                player_info = PlayerMatch(
                    match_id=match_id,
                    player_name=player,
                    player_team=team,
                    player_registry=player_registry,
                )

                all_players.append(player_info)
        return all_players
