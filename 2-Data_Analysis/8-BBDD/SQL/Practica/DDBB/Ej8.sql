-- 8. Obtener los bares que han adquirido todos los tipos de cerveza con envase de botella y capacidad menor que 1 litro.
WITH botellas_menores_1 AS (
    SELECT count() AS total FROM cervezas WHERE cervezas.envase = 'Botella' AND capacidad < 1
)
SELECT
    bares.nombre
FROM bares
INNER JOIN reparto ON bares.id_b = reparto.id_b
INNER JOIN cervezas ON reparto.id_c = cervezas.id_c
WHERE cervezas.envase = 'Botella' AND capacidad < 1
GROUP BY bares.id_b, bares.nombre
HAVING count(DISTINCT cervezas.id_c) = (SELECT total FROM botellas_menores_1)
;