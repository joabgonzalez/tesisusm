#CREAR BASE DE DATOS ¨tesis_core¨
CREATE DATABASE tesis_core;

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#CREAR USUARIO "tesis"
CREATE USER tesis IDENTIFIED BY 'tesis123';

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#ASIGNAR PERMISOS AL USUARIO "tesis" SOBRE EL ESQUEMA "tesis_core"
GRANT ALL PRIVILEGES ON tesis_core.* TO tesis;