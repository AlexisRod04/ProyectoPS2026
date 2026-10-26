CREATE DATABASE IF NOT EXISTS sistema_evaluacion;

CREATE USER IF NOT EXISTS 'maya_evaluador'@'localhost'
IDENTIFIED BY 'amolosconejos123';

GRANT ALL PRIVILEGES ON sistema_evaluacion.*
TO 'maya_evaluador'@'localhost';