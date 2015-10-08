DELIMITER //
CREATE PROCEDURE gra_venta_mensual (IN idv INTEGER, IN ttv DECIMAL)
BEGIN
	SET @ano := (SELECT cast(date_format(fecha_venta, '%Y') AS UNSIGNED) FROM tesis_core.app_venta WHERE id_venta = idv);
	SET @mes := (SELECT cast(date_format(fecha_venta, '%m') AS UNSIGNED) FROM tesis_core.app_venta WHERE id_venta = idv);
	IF NOT EXISTS (SELECT * FROM tesis_core.app_utilidad_mensual WHERE ano = (SELECT date_format(fecha_venta, '%Y') FROM tesis_core.app_venta WHERE id_venta = idv)) THEN
		IF @mes = 1 THEN
			INSERT INTO tesis_core.app_utilidad_mensual (ano,ene) VALUES (@ano,ttv);
		ELSEIF @mes = 2 THEN
			INSERT INTO tesis_core.app_utilidad_mensual (ano,feb) VALUES (@ano,ttv);
		ELSEIF @mes = 3 THEN
			INSERT INTO tesis_core.app_utilidad_mensual (ano,mar) VALUES (@ano,ttv);
		ELSEIF @mes = 4 THEN
			INSERT INTO tesis_core.app_utilidad_mensual (ano,abr) VALUES (@ano,ttv);
		ELSEIF @mes = 5 THEN
			INSERT INTO tesis_core.app_utilidad_mensual (ano,may) VALUES (@ano,ttv);
		ELSEIF @mes = 6 THEN
			INSERT INTO tesis_core.app_utilidad_mensual (ano,jun) VALUES (@ano,ttv);
		ELSEIF @mes = 7 THEN
			INSERT INTO tesis_core.app_utilidad_mensual (ano,jul) VALUES (@ano,ttv);
		ELSEIF @mes = 8 THEN
			INSERT INTO tesis_core.app_utilidad_mensual (ano,ago) VALUES (@ano,ttv);
		ELSEIF @mes = 9 THEN
			INSERT INTO tesis_core.app_utilidad_mensual (ano,sep) VALUES (@ano,ttv);
		ELSEIF @mes = 10 THEN
			INSERT INTO tesis_core.app_utilidad_mensual (ano,oct) VALUES (@ano,ttv);
		ELSEIF @mes = 11 THEN
			INSERT INTO tesis_core.app_utilidad_mensual (ano,nov) VALUES (@ano,ttv);
		ELSEIF @mes = 12 THEN
			INSERT INTO tesis_core.app_utilidad_mensual (ano,dic) VALUES (@ano,ttv);
		END IF;
	ELSE
		SET @id := (SELECT id_utilidad_mensual FROM tesis_core.app_utilidad_mensual WHERE ano = @ano);
		IF @mes = 1 THEN
			SET @va := (SELECT ene FROM tesis_core.app_utilidad_mensual WHERE ano = @ano);
			SET @total := (SELECT sum(@va+ttv) FROM dual);
			UPDATE tesis_core.app_utilidad_mensual SET ene = @total WHERE id_utilidad_mensual = @id;
		ELSEIF @mes = 2 THEN
			SET @va := (SELECT feb FROM tesis_core.app_utilidad_mensual WHERE ano = @ano);
			SET @total := (SELECT sum(@va+ttv) FROM dual);
			UPDATE tesis_core.app_utilidad_mensual SET feb = @total WHERE id_utilidad_mensual = @id;
		ELSEIF @mes = 3 THEN
			SET @va := (SELECT mar FROM tesis_core.app_utilidad_mensual WHERE ano = @ano);
			SET @total := (SELECT sum(@va+ttv) FROM dual);
			UPDATE tesis_core.app_utilidad_mensual SET mar = @total WHERE id_utilidad_mensual = @id;
		ELSEIF @mes = 4 THEN
			SET @va := (SELECT abr FROM tesis_core.app_utilidad_mensual WHERE ano = @ano);
			UPDATE tesis_core.app_utilidad_mensual SET abr = @total WHERE id_utilidad_mensual = @id;
		ELSEIF @mes = 5 THEN
			SET @va := (SELECT may FROM tesis_core.app_utilidad_mensual WHERE ano = @ano);
			SET @total := (SELECT sum(@va+ttv) FROM dual);
			UPDATE tesis_core.app_utilidad_mensual SET may = @total WHERE id_utilidad_mensual = @id;
		ELSEIF @mes = 6 THEN
			SET @va := (SELECT jun FROM tesis_core.app_utilidad_mensual WHERE ano = @ano);
			SET @total := (SELECT sum(@va+ttv) FROM dual);
			UPDATE tesis_core.app_utilidad_mensual SET jun = @total WHERE id_utilidad_mensual = @id;
		ELSEIF @mes = 7 THEN
			SET @va := (SELECT jul FROM tesis_core.app_utilidad_mensual WHERE ano = @ano);
			SET @total := (SELECT sum(@va+ttv) FROM dual);
			UPDATE tesis_core.app_utilidad_mensual SET jul = @total WHERE id_utilidad_mensual = @id;
		ELSEIF @mes = 8 THEN
			SET @va := (SELECT ago FROM tesis_core.app_utilidad_mensual WHERE ano = @ano);
			SET @total := (SELECT sum(@va+ttv) FROM dual);
			UPDATE tesis_core.app_utilidad_mensual SET ago = @total WHERE id_utilidad_mensual = @id;
		ELSEIF @mes = 9 THEN
			SET @va := (SELECT sep FROM tesis_core.app_utilidad_mensual WHERE ano = @ano);
			SET @total := (SELECT sum(@va+ttv) FROM dual);
			UPDATE tesis_core.app_utilidad_mensual SET sep = @total WHERE id_utilidad_mensual = @id;
		ELSEIF @mes = 10 THEN
			SET @va := (SELECT oct FROM tesis_core.app_utilidad_mensual WHERE ano = @ano);
			SET @total := (SELECT sum(@va+ttv) FROM dual);
			UPDATE tesis_core.app_utilidad_mensual SET oct = @total WHERE id_utilidad_mensual = @id;
		ELSEIF @mes = 11 THEN
			SET @va := (SELECT nov FROM tesis_core.app_utilidad_mensual WHERE ano = @ano);
			SET @total := (SELECT sum(@va+ttv) FROM dual);
			UPDATE tesis_core.app_utilidad_mensual SET nov = @total WHERE id_utilidad_mensual = @id;
		ELSEIF @mes = 12 THEN
			SET @va := (SELECT dic FROM tesis_core.app_utilidad_mensual WHERE ano = @ano);
			SET @total := (SELECT sum(@va+ttv) FROM dual);
			UPDATE tesis_core.app_utilidad_mensual SET dic = @total WHERE id_utilidad_mensual = @id;
		END IF;
	END IF;
END;//
DELIMITER ;

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#