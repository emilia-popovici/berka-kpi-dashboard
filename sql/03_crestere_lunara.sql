WITH lunar AS (
    SELECT DATE_TRUNC('month', date) AS luna,
        ROUND( SUM(amount)::numeric, 2) AS valoare_totala
    FROM trans
    GROUP BY 1
)

SELECT luna, valoare_totala,
    LAG(valoare_totala) OVER (ORDER BY luna) AS luna_anterioara,
    ROUND(
        (valoare_totala - LAG(valoare_totala) 
        OVER (ORDER BY luna)) / NULLIF(LAG(valoare_totala) 
        OVER (ORDER BY luna), 0) * 100, 2) AS crestere_procent
FROM lunar
ORDER BY luna;