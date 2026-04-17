-- Tabla cervezas
DROP TABLE IF EXISTS cervezas;
CREATE TABLE cervezas (
    id_c INTEGER,
    envase TEXT(10),
    capacidad REAL,
    stock INTEGER,
    PRIMARY KEY(id_c ASC)
);

INSERT INTO cervezas (envase, capacidad, stock) VALUES ('Botella', 0.2, 3600);
INSERT INTO cervezas (envase, capacidad, stock) VALUES ('Botella', 0.33, 1200);
INSERT INTO cervezas (envase, capacidad, stock) VALUES ('Lata', 0.33, 2400);
INSERT INTO cervezas (envase, capacidad, stock) VALUES ('Botella', 1, 288);
INSERT INTO cervezas (envase, capacidad, stock) VALUES ('Barril', 60, 30);

-- Tabla bares
DROP TABLE IF EXISTS bares;
CREATE TABLE bares (
    id_b INTEGER,
    cif TEXT(10),
    nombre TEXT(15),
    localidad TEXT(15),
    PRIMARY KEY(id_b ASC)
);

INSERT INTO bares (cif, nombre, localidad) VALUES ('11111111X', 'Stop', 'Villa Botijo');
INSERT INTO bares (cif, nombre, localidad) VALUES ('22222222Y', 'Las Vegas', 'Villa Botijo');
INSERT INTO bares (cif, nombre, localidad) VALUES ('-', 'Club Social', 'Las Ranas');
INSERT INTO bares (cif, nombre, localidad) VALUES ('33333333Z', 'Otra Ronda', 'La Esponja');

-- Tabla empleados
DROP TABLE IF EXISTS empleados;
CREATE TABLE IF NOT EXISTS empleados (
    id_e INTEGER,
    nombre TEXT(20),
    sueldo INTEGER,
    PRIMARY KEY(id_e ASC)
);

INSERT INTO empleados (nombre, sueldo) VALUES ('Prudencio Caminero', 120000);
INSERT INTO empleados (nombre, sueldo) VALUES ('Vicente Merario', 110000);
INSERT INTO empleados (nombre, sueldo) VALUES ('Valentin Siempre', 100000);

-- Tabla reparto
DROP TABLE IF EXISTS reparto;
CREATE TABLE reparto (
    id_e INTEGER,
    id_b INTEGER,
    id_c INTEGER,
    fecha DATETIME,
    cantidad INTEGER,
    FOREIGN KEY (id_e) REFERENCES empleados ON DELETE RESTRICT,
    FOREIGN KEY (id_b) REFERENCES bares ON DELETE RESTRICT,
    FOREIGN KEY (id_c) REFERENCES cervezas ON DELETE RESTRICT
);

INSERT INTO reparto (id_e, id_b, id_c, fecha, cantidad) VALUES (1, 1, 1, '2005-10-21', 240);
INSERT INTO reparto (id_e, id_b, id_c, fecha, cantidad) VALUES (1, 1, 2, '2005-10-21', 48);
INSERT INTO reparto (id_e, id_b, id_c, fecha, cantidad) VALUES (1, 2, 3, '2005-10-22', 60);
INSERT INTO reparto (id_e, id_b, id_c, fecha, cantidad) VALUES (1, 4, 5, '2005-10-22', 4);
INSERT INTO reparto (id_e, id_b, id_c, fecha, cantidad) VALUES (2, 2, 3, '2005-10-22', 48);
INSERT INTO reparto (id_e, id_b, id_c, fecha, cantidad) VALUES (2, 2, 5, '2005-10-23', 2);
INSERT INTO reparto (id_e, id_b, id_c, fecha, cantidad) VALUES (2, 4, 1, '2005-10-23', 480);
INSERT INTO reparto (id_e, id_b, id_c, fecha, cantidad) VALUES (2, 4, 2, '2005-10-24', 72);
INSERT INTO reparto (id_e, id_b, id_c, fecha, cantidad) VALUES (3, 3, 3, '2005-10-24', 48);
INSERT INTO reparto (id_e, id_b, id_c, fecha, cantidad) VALUES (3, 3, 4, '2005-10-25', 20);
