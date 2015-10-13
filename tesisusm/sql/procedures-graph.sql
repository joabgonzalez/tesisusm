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

DELIMITER //
CREATE PROCEDURE gra_proyeccion (IN pano INTEGER)
BEGIN
	SET @x := (SELECT sum(substr(cast(pano AS CHAR),4)+1) FROM dual);
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	SET @y1 := (SELECT sum(ene+feb+mar+abr+may+jun+jul+ago+sep+oct+nov+dic) FROM app_utilidad_mensual WHERE ano = 2010);
	SET @y2 := (SELECT sum(ene+feb+mar+abr+may+jun+jul+ago+sep+oct+nov+dic) FROM app_utilidad_mensual WHERE ano = 2011);
	SET @y3 := (SELECT sum(ene+feb+mar+abr+may+jun+jul+ago+sep+oct+nov+dic) FROM app_utilidad_mensual WHERE ano = 2012);
	SET @y4 := (SELECT sum(ene+feb+mar+abr+may+jun+jul+ago+sep+oct+nov+dic) FROM app_utilidad_mensual WHERE ano = 2013);
	SET @y5 := (SELECT sum(ene+feb+mar+abr+may+jun+jul+ago+sep+oct+nov+dic) FROM app_utilidad_mensual WHERE ano = 2014);
	SET @sumy := (SELECT sum(@y1+@y2+@y3+@y4+@y5) FROM dual);
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	SET @xy1 := (SELECT sum((@y1)*1) FROM dual);
	SET @xy2 := (SELECT sum((@y2)*2) FROM dual);
	SET @xy3 := (SELECT sum((@y3)*3) FROM dual);
	SET @xy4 := (SELECT sum((@y4)*4) FROM dual);
	SET @xy5 := (SELECT sum((@y5)*5) FROM dual);
	SET @sumxy := (SELECT sum(@xy1+@xy2+@xy3+@xy4+@xy5) FROM dual);
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	SET @b := (SELECT sum(((5*@sumxy)-(15*@sumy))/50));
	SET @a := (SELECT sum((@sumy-(@b*15))/5));
	SET @c := (SELECT sum(@a+(@b*@x)));
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	SET @pene := (SELECT sum(@c*0.1014) FROM dual);
	SET @pfeb := (SELECT sum(@c*0.0660) FROM dual);
	SET @pmar := (SELECT sum(@c*0.0566) FROM dual);
	SET @pabr := (SELECT sum(@c*0.0605) FROM dual);
	SET @pmay := (SELECT sum(@c*0.0565) FROM dual);
	SET @pjun := (SELECT sum(@c*0.1268) FROM dual);
	SET @pjul := (SELECT sum(@c*0.0894) FROM dual);
	SET @pago := (SELECT sum(@c*0.0659) FROM dual);
	SET @psep := (SELECT sum(@c*0.0729) FROM dual);
	SET @poct := (SELECT sum(@c*0.0502) FROM dual);
	SET @pnov := (SELECT sum(@c*0.1459) FROM dual);
	SET @pdic := (SELECT sum(@c*0.1080) FROM dual);
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	INSERT INTO tesis_core.app_proyeccion_venta (ano,ene,feb,mar,abr,may,jun,jul,ago,sep,oct,nov,dic)
	VALUES (pano,@pene,@pfeb,@pmar,@pabr,@pmay,@pjun,@pjul,@pago,@psep,@poct,@pnov,@pdic);
END;//
DELIMITER ;