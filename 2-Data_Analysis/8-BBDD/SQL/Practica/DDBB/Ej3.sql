-- 3. Obtener los repartos (nombre del bar, envase y capacidad de la bebida, fecha y cantidad) realizados por **Prudencio Caminero**.
SELECT
    bares.nombre,
    cervezas.envase,
    cervezas.capacidad,
    reparto.fecha,
    reparto.cantidad
FROM reparto
INNER JOIN empleados ON reparto.id_e = empleados.id_e
INNER JOIN bares ON reparto.id_b = bares.id_b
INNER JOIN cervezas ON reparto.id_c = cervezas.id_c
WHERE empleados.nombre = 'Prudencio Caminero'
;