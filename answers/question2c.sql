WITH PREP_MATCHES AS (
	SELECT match_id FROM matches
	WHERE strftime('%Y', date_started) = '2019'
)

SELECT 
	batter,
	SUM(runs_batter) AS total_runs_scored,
	COUNT(*) AS total_at_bats,
	printf("%.2f", SUM(runs_batter) * 1.0 / COUNT(*) * 100) AS strike_rate
FROM innings_deliveries AS DELIVERIES
INNER JOIN PREP_MATCHES ON DELIVERIES.match_id = PREP_MATCHES.match_id
GROUP BY batter
ORDER BY strike_rate DESC