#INSERT DE PROYECCION_HISTORICO
DELIMITER //
CREATE TRIGGER ins_proyeccion_venta AFTER INSERT ON tesis_core.app_proyeccion_historico FOR EACH ROW
BEGIN
	DELETE FROM tesis_core.app_proyeccion_venta;
	CALL gra_proyeccion (NEW.ano);
END;//
DELIMITER ;
