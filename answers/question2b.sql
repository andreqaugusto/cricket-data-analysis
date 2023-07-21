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
	AND strftime('%Y', date_started) = '2019'
),

RESULTS_PREP AS (
SELECT match_id, match_gender, year, match_team_1 AS team, CASE WHEN winner = match_team_1 THEN 1 ELSE 0 END AS IS_WINNER FROM MATCH_FILTER
UNION
SELECT match_id, match_gender, year, match_team_2 AS team, CASE WHEN winner = match_team_2 THEN 1 ELSE 0 END AS IS_WINNER FROM MATCH_FILTER
), 


CALCULATION AS (
SELECT
	--doing the subquery just to make sure that the ROW_NUMBER() function works as expected 
	*,
	ROW_NUMBER() OVER (PARTITION BY match_gender ORDER BY percentage_wins DESC, total_wins DESC) AS RN
FROM 
	(	
		SELECT
			match_gender,
			year,
			team,
			SUM(1) AS total_matches,
			SUM(IS_WINNER) AS total_wins,
			printf("%.2f", SUM(IS_WINNER) * 1.0 / SUM(1)) AS percentage_wins
		FROM RESULTS_PREP
		GROUP BY 1,2,3
	)
)

SELECT 
	match_gender,
	team,
	total_matches 
	total_wins,
	percentage_wins
FROM CALCULATION
WHERE RN = 1
		
	