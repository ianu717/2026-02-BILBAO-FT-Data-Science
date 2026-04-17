-- 5. Nombre de los empleados que han repartido a los bares **"Stop"** y **"Las Vegas"** cervezas con envase botella.
SELECT
    empleados.nombre,
    count(DISTINCT bares.nombre) AS num_bares_repartidos
FROM empleados
INNER JOIN reparto ON empleados.id_e = reparto.id_e
INNER JOIN bares ON reparto.id_b = bares.id_b
INNER JOIN cervezas ON reparto.id_c = cervezas.id_c
WHERE bares.nombre IN ('Stop', 'Las Vegas') AND cervezas.envase = 'Botella'
GROUP BY empleados.id_e, empleados.nombre
HAVING num_bares_repartidos = 2
;