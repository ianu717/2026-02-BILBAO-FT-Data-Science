-- 2. Obtener el Cif y nombre de los bares a los que se ha repartido cerveza de tipo **Botella** y capacidad inferior a 1 litro, ordenados por localidad.
SELECT DISTINCT
    bares.cif,
    bares.nombre
FROM bares
INNER JOIN reparto ON bares.id_b = reparto.id_b
INNER JOIN cervezas ON reparto.id_c = cervezas.id_c
WHERE cervezas.envase = 'Botella' AND cervezas.capacidad < 1
ORDER BY bares.localidad
;