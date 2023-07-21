from sqlalchemy import Column, Integer, String, UniqueConstraint

from database import Base


# following https://cricsheet.org/format/json/#the-innings-section
class Delivery(Base):
    __tablename__ = "innings_deliveries"
    __table_args__ = (
        UniqueConstraint(
            "match_id",
            "inning_number",
            "over_number",
            "delivery_number",
            name="_match_inning_over_delivery_uc",
        ),
    )

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    match_id = Column(Integer)
    inning_number = Column(Integer)
    over_number = Column(Integer)
    team = Column(String)
    delivery_number = Column(Integer)
    batter = Column(String)
    bowler = Column(String)
    non_striker = Column(String)
    runs_batter = Column(Integer)
    runs_extras = Column(Integer)
    runs_total = Column(Integer)

    @classmethod
    def parse_from_data(cls, innings: list[dict], match_id: int) -> list["Delivery"]:
        """Parses the deliveries from a match and returns a list of Delivery objects"""

        all_deliveries_parsed = []
        #! There is probably a smarter method to do this than a 3-nested for loop...
        #! however, I'm not having the time to think about it. I'll come back to this later
        for idx_inn, inning in enumerate(innings):
            team = inning["team"]
            overs = inning["overs"]
            for over in overs:
                # adding one to make it start at 1 instead of 0 - more natural to humans
                over_number = over["over"] + 1
                for idx_del, delivery in enumerate(over["deliveries"]):
                    delivery_added = Delivery(
                        match_id=match_id,
                        # same situation as the over_number
                        # could have used `enumerate(innings, start=1)` but I think this is more readable
                        inning_number=idx_inn + 1,
                        over_number=over_number,
                        team=team,
                        # same situation as above
                        delivery_number=idx_del + 1,
                        batter=delivery["batter"],
                        bowler=delivery["bowler"],
                        non_striker=delivery["non_striker"],
                        runs_batter=delivery["runs"]["batter"],
                        runs_extras=delivery["runs"]["extras"],
                        runs_total=delivery["runs"]["total"],
                    )

                    all_deliveries_parsed.append(delivery_added)
        return all_deliveries_parsed
