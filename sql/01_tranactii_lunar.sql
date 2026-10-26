SELECT DATE_TRUNC('month', date) AS luna,
    COUNT(*) AS nr_tranzactii,
    SUM(amount) AS valoare_totala
FROM trans
GROUP BY 1
ORDER BY 1;