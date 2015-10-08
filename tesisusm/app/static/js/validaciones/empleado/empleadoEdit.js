$(document).ready(function(){

	var regexCed = /^([1-9]{1}[0-9]{3,7})$/;
	var regexName = /^[A-Za-zÁáÉéÍíÓóÚúÜüÑñ'\s]{2,50}$/;
	var regexPhone1 = /^([0]{1}[2]{1}[0-9]{2}[0-9]{7})$/;
	var regexPhone2 = /^([0]{1}[4]{1}[0-9]{2}[0-9]{7})$/;
	var regexFecha = /^(0?[1-9]|[12][0-9]|3[01])[\/](0?[1-9]|1[012])[\/](19|20)\d{2}$/;
	var regexAdress = /^([A-Za-zÁáÉéÍíÓóÚúÜüÑñ#,-\.\d\s]{6,100})$/;
	var regexMail = /^([\da-z_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/;
	var regexS1 = /^([\d]*\.[\d]{1,8})$/;
	var regexS2 = /^([\d]*)$/;

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//CEDULA
	var f_cedula = false;
	$('#id_cedula').numeric();
	$('#id_cedula').attr('maxlength', '8');
	$('#id_cedula').tooltip({'trigger':'focus'});
	$('#id_cedula').wrap('<div id="d_cedula" class="has-feedback"> </div>');
	$('#d_cedula').append('<span id="s_cedula" class="form-control-feedback"></span>');
	$('#id_cedula').focus(function(){
		$(this).keyup(function(){
			$('#d_cedula').removeClass('has-success has-error');
			$('#s_cedula').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexCed)) {
				$('#d_cedula').addClass('has-success has-feedback');
				$('#s_cedula').addClass('glyphicon glyphicon-ok form-control-feedback');
				f_cedula = true;
			} else if ($(this).val() === '') {
				$('#d_cedula').removeClass('has-success has-error');
				$('#s_cedula').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_cedula = false;
			} else {
				$('#d_cedula').addClass('has-error');
				$('#s_cedula').addClass('glyphicon glyphicon-remove');
				f_cedula = false;
			}
			formValido();
		});
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//PRIMER NOMBRE
	var f_primer_nombre = false;
	$('#id_primer_nombre').tooltip({'trigger':'focus'});
	$('#id_primer_nombre').wrap('<div id="d_primer_nombre" class="has-feedback"> </div>');
	$('#d_primer_nombre').append('<span id="s_primer_nombre" class="form-control-feedback"></span>');
	$('#id_primer_nombre').focus(function(){
		$(this).keyup(function(){
			$('#d_primer_nombre').removeClass('has-success has-error');
			$('#s_primer_nombre').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexName)) {
				$('#d_primer_nombre').addClass('has-success');
				$('#s_primer_nombre').addClass('glyphicon glyphicon-ok');
				f_primer_nombre = true;
			} else if ($(this).val() === '') {
				$('#d_primer_nombre').removeClass('has-success has-error');
				$('#s_primer_nombre').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_primer_nombre = false;
			} else {
				$('#d_primer_nombre').addClass('has-error');
				$('#s_primer_nombre').addClass('glyphicon glyphicon-remove');
				f_primer_nombre = false;
			}
			formValido();
		});
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//SEGUNDO NOMBRE
	var f_segundo_nombre = true;
	$('#id_segundo_nombre').tooltip({'trigger':'focus'});
	$('#id_segundo_nombre').wrap('<div id="d_segundo_nombre" class="has-feedback"> </div>');
	$('#d_segundo_nombre').append('<span id="s_segundo_nombre" class="form-control-feedback"></span>');
	$('#id_segundo_nombre').focus(function(){
		$(this).keyup(function(){
			$('#d_segundo_nombre').removeClass('has-success has-error');
			$('#s_segundo_nombre').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexName)) {
				$('#d_segundo_nombre').addClass('has-success');
				$('#s_segundo_nombre').addClass('glyphicon glyphicon-ok');
				f_segundo_nombre = true;
			} else if ($(this).val() === '') {
				$('#d_segundo_nombre').removeClass('has-success has-error');
				$('#s_segundo_nombre').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_segundo_nombre = true;
			} else {
				$('#d_segundo_nombre').addClass('has-error');
				$('#s_segundo_nombre').addClass('glyphicon glyphicon-remove');
				f_segundo_nombre = false;
			}
			formValido();
		});
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//PRIMER APELLIDO
	var f_primer_apellido = false;
	$('#id_primer_apellido').tooltip({'trigger':'focus'});
	$('#id_primer_apellido').wrap('<div id="d_primer_apellido" class="has-feedback"> </div>');
	$('#d_primer_apellido').append('<span id="s_primer_apellido" class="form-control-feedback"></span>');
	$('#id_primer_apellido').focus(function(){
		$(this).keyup(function(){
			$('#d_primer_apellido').removeClass('has-success has-error');
			$('#s_primer_apellido').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexName)) {
				$('#d_primer_apellido').addClass('has-success');
				$('#s_primer_apellido').addClass('glyphicon glyphicon-ok');
				f_primer_apellido = true;
			} else if ($(this).val() === '') {
				$('#d_primer_apellido').removeClass('has-success has-error');
				$('#s_primer_apellido').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_primer_apellido = false;
			} else {
				$('#d_primer_apellido').addClass('has-error');
				$('#s_primer_apellido').addClass('glyphicon glyphicon-remove');
				f_primer_apellido = false;
			}
			formValido();
		});
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//SEGUNDO APELLIDO
	var f_segundo_apellido = true;
	$('#id_segundo_apellido').tooltip({'trigger':'focus'});
	$('#id_segundo_apellido').wrap('<div id="d_segundo_apellido" class="has-feedback"> </div>');
	$('#d_segundo_apellido').append('<span id="s_segundo_apellido" class="form-control-feedback"></span>');
	$('#id_segundo_apellido').focus(function(){
		$(this).keyup(function(){
			$('#d_segundo_apellido').removeClass('has-success has-error');
			$('#s_segundo_apellido').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexName)) {
				$('#d_segundo_apellido').addClass('has-success');
				$('#s_segundo_apellido').addClass('glyphicon glyphicon-ok');
				f_segundo_apellido = true;
			} else if ($(this).val() === '') {
				$('#d_segundo_apellido').removeClass('has-success has-error');
				$('#s_segundo_apellido').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_segundo_apellido = true;
			} else {
				$('#d_segundo_apellido').addClass('has-error');
				$('#s_segundo_apellido').addClass('glyphicon glyphicon-remove');
				f_segundo_apellido = false;
			}
			formValido();
		});
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//TELEFONO LOCAL
	var f_telefono_local = true;
	$('#id_telefono_local').numeric();
	$('#id_telefono_local').tooltip({'trigger':'focus'});
	$('#id_telefono_local').wrap('<div id="d_telefono_local" class="has-feedback"> </div>');
	$('#d_telefono_local').append('<span id="s_telefono_local" class="form-control-feedback"></span>');
	$('#id_telefono_local').focus(function(){
		$(this).keyup(function(){
			$('#d_telefono_local').removeClass('has-success has-error');
			$('#s_telefono_local').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexPhone1)) {
				$('#d_telefono_local').addClass('has-success has-feedback');
				$('#s_telefono_local').addClass('glyphicon glyphicon-ok form-control-feedback');
				f_telefono_local = true;
			} else if ($(this).val() === '') {
				$('#d_telefono_local').removeClass('has-success has-error');
				$('#s_telefono_local').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_telefono_local = true;
			} else {
				$('#d_telefono_local').addClass('has-error');
				$('#s_telefono_local').addClass('glyphicon glyphicon-remove');
				f_telefono_local = false;
			}
			formValido();
		});
	});
	$('#id_telefono_local').blur(function(){
		 if ($(this).val() === '') {
			$('#d_telefono_local').removeClass('has-success has-error');
			$('#s_telefono_local').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			f_telefono_local = true;
		}
		formValido();
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//TELEFONO CELULAR
	var f_telefono_celular = false;
	$('#id_telefono_celular').numeric();
	$('#id_telefono_celular').tooltip({'trigger':'focus'});
	$('#id_telefono_celular').wrap('<div id="d_telefono_celular" class="has-feedback"> </div>');
	$('#d_telefono_celular').append('<span id="s_telefono_celular" class="form-control-feedback"></span>');
	$('#id_telefono_celular').focus(function(){
		$(this).keyup(function(){
			$('#d_telefono_celular').removeClass('has-success has-error');
			$('#s_telefono_celular').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if($(this).val().length >= 1 && $(this).val().match(regexPhone2)) {
				$('#d_telefono_celular').addClass('has-success has-feedback');
				$('#s_telefono_celular').addClass('glyphicon glyphicon-ok form-control-feedback');
				f_telefono_celular = true;
			} else if ($(this).val() === '') {
				$('#d_telefono_celular').removeClass('has-success has-error');
				$('#s_telefono_celular').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_telefono_celular = false;
			} else {
				$('#d_telefono_celular').addClass('has-error');
				$('#s_telefono_celular').addClass('glyphicon glyphicon-remove');
				f_telefono_celular = false;
			}
			formValido();
		});
	});
	$('#id_telefono_celular').blur(function(){
		 if ($(this).val() === '') {
			$('#d_telefono_celular').removeClass('has-success has-error');
			$('#s_telefono_celular').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			f_telefono_celular = false;
		}
		formValido();
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//FECHA DE NACIMIENTO
	var f_fecha_nacimiento = false;
	$('#id_fecha_nacimiento').mask('99/99/9999');
	$('#id_fecha_nacimiento').tooltip({'trigger':'focus'});
	$('#id_fecha_nacimiento').wrap('<div id="d_fecha_nacimiento" class="has-feedback"> </div>');
	$('#d_fecha_nacimiento').append('<span id="s_fecha_nacimiento" class="form-control-feedback"></span>');
	$('#id_fecha_nacimiento').focus(function(){
		$(this).keyup(function(){
			$('#d_fecha_nacimiento').removeClass('has-success has-error');
			$('#s_fecha_nacimiento').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexFecha)) {
				$('#d_fecha_nacimiento').addClass('has-success has-feedback');
				$('#s_fecha_nacimiento').addClass('glyphicon glyphicon-ok form-control-feedback');
				f_fecha_nacimiento = true;
			} else if ($(this).val() === '') {
				$('#d_fecha_nacimiento').removeClass('has-success has-error');
				$('#s_fecha_nacimiento').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_fecha_nacimiento = false;
			} else {
				$('#d_fecha_nacimiento').addClass('has-error');
				$('#s_fecha_nacimiento').addClass('glyphicon glyphicon-remove');
				f_fecha_nacimiento = false;
			}
			formValido();
		});
	});
	$('#id_fecha_nacimiento').blur(function(){
		 if ($(this).val() === '') {
			$('#d_fecha_nacimiento').removeClass('has-success has-error');
			$('#s_fecha_nacimiento').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			f_fecha_nacimiento = false;
		}
		formValido();
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//DIRECCION
	var f_direccion = false;
	$('#id_direccion').tooltip({'trigger':'focus'});
	$('#id_direccion').wrap('<div id="d_direccion" class="has-feedback"> </div>');
	$('#d_direccion').append('<span id="s_direccion" class="form-control-feedback"></span>');
	$('#id_direccion').focus(function(){
		$(this).keyup(function(){
			$('#d_direccion').removeClass('has-success has-error');
			$('#s_direccion').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexAdress)) {
				$('#d_direccion').addClass('has-success has-feedback');
				$('#s_direccion').addClass('glyphicon glyphicon-ok form-control-feedback');
				f_direccion = true;
			} else if ($(this).val() === '') {
				$('#d_direccion').removeClass('has-success has-error');
				$('#s_direccion').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_direccion = false;
			} else {
				$('#d_direccion').addClass('has-error');
				$('#s_direccion').addClass('glyphicon glyphicon-remove');
				f_direccion = false;
			}
			formValido();
		});
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//CORREO ELECTRONICO PERSONAL
	var f_correo_personal = false;
	$('#id_correo_personal').tooltip({'trigger':'focus'});
	$('#id_correo_personal').wrap('<div id="d_correo_personal" class="has-feedback"> </div>');
	$('#d_correo_personal').append('<span id="s_correo_personal" class="form-control-feedback"></span>');
	$('#id_correo_personal').focus(function(){
		$(this).keyup(function(){
			$('#d_correo_personal').removeClass('has-success has-error');
			$('#s_correo_personal').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexMail)) {
				$('#d_correo_personal').addClass('has-success has-feedback');
				$('#s_correo_personal').addClass('glyphicon glyphicon-ok form-control-feedback');
				f_correo_personal = true;
			} else if ($(this).val() === '') {
				$('#d_correo_personal').removeClass('has-success has-error');
				$('#s_correo_personal').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_correo_personal = false;
			} else {
				$('#d_correo_personal').addClass('has-error');
				$('#s_correo_personal').addClass('glyphicon glyphicon-remove');
				f_correo_personal = false;
			}
			formValido();
		});
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//CORREO ELECTRONICO COORPORATIVO
	var f_correo_corporativo = true;
	$('#id_correo_corporativo').tooltip({'trigger':'focus'});
	$('#id_correo_corporativo').wrap('<div id="d_correo_corporativo" class="has-feedback"> </div>');
	$('#d_correo_corporativo').append('<span id="s_correo_corporativo" class="form-control-feedback"></span>');
	$('#id_correo_corporativo').focus(function(){
		$(this).keyup(function(){
			$('#d_correo_corporativo').removeClass('has-success has-error');
			$('#s_correo_corporativo').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexMail)) {
				$('#d_correo_corporativo').addClass('has-success has-feedback');
				$('#s_correo_corporativo').addClass('glyphicon glyphicon-ok form-control-feedback');
				f_correo_corporativo = true;
			} else if ($(this).val() === '') {
				$('#d_correo_corporativo').removeClass('has-success has-error');
				$('#s_correo_corporativo').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_correo_corporativo = true;
			} else {
				$('#d_correo_corporativo').addClass('has-error');
				$('#s_correo_corporativo').addClass('glyphicon glyphicon-remove');
				f_correo_corporativo = false;
			}
			formValido();
		});
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//SUELDO
	var f_sueldo = false;
	$('#id_sueldo').numeric(",");
	$('#id_sueldo').tooltip({'trigger':'focus'});
	$('#id_sueldo').wrap('<div id="d_sueldo" class="has-feedback"> </div>');
	$('#d_sueldo').append('<span id="s_sueldo" class="form-control-feedback"></span>');
	$('#id_sueldo').focus(function(){
		$(this).keyup(function(){
			//console.log(parseFloat($(this).val()).toFixed(2));
			$('#d_sueldo').removeClass('has-success has-error');
			$('#s_sueldo').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && ($(this).val().match(regexS1) || $(this).val().match(regexS2))) {
				$('#d_sueldo').addClass('has-success has-feedback');
				$('#s_sueldo').addClass('glyphicon glyphicon-ok form-control-feedback');
				f_sueldo = true;
			} else if ($(this).val() === '') {
				$('#d_sueldo').removeClass('has-success has-error');
				$('#s_sueldo').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_sueldo = false;
			} else {
				$('#d_sueldo').addClass('has-error');
				$('#s_sueldo').addClass('glyphicon glyphicon-remove');
				f_sueldo = false;
			}
			formValido();
		});
	});
	$('#id_sueldo').blur(function(){
		$(this).val(parseFloat($(this).val()).toFixed(2));
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//CARGO
	var f_cargo = false;
	//$("#id_cargo option[value='']").remove();
	$('#id_cargo').wrap('<div id="d_cargo" class="has-feedback"> </div>');
	$('#d_cargo').append('<span id="s_cargo" style="margin-right: 10px" class="form-control-feedback"></span>');
	$('#id_cargo').change(function(){
		$('#d_cargo').removeClass('has-success has-error');
		$('#s_cargo').removeClass('glyphicon glyphicon-ok glyphicon-remove');
		if ($(this).val().trim() !== "") {
			$('#d_cargo').addClass('has-success');
			$('#s_cargo').addClass('glyphicon glyphicon-ok');
			f_cargo = true;
		} else {
			$('#d_cargo').addClass('has-error');
			$('#s_cargo').addClass('glyphicon glyphicon-remove');
			f_cargo = false;
		}
		formValido();
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//TIPO DE EMPLEADO
	var f_tipo_empleado = false;
	//$("#id_tipo_empleado option[value='']").remove();
	$('#id_tipo_empleado').wrap('<div id="d_tipo_empleado" class="has-feedback"> </div>');
	$('#d_tipo_empleado').append('<span id="s_tipo_empleado" style="margin-right: 10px" class="form-control-feedback"></span>');
	$('#id_tipo_empleado').change(function(){
		$('#d_tipo_empleado').removeClass('has-success has-error');
		$('#s_tipo_empleado').removeClass('glyphicon glyphicon-ok glyphicon-remove');
		if ($(this).val().trim() !== "") {
			$('#d_tipo_empleado').addClass('has-success');
			$('#s_tipo_empleado').addClass('glyphicon glyphicon-ok');
			f_tipo_empleado = true;
		} else {
			$('#d_tipo_empleado').addClass('has-error');
			$('#s_tipo_empleado').addClass('glyphicon glyphicon-remove');
			f_tipo_empleado = false;
		}
		formValido();
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//FECHA DE INGRESO
	var f_fecha_ingreso = false;
	$('#id_fecha_ingreso').mask('99/99/9999');
	$('#id_fecha_ingreso').tooltip({'trigger':'focus'});
	$('#id_fecha_ingreso').wrap('<div id="d_fecha_ingreso" class="has-feedback"> </div>');
	$('#d_fecha_ingreso').append('<span id="s_fecha_ingreso" class="form-control-feedback"></span>');
	$('#id_fecha_ingreso').focus(function(){
		$(this).keyup(function(){
			$('#d_fecha_ingreso').removeClass('has-success has-error');
			$('#s_fecha_ingreso').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexFecha)) {
				$('#d_fecha_ingreso').addClass('has-success has-feedback');
				$('#s_fecha_ingreso').addClass('glyphicon glyphicon-ok form-control-feedback');
				f_fecha_ingreso = true;
			} else if ($(this).val() === '') {
				$('#d_fecha_ingreso').removeClass('has-success has-error');
				$('#s_fecha_ingreso').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_fecha_ingreso = false;
			} else {
				$('#d_fecha_ingreso').addClass('has-error');
				$('#s_fecha_ingreso').addClass('glyphicon glyphicon-remove');
				f_fecha_ingreso = false;
			}
			formValido();
		});
	});
	$('#id_fecha_ingreso').blur(function(){
		 if ($(this).val() === '') {
			$('#d_fecha_ingreso').removeClass('has-success has-error');
			$('#s_fecha_ingreso').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			f_fecha_ingreso = false;
		}
		formValido();
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//FECHA DE EGRESO
	var f_fecha_egreso = true;
	$('#id_fecha_egreso').mask('99/99/9999');
	$('#id_fecha_egreso').tooltip({'trigger':'focus'});
	$('#id_fecha_egreso').wrap('<div id="d_fecha_egreso" class="has-feedback"> </div>');
	$('#d_fecha_egreso').append('<span id="s_fecha_egreso" class="form-control-feedback"></span>');
	$('#id_fecha_egreso').focus(function(){
		$(this).keyup(function(){
			$('#d_fecha_egreso').removeClass('has-success has-error');
			$('#s_fecha_egreso').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexFecha)) {
				$('#d_fecha_egreso').addClass('has-success has-feedback');
				$('#s_fecha_egreso').addClass('glyphicon glyphicon-ok form-control-feedback');
				f_fecha_egreso = true;
			} else if ($(this).val() === '') {
				$('#d_fecha_egreso').removeClass('has-success has-error');
				$('#s_fecha_egreso').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_fecha_egreso = true;
			} else {
				$('#d_fecha_egreso').addClass('has-error');
				$('#s_fecha_egreso').addClass('glyphicon glyphicon-remove');
				f_fecha_egreso = false;
			}
			formValido();
		});
	});
	$('#id_fecha_egreso').blur(function(){
		 if ($(this).val() === '') {
			$('#d_fecha_egreso').removeClass('has-success has-error');
			$('#s_fecha_egreso').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			f_fecha_egreso = true;
		}
		formValido();
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//VERIFICACION INICIAL
	if ($('#id_cedula').val().match(regexCed)) {
		$('#d_cedula').addClass('has-success has-feedback');
		$('#s_cedula').addClass('glyphicon glyphicon-ok form-control-feedback');
		f_cedula = true;
	}
	if ($('#id_primer_nombre').val().match(regexName)) {
		$('#d_primer_nombre').addClass('has-success');
		$('#s_primer_nombre').addClass('glyphicon glyphicon-ok');
		f_primer_nombre = true;
	}
	if ($('#id_segundo_nombre').val().match(regexName)) {
		$('#d_segundo_nombre').addClass('has-success');
		$('#s_segundo_nombre').addClass('glyphicon glyphicon-ok');
		f_segundo_nombre = true;
	}
	if ($('#id_primer_apellido').val().match(regexName)) {
		$('#d_primer_apellido').addClass('has-success');
		$('#s_primer_apellido').addClass('glyphicon glyphicon-ok');
		f_primer_apellido = true;
	}
	if ($('#id_segundo_apellido').val().match(regexName)) {
		$('#d_segundo_apellido').addClass('has-success');
		$('#s_segundo_apellido').addClass('glyphicon glyphicon-ok');
		f_segundo_apellido = true;
	}
	if ($('#id_telefono_local').val().match(regexPhone1)) {
		$('#d_telefono_local').addClass('has-success has-feedback');
		$('#s_telefono_local').addClass('glyphicon glyphicon-ok form-control-feedback');
		f_telefono_local = true;
	}
	if($('#id_telefono_celular').val().match(regexPhone2)) {
		$('#d_telefono_celular').addClass('has-success has-feedback');
		$('#s_telefono_celular').addClass('glyphicon glyphicon-ok form-control-feedback');
		f_telefono_celular = true;
	}
	if ($('#id_fecha_nacimiento').val().match(regexFecha)) {
		$('#d_fecha_nacimiento').addClass('has-success has-feedback');
		$('#s_fecha_nacimiento').addClass('glyphicon glyphicon-ok form-control-feedback');
		f_fecha_nacimiento = true;
	}
	if ($('#id_direccion').val().match(regexAdress)) {
		$('#d_direccion').addClass('has-success has-feedback');
		$('#s_direccion').addClass('glyphicon glyphicon-ok form-control-feedback');
		f_direccion = true;
	}
	if ($('#id_correo_personal').val().match(regexMail)) {
		$('#d_correo_personal').addClass('has-success has-feedback');
		$('#s_correo_personal').addClass('glyphicon glyphicon-ok form-control-feedback');
		f_correo_personal = true;
	}
	if ($('#id_correo_corporativo').val().match(regexMail)) {
		$('#d_correo_corporativo').addClass('has-success has-feedback');
		$('#s_correo_corporativo').addClass('glyphicon glyphicon-ok form-control-feedback');
		f_correo_corporativo = true;
	}
	if ($('#id_sueldo').val().match(regexS1) || $('#id_sueldo').val().match(regexS2)) {
		$('#d_sueldo').addClass('has-success has-feedback');
		$('#s_sueldo').addClass('glyphicon glyphicon-ok form-control-feedback');
		f_sueldo = true;
	}
	if ($('#id_cargo').val().trim() !== "") {
		$('#d_cargo').addClass('has-success');
		$('#s_cargo').addClass('glyphicon glyphicon-ok');
		f_cargo = true;
	}
	if ($('#id_tipo_empleado').val().trim() !== "") {
		$('#d_tipo_empleado').addClass('has-success');
		$('#s_tipo_empleado').addClass('glyphicon glyphicon-ok');
		f_tipo_empleado = true;
	}
	if ($('#id_fecha_ingreso').val().match(regexFecha)) {
		$('#d_fecha_ingreso').addClass('has-success has-feedback');
		$('#s_fecha_ingreso').addClass('glyphicon glyphicon-ok form-control-feedback');
		f_fecha_ingreso = true;
	}
	if ($('#id_fecha_egreso').val().match(regexFecha)) {
		$('#d_fecha_egreso').addClass('has-success has-feedback');
		$('#s_fecha_egreso').addClass('glyphicon glyphicon-ok form-control-feedback');
		f_fecha_egreso = true;
	}

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//ACTIVA BOTON
	function formValido() {
		if ((f_cedula === true) && (f_primer_nombre === true) && (f_segundo_nombre === true) && (f_primer_apellido === true) && (f_segundo_apellido === true) && (f_telefono_local === true) && (f_telefono_celular === true) && (f_fecha_nacimiento === true) && (f_direccion === true) && (f_correo_personal === true) && (f_correo_corporativo === true) && (f_sueldo === true) && (f_cargo === true) && (f_tipo_empleado === true) && (f_fecha_ingreso === true) && (f_fecha_egreso === true)) {
			$('#btnForm').removeClass('disabled');
			$('#btnForm').removeAttr('disabled','disabled');
		} else {
			$('#btnForm').addClass('disabled');
			$('#btnForm').attr('disabled','disabled');
		}
	}

});