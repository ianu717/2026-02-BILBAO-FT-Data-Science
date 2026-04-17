-- 10. Insertar un nuevo reparto del empleado **"Vicente Merario"** al bar **"Stop"** de 48 cervezas de tipo lata el día 10/26/05.
INSERT INTO reparto (id_e, id_b, id_c, fecha, cantidad)
VALUES (
    (SELECT empleados.id_e FROM empleados WHERE empleados.nombre = 'Vicente Merario'),
    (SELECT bares.id_b FROM bares WHERE bares.nombre = 'Stop'),
    (SELECT cervezas.id_c FROM cervezas WHERE cervezas.envase = 'Lata'),
    '2005-10-26',
    48
);