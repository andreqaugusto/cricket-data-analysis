WITH MATCH_FILTER AS
(
	SELECT
		match_id, --just for debug
		match_gender, 
		strftime('%Y', date_started) AS year, 
		winner,
		match_team_1,
		match_team_2
	FROM matches
	WHERE 1=1
	AND match_result NOT IN ('tie', 'no_result')
	AND (winner_method != 'D/L' OR winner_method IS NULL)
),

RESULTS_PREP AS (
SELECT match_id, match_gender, year, match_team_1 AS team, CASE WHEN winner = match_team_1 THEN 1 ELSE 0 END AS IS_WINNER FROM MATCH_FILTER
UNION
SELECT match_id, match_gender, year, match_team_2 AS team, CASE WHEN winner = match_team_2 THEN 1 ELSE 0 END AS IS_WINNER FROM MATCH_FILTER
)

SELECT
	match_gender,
	year,
	team,
	SUM(1) AS total_matches,
	SUM(IS_WINNER) AS total_wins,
	printf("%.2f", SUM(IS_WINNER) * 1.0 / SUM(1)) AS percentage_wins
FROM RESULTS_PREP
GROUP BY 1,2,3
ORDER BY total_matches DESC

		
	