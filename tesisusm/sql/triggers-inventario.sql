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
	IF ((OLD.codigo <> NEW.codigo) OR (OLD.producto <> NEW.producto)) THEN
		UPDATE tesis_core.app_stock SET codigo_producto = NEW.codigo, nombre_producto = NEW.producto WHERE codigo_producto = OLD.codigo;
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
	CALL gra_venta_mensual(NEW.id_venta, NEW.total_venta);
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