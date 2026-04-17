-- 4. Obtener los bares a los que se les ha repartido envases de tipo **botella** y capacidad 0.2 ó 0.33.
SELECT DISTINCT
    bares.*
FROM bares
INNER JOIN reparto ON bares.id_b = reparto.id_b
INNER JOIN cervezas ON reparto.id_c = cervezas.id_c
WHERE cervezas.envase = 'Botella' AND cervezas.capacidad IN (0.2, 0.33)
;