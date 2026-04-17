-- 7. Obtener el nombre y localidad del bar que más litros de cerveza ha comprado.
SELECT
    bares.nombre,
    bares.localidad
FROM bares
INNER JOIN reparto ON bares.id_b = reparto.id_b
INNER JOIN cervezas ON reparto.id_c = cervezas.id_c
GROUP BY bares.id_b, bares.nombre, bares.localidad
ORDER BY sum(cervezas.capacidad * reparto.cantidad) DESC
LIMIT 1
;