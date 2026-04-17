-- 1. Obtener el nombre de los empleados que hayan repartido al bar **Stop durante la semana del 17 al 23 de octubre de 2005.
SELECT DISTINCT
    empleados.nombre
FROM empleados
INNER JOIN reparto ON empleados.id_e = reparto.id_e
INNER JOIN bares ON reparto.id_b = bares.id_b
WHERE bares.nombre = 'Stop' AND reparto.fecha BETWEEN '2005-10-17' AND '2005-10-23'
;