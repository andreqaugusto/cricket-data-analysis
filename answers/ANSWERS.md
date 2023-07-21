# Answers

## Question 0

I would say that I have a familiarity of 2 with Cricket. I've never seen Cricket before or knew its rules. However, I knew that it was a game similar to one that is widely played here in Brazil by children: [Taco](https://en.wikipedia.org/wiki/Bete-ombro). After watching the Netflix Youtube video, it became clear that all the core elements are the same: wickets, batting, running between the wickets, etc.

The rules are similar, as you can read on the Wikipedia link. However, we don't have overs and deliveries - and these concepts were (and still are) hard to understand.

## Question 1

No answer is needed.

## Question 2

a. Using the query provided in [question2a.sql](./question2a.sql), here are the 5 teams that played the most during the period in question, with their percentage and total wins (considering the restrictions that were given):
| Gender | Year | Country   | Matches Played | Matches Won | Win Percentage |
| ------ | ---- | --------- | -------------- | ----------- | -------------- |
| male   | 2009 | Australia | 36             | 22          | 0.61           |
| male   | 2007 | England   | 31             | 16          | 0.52           |
| male   | 2007 | Australia | 30             | 23          | 0.77           |
| male   | 2007 | India     | 30             | 15          | 0.50           |
| male   | 2006 | Sri Lanka | 29             | 16          | 0.55           |

b. Using the previous query as a baseline, we have that the **Australian female team** and the **Netherlands male team** were the ones with most win percentage (100%):
| Gender | Country     | Games Played | Win Percentage |
| ------ | ----------- | ------------ | -------------- |
| female | Australia   | 11           | 1.00           |
| male   | Netherlands | 2            | 1.00           |

The query used can be seem at [question2b.sql](./question2b.sql).

c. If I understood [batting strike rate](https://en.wikipedia.org/wiki/Strike_rate) correctly, then these are the 5 top players in Strike Rate for 2019:
| Player      | Runs | Innings | Batting Average |
| ----------- | ---- | ------- | --------------- |
| TK Curran   | 107  | 108     | 99.07           |
| JM Bairstow | 844  | 852     | 99.06           |
| Q de Kock   | 774  | 784     | 98.72           |
| RR Pant     | 305  | 310     | 98.39           |
| AU Rashid   | 74   | 76      | 97.37           |

The query used can be seem at [question2c.sql](./question2b.sql).

## Question 3

There is two things that come to mind that would need to be changed:
1. the more obvious change would be to change the code that downloads directly from the Cricsheet website (see `main.py`). It would need to be changed or adapted to download from other sources (either a streaming service or another URL from Cricsheet).
2. the other one (and most important) is the `match_id` definition. Since we are batch-backfilling, we ended up using the auto-incremental index from `sqlite` (since I didn't wanted to rely on the data itself due to my unfamiliarity with cricket). In the go-forward scenario, we would need to have an index that we can trust in a way to **not** let us have duplicate matches in our database. You can achieve this by hashing some fields (which should be chosen wisely) or using some natural ID from the service that you are reading the data from (in which case, as I said above, I chose to not do this for my assessment).

There are other aspects that would need to be addressed (e.g. orchestration), but these two presented are the most relevant to the code that was written in this assessment.
