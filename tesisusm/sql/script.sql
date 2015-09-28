#CREAR BASE DE DATOS ¨tesis_core¨
CREATE DATABASE tesis_core;

#CREAR USUARIO "tesis"
CREATE USER tesis IDENTIFIED BY 'tesis123';

#ASIGNAR PERMISOS AL USUARIO "tesis" SOBRE EL ESQUEMA "tesis_core"
GRANT ALL PRIVILEGES ON tesis_core.* TO tesis;

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#INSERT ROLES DE USUARIO
INSERT INTO tesis_core.app_rol_usuario (rol, descripcion) VALUES ('Root', 'Administradores del sistema');
INSERT INTO tesis_core.app_rol_usuario (rol, descripcion) VALUES ('Administrador', 'Dueño del negocio y/o encargado de la empresa');
INSERT INTO tesis_core.app_rol_usuario (rol, descripcion) VALUES ('Jefe', 'Supervisor de planta');

#INSERT TIPOS DE PRODUCTO
INSERT INTO tesis_core.app_tipo_producto (tipo_producto, descripcion) VALUES ('Materia prima', 'Productos utilizados en la elaboración del producto final');
INSERT INTO tesis_core.app_tipo_producto (tipo_producto, descripcion) VALUES ('Perecedero', 'Productos con fecha de caducidad reducida');
INSERT INTO tesis_core.app_tipo_producto (tipo_producto, descripcion) VALUES ('Producto', 'Producto final');

#INSERT CARGO DE EMPLEAQDO
INSERT INTO tesis_core.app_cargo (cargo, descripcion) VALUES ('Supervisor', 'Supervisor de planta');
INSERT INTO tesis_core.app_cargo (cargo, descripcion) VALUES ('Empaquetador', 'Empaqueta el producto final y arma los bultos');

#INSERT TIPO DE EMPLEADO
INSERT INTO tesis_core.app_tipo_empleado (tipo_empleado, descripcion) VALUES ('Fijo', 'Empleado fijo de la empresa');
INSERT INTO tesis_core.app_tipo_empleado (tipo_empleado, descripcion) VALUES ('Contratado', 'Empleado a tiempo determinado de la empresa');

################################################################
# USER #########################################################
################################################################

#DELETE DE APP_USUSARIO
DELIMITER //
CREATE TRIGGER del_user_from_user AFTER DELETE ON tesis_core.app_usuario FOR EACH ROW
BEGIN
	DELETE FROM tesis_core.auth_user WHERE id = OLD.usuario_id;
END;//
DELIMITER ;

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#UPDATE DE APP_USUSARIO
DELIMITER //
CREATE TRIGGER upd_user_is_active AFTER UPDATE ON tesis_core.app_usuario FOR EACH ROW
BEGIN
	IF NEW.activo = False THEN
		UPDATE tesis_core.auth_user SET is_active = False WHERE id = OLD.usuario_id;
	ELSEIF NEW.activo = True THEN
		UPDATE tesis_core.auth_user SET is_active = True WHERE id = OLD.usuario_id;
 	END IF;
END;//
DELIMITER ;

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#UPDATE DE AUTH_USER
DELIMITER //
CREATE TRIGGER upd_user_last_login AFTER UPDATE ON tesis_core.auth_user FOR EACH ROW
BEGIN
	UPDATE tesis_core.app_usuario SET ultima_conexion = NEW.last_login WHERE usuario_id = NEW.id;
END;//
DELIMITER ;

################################################################
# INVENTARIO ###################################################
################################################################

#INSERT DE APP_PRODUCTO
DELIMITER //
CREATE TRIGGER ins_prod_inventario AFTER INSERT ON tesis_core.app_producto FOR EACH ROW
BEGIN
	INSERT INTO tesis_core.app_stock (producto_id, codigo_producto, nombre_producto, cantidad_producto)
	VALUES (NEW.id_producto, NEW.codigo, NEW.producto, 0);
END;//
DELIMITER ;

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#UPDATE DE APP_PRODUCTO
DELIMITER //
CREATE TRIGGER upd_prod_inventario AFTER UPDATE ON tesis_core.app_producto FOR EACH ROW
BEGIN
	IF OLD.codigo <> NEW.codigo THEN
		UPDATE tesis_core.app_stock SET codigo_producto = NEW.codigo WHERE codigo_producto = OLD.codigo;
	END IF;
	IF OLD.producto <> NEW.producto THEN
		UPDATE tesis_core.app_stock SET nombre_producto = NEW.producto WHERE codigo_producto = OLD.codigo;
	END IF;
