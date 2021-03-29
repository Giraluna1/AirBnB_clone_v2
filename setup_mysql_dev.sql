-- Prepares a MySQL server for the project
--Creamos la DB

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

--crear un nuevo usuario

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Darle los provilegios

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Darle el permiso de ver

GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

--Actualizar los permisos

FLUSH PRIVILEGES;
