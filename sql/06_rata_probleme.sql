SELECT COUNT(*) AS total_credite,
  SUM(CASE WHEN status IN ('B','D') THEN 1 ELSE 0 END) AS credite_cu_probleme,
  ROUND(100.0 * SUM(CASE WHEN status IN ('B','D') THEN 1 ELSE 0 END) / COUNT(*), 2) AS rata_probleme_procent
FROM loan;