END;//
DELIMITER ;

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#DELETE DE APP_PRODUCTO
DELIMITER //
CREATE TRIGGER del_prod_inventario AFTER DELETE ON tesis_core.app_producto FOR EACH ROW
BEGIN
	DELETE FROM tesis_core.app_stock WHERE codigo_producto = OLD.codigo;
END;//
DELIMITER ;

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#INSERT DE APP_VENTA
DELIMITER //
CREATE TRIGGER upd_prod_venta AFTER INSERT ON tesis_core.app_venta FOR EACH ROW
BEGIN
	DECLARE cod_prod VARCHAR(10);
	DECLARE total_prod INTEGER;
	DECLARE total_venta INTEGER;
	SET @cod_prod := (SELECT codigo FROM tesis_core.app_producto WHERE id_producto = NEW.producto_id);
	SET @total_prod := (SELECT cantidad_producto from tesis_core.app_stock WHERE codigo_producto = @cod_prod);
	SET @total_venta := (SELECT SUM(@total_prod-NEW.cantidad) FROM dual);
	UPDATE tesis_core.app_stock SET cantidad_producto = @total_venta WHERE codigo_producto = @cod_prod;
END;//
DELIMITER ;

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#UPDATE DE APP_VENTA
DELIMITER //
CREATE TRIGGER upd_cant_venta AFTER UPDATE ON tesis_core.app_venta FOR EACH ROW
BEGIN
	DECLARE id_prod INTEGER;
	DECLARE disponible INTEGER;
	DECLARE total INTEGER;
	DECLARE total_inv INTEGER;
	SET @id_prod := (SELECT producto_id FROM tesis_core.app_venta WHERE id_venta = OLD.id_venta);
	SET @disponible := (SELECT cantidad_producto FROM tesis_core.app_stock WHERE producto_id = @id_prod);
	IF OLD.cantidad < NEW.cantidad THEN
		SET @total := (SELECT sum(NEW.cantidad-OLD.cantidad) FROM dual);
		SET @total_inv := (SELECT sum(@disponible-@total) FROM dual);
		UPDATE tesis_core.app_stock SET cantidad_producto = @total_inv WHERE producto_id = @id_prod;
	END IF;
	IF OLD.cantidad > NEW.cantidad THEN
		SET @total := (SELECT sum(OLD.cantidad-NEW.cantidad) FROM dual);
		SET @total_inv := (SELECT sum(@disponible+@total) FROM dual);
		UPDATE tesis_core.app_stock SET cantidad_producto = @total_inv WHERE producto_id = @id_prod;
	END IF;
END;//
DELIMITER ;

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#DELETE DE APP_VENTA
DELIMITER //
CREATE TRIGGER del_venta BEFORE DELETE ON tesis_core.app_venta FOR EACH ROW
BEGIN
	DECLARE id_prod INTEGER;
	DECLARE disponible INTEGER;
	DECLARE total INTEGER;
	DECLARE total_inv INTEGER;
	SET @id_prod := (SELECT producto_id FROM tesis_core.app_venta WHERE id_venta = OLD.id_venta);
	SET @disponible := (SELECT cantidad_producto FROM tesis_core.app_stock WHERE producto_id = @id_prod);
	SET @total := (SELECT cantidad FROM tesis_core.app_venta WHERE id_venta = OLD.id_venta);
	SET @total_inv := (SELECT sum(@disponible+@total) FROM dual);
	UPDATE tesis_core.app_stock SET cantidad_producto = @total_inv WHERE producto_id = @id_prod;
END;//
DELIMITER ;

#INSERT EJEMPLO GRAFICO
INSERT INTO tesis_core.app_utilidad_mensual (ano,ene,feb,mar,abr,may,jun,jul,ago,sep,oct,nov,dic) VALUES (2014,10,20,30,40,45,40,40,35,50,25,60,100);
INSERT INTO tesis_core.app_utilidad_mensual (ano,ene,feb,mar,abr,may,jun,jul,ago,sep,oct,nov,dic) VALUES (2015,25,20,35,30,45,40,10,20,30,60,30,55);