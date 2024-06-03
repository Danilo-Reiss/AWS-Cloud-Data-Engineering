SELECT 
    max(cast(TARIFA as decimal)), 
    min(cast(TARIFA as decimal)),
    avg(cast(TARIFA as decimal)),
    CASE
        WHEN max(cast(TARIFA as decimal)) > 3500 THEN 'Tarifa máxima maior que 3,500'
    END,
    UTCNOW()
FROM s3object s
WHERE ORIGEM in (upper('sbsp')) and DESTINO in (upper('sbrj'))"