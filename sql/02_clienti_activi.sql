SELECT DATE_TRUNC('month', date) AS luna,
    COUNT(DISTINCT account_id) AS conturi_active
FROM trans
GROUP BY 1
ORDER BY 1;