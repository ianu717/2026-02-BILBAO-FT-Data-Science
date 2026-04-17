-- 6. Obtener el nombre y número de viajes que ha realizado cada empleado fuera de **Villa Botijo**.
SELECT
    empleados.nombre,
    count() AS numero_viajes
FROM empleados
INNER JOIN reparto ON empleados.id_e = reparto.id_e
INNER JOIN bares ON reparto.id_b = bares.id_b
WHERE bares.localidad != 'Villa Botijo'
GROUP BY empleados.id_e, empleados.nombre
;