SELECT status,
    COUNT(*) AS nr_credite,
    SUM(amount) AS suma_acordata,
    ROUND( AVG(amount)::numeric, 2) AS suma_medie
FROM loan
GROUP BY status
ORDER BY status;