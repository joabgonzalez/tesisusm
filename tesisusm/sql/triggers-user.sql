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

#DELETE DE APP_USUSARIO
DELIMITER //
CREATE TRIGGER del_user_from_user AFTER DELETE ON tesis_core.app_usuario FOR EACH ROW
BEGIN
	DELETE FROM tesis_core.auth_user WHERE id = OLD.usuario_id;
END;//
DELIMITER ;