-- 9. Subir un 5% el sueldo del empleado que más días haya trabajado.
WITH
    dia_maximo AS (
    SELECT max(dias_diferentes_trabajados) AS max_dias_trabajados
    FROM (
        SELECT
            count(DISTINCT reparto.fecha) AS dias_diferentes_trabajados
        FROM reparto
        INNER JOIN empleados ON reparto.id_e = empleados.id_e
        GROUP BY empleados.id_e, empleados.nombre
        )
    ),
    empleados_mas_trabajadores AS (
        SELECT
            empleados.id_e
        FROM reparto
        INNER JOIN empleados ON reparto.id_e = empleados.id_e
        GROUP BY empleados.id_e, empleados.nombre
        HAVING count(DISTINCT reparto.fecha) = (SELECT max_dias_trabajados FROM dia_maximo)
    )

UPDATE empleados
SET sueldo = sueldo + ((sueldo / 100) * 5)
WHERE id_e IN (SELECT empleados_mas_trabajadores.id_e FROM empleados_mas_trabajadores)
;