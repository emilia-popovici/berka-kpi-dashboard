SELECT DATE_TRUNC('month', date) AS luna,
    ROUND( AVG(balance)::numeric, 2) AS sold_mediu
FROM trans
GROUP BY 1
ORDER BY 1;