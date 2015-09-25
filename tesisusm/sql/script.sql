--INSERT ROLES DE USUARIO
INSERT INTO tesis_core.app_rol_usuario (rol, descripcion) VALUES ('Root', 'Administradores del sistema');
INSERT INTO tesis_core.app_rol_usuario (rol, descripcion) VALUES ('Administrador', 'Dueño del negocio y/o encargado de la empresa');
INSERT INTO tesis_core.app_rol_usuario (rol, descripcion) VALUES ('Jefe', 'Supervisor de planta');

--INSERT TIPOS DE PRODUCTO
INSERT INTO tesis_core.app_tipo_producto (tipo_producto, descripcion) VALUES ('Materia prima', 'Productos utilizados en la elaboración del producto final');
INSERT INTO tesis_core.app_tipo_producto (tipo_producto, descripcion) VALUES ('Perecedero', 'Productos con fecha de caducidad reducida');
INSERT INTO tesis_core.app_tipo_producto (tipo_producto, descripcion) VALUES ('Producto', 'Producto final');

--INSERT CARGO DE EMPLEAQDO
INSERT INTO tesis_core.app_cargo (cargo, descripcion) VALUES ('Supervisor', 'Supervisor de planta');
INSERT INTO tesis_core.app_cargo (cargo, descripcion) VALUES ('Empaquetador', 'Empaqueta el producto final y arma los bultos');

--INSERT TIPO DE EMPLEADO
INSERT INTO tesis_core.app_tipo_empleado (tipo_empleado, descripcion) VALUES ('Fijo', 'Empleado fijo de la empresa');
INSERT INTO tesis_core.app_tipo_empleado (tipo_empleado, descripcion) VALUES ('Contratado', 'Empleado a tiempo determinado de la empresa');

/*#########
USER #####
#########*/

--DELETE DE APP_USUSARIO
DELIMITER //
CREATE TRIGGER del_user_from_user AFTER DELETE ON tesis_core.app_usuario FOR EACH ROW
BEGIN
	DELETE FROM tesis_core.auth_user WHERE id = OLD.usuario_id;
END;//
DELIMITER ;

--UPDATE DE APP_USUSARIO
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

--UPDATE DE AUTH_USER
DELIMITER //
CREATE TRIGGER upd_user_last_login AFTER UPDATE ON tesis_core.auth_user FOR EACH ROW
BEGIN
	UPDATE tesis_core.app_usuario SET ultima_conexion = NEW.last_login WHERE usuario_id = NEW.id;
END;//
DELIMITER ;

/*###############
INVENTARIO #####
##############*/

--INSERT DE APP_PRODUCTO
DELIMITER //
CREATE TRIGGER ins_prod_inventario AFTER INSERT ON tesis_core.app_producto FOR EACH ROW
BEGIN
	INSERT INTO tesis_core.app_inventario (codigo_producto, nombre_producto, cantidad_producto, precio_producto, precio_total)
	VALUES (NEW.codigo, NEW.producto, 0, NEW.precio_unitario, 0);
END;//
DELIMITER ;

--UPDATE DE APP_PRODUCTO
DELIMITER //
CREATE TRIGGER upd_prod_inventario AFTER UPDATE ON tesis_core.app_producto FOR EACH ROW
BEGIN
	IF OLD.codigo <> NEW.codigo THEN
		UPDATE tesis_core.app_inventario SET codigo_producto = NEW.codigo WHERE codigo_producto = OLD.codigo;
	END IF;
	IF OLD.producto <> NEW.producto THEN
		UPDATE tesis_core.app_inventario SET nombre_producto = NEW.producto WHERE codigo_producto = OLD.codigo;
	END IF;
	IF OLD.precio_unitario <> NEW.precio_unitario THEN
		UPDATE tesis_core.app_inventario SET precio_producto = NEW.precio_unitario WHERE codigo_producto = OLD.codigo;
	END IF;
END;//
DELIMITER ;

--DELETE DE APP_PRODUCTO
DELIMITER //
CREATE TRIGGER del_prod_inventario AFTER DELETE ON tesis_core.app_producto FOR EACH ROW
BEGIN
	DELETE FROM tesis_core.app_inventario WHERE codigo_producto = OLD.codigo;
END;//
DELIMITER ;
