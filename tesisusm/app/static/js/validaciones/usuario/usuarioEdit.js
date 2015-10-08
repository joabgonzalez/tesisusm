$(document).ready(function(){

	var regexName = /^[A-Za-zÁáÉéÍíÓóÚúÜüÑñçÇ'\s]{2,50}$/;
	var regexMail = /^([\da-z_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/;

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
	//CORREO ELECTRONICO
	var f_correo = false;
	$('#id_correo').tooltip({'trigger':'focus'});
	$('#id_correo').wrap('<div id="d_correo" class="has-feedback"> </div>');
	$('#d_correo').append('<span id="s_correo" class="form-control-feedback"></span>');
	$('#id_correo').focus(function(){
		$(this).keyup(function(){
			$('#d_correo').removeClass('has-success has-error');
			$('#s_correo').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(/^([1-9]{3})$/)) {
				$('#d_correo').addClass('has-success');
				$('#s_correo').addClass('glyphicon glyphicon-ok');
				f_correo = true;
			} else if ($(this).val() === '') {
				$('#d_correo').removeClass('has-success has-error');
				$('#s_correo').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_correo = false;
			} else {
				$('#d_correo').addClass('has-error');
				$('#s_correo').addClass('glyphicon glyphicon-remove');
				f_correo = false;
			}
			formValido();
		});
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//ROL
	var f_rol = false;
	$('#id_rol').wrap('<div id="d_rol" class="has-feedback"> </div>');
	$('#d_rol').append('<span id="s_rol" style="margin-right: 10px" class="form-control-feedback"></span>');
	$('#id_rol').change(function(){
		$('#d_rol').removeClass('has-success has-error');
		$('#s_rol').removeClass('glyphicon glyphicon-ok glyphicon-remove');
		if ($(this).val().trim() !== "") {
			$('#d_rol').addClass('has-success');
			$('#s_rol').addClass('glyphicon glyphicon-ok');
			f_rol = true;
		} else {
			$('#d_rol').addClass('has-error');
			$('#s_rol').addClass('glyphicon glyphicon-remove');
			f_rol = false;
		}
		formValido();
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//USUARIO ACTIVO
	$('#id_activo').change(function(){
		formValido();
	});
	
	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//VERIFICACION INICIAL
	if ($('#id_primer_nombre').val().match(regexName)) {
		$('#d_primer_nombre').addClass('has-success');
		$('#s_primer_nombre').addClass('glyphicon glyphicon-ok');
		f_primer_nombre = true
	}
	if ($('#id_segundo_nombre').val().match(regexName)) {
		$('#d_segundo_nombre').addClass('has-success');
		$('#s_segundo_nombre').addClass('glyphicon glyphicon-ok');
		f_segundo_nombre = true
	}
	if ($('#id_primer_apellido').val().match(regexName)) {
		$('#d_primer_apellido').addClass('has-success');
		$('#s_primer_apellido').addClass('glyphicon glyphicon-ok');
		f_primer_apellido = true;
	}
	if ($('#id_segundo_apellido').val().match(regexName)) {
		$('#d_segundo_apellidoo').addClass('has-success');
		$('#s_segundo_apellido').addClass('glyphicon glyphicon-ok');
		f_primer_apellido = true;
	}
	if ($('#id_correo').val().match(regexMail)) {
		$('#d_correo').addClass('has-success');
		$('#s_correo').addClass('glyphicon glyphicon-ok');
		f_correo = true;
	}
	if ($('#id_rol').val().trim() !== "") {
		$('#d_rol').addClass('has-success');
		$('#s_rol').addClass('glyphicon glyphicon-ok');
		f_rol = true;
	}

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//ACTIVA BOTON
	function formValido() {
		if ((f_primer_nombre === true) && (f_segundo_nombre === true) && (f_primer_apellido === true) && (f_segundo_apellido === true) && (f_correo === true) && (f_rol === true)) {
			$('#btnForm').removeClass('disabled');
			$('#btnForm').removeAttr('disabled','disabled');
		} else {
			$('#btnForm').addClass('disabled');
			$('#btnForm').attr('disabled','disabled');
		}
	}

});
