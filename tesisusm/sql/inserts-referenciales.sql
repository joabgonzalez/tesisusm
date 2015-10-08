#INSERT ROLES DE USUARIO
INSERT INTO tesis_core.app_rol_usuario (rol, descripcion) VALUES ('Administrador', 'Dueño del negocio y/o encargado de la empresa');
INSERT INTO tesis_core.app_rol_usuario (rol, descripcion) VALUES ('Jefe', 'Supervisor de planta');

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#INSERT TIPOS DE PRODUCTO
INSERT INTO tesis_core.app_tipo_producto (tipo_producto, descripcion) VALUES ('Materia prima', 'Productos utilizados en la elaboración del producto final');
INSERT INTO tesis_core.app_tipo_producto (tipo_producto, descripcion) VALUES ('Producto final', 'Producto final disponible para la venta');

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#INSERT CARGO DE EMPLEAQDO
INSERT INTO tesis_core.app_cargo (cargo, descripcion) VALUES ('Supervisor', 'Supervisor de planta');
INSERT INTO tesis_core.app_cargo (cargo, descripcion) VALUES ('Empaquetador', 'Empaqueta el producto final y arma los bultos');

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#INSERT TIPO DE EMPLEADO
INSERT INTO tesis_core.app_tipo_empleado (tipo_empleado, descripcion) VALUES ('Fijo', 'Empleado fijo de la empresa');
INSERT INTO tesis_core.app_tipo_empleado (tipo_empleado, descripcion) VALUES ('Contratado', 'Empleado a tiempo determinado de la empresa');

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#INSERT EJEMPLO GRAFICO
#INSERT INTO tesis_core.app_utilidad_mensual (ano,ene,feb,mar,abr,may,jun,jul,ago,sep,oct,nov,dic) VALUES (2015,25,20,35,30,45,40,10,20,30,60,30,55);