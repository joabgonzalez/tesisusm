$(document).ready(function(){

	var regexUser = /^[a-zA-Z0-9-_]{4,12}$/;
	var regexPass = /(^(?=.*[a-z])(?=.*[A-Z])(?=.*\d){6,20}.+$)/;
	var regexName = /^[A-Za-zÁáÉéÍíÓóÚúÜüÑñ'\s]{2,50}$/;
	var regexMail = /^([\da-z_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/;
	var valUsername = $('#id_username').val();
	var f_err = false;

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//USUARIO
	var f_username = false;
	$('#id_username').tooltip({'trigger':'focus'});
	$('#id_username').wrap('<div id="d_username" class="has-feedback"> </div>');
	$('#d_username').append('<span id="s_username" class="form-control-feedback"></span>');
	$('#id_username').focus(function(){
		$(this).keyup(function(){
			$('#d_username').removeClass('has-success has-error');
			$('#s_username').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexUser)) {
				if (f_err === true && $(this).val() === valUsername) {
					$('#d_username').addClass('has-error');
					$('#s_username').addClass('glyphicon glyphicon-remove');
					f_username = false;
				} else {
					$('#d_username').addClass('has-success');
					$('#s_username').addClass('glyphicon glyphicon-ok');
					f_username = true;
				}
			} else if ($(this).val() === '') {
				$('#d_username').removeClass('has-success has-error');
				$('#s_username').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_username = false;
			} else {
				$('#d_username').addClass('has-error');
				$('#s_username').addClass('glyphicon glyphicon-remove');
				f_username = false;
			}
			formValido();
		});
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//PASSWORD
	var f_password1 = false;
	$('#id_password1').tooltip({'trigger':'focus'});
	$('#id_password1').wrap('<div id="d_password1" class="has-feedback"> </div>');
	$('#d_password1').append('<span id="s_password1" class="form-control-feedback"></span>');
	$('#id_password1').focus(function(){
		$(this).keyup(function(){
			$('#d_password1').removeClass('has-success has-error ');
			$('#s_password1').removeClass('glyphicon glyphicon-ok glyphicon-remove ');
			if ($(this).val().length >= 6 && $(this).val().match(regexPass)) {
				$('#d_password1').addClass('has-success');
				$('#s_password1').addClass('glyphicon glyphicon-ok');
				f_password1 = true;
			} else if ($(this).val() === '') {
				$('#d_password1').removeClass('has-success has-error');
				$('#s_password1').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_password1 = false;
			} else {
				$('#d_password1').addClass('has-error');
				$('#s_password1').addClass('glyphicon glyphicon-remove');
				f_password1 = false;
			}
			formValido();
		});
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//CONFIRMACION PASSWORD
	var f_password2 = false;
	$('#id_password2').tooltip({'trigger':'focus'});
	$('#id_password2').wrap('<div id="d_password2" class="has-feedback"> </div>');
	$('#d_password2').append('<span id="s_password2" class="form-control-feedback"></span>');
	$('#id_password2').focus(function(){
		$(this).keyup(function(){
			$('#d_password2').removeClass('has-success has-error');
			$('#s_password2').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && ($(this).val() === $('#id_password1').val())) {
				$('#d_password2').addClass('has-success');
				$('#s_password2').addClass('glyphicon glyphicon-ok');
				f_password2 = true;
			} else if ($(this).val() === '') {
				$('#d_password2').removeClass('has-success has-error');
				$('#s_password2').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_password2 = false;
			} else {
				$('#d_password2').addClass('has-error');
				$('#s_password2').addClass('glyphicon glyphicon-remove');
				f_password2 = false;
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
	//CORREO ELECTRONICO
	var f_correo_electronico = false;
	$('#id_correo_electronico').tooltip({'trigger':'focus'});
	$('#id_correo_electronico').wrap('<div id="d_correo_electronico" class="has-feedback"> </div>');
	$('#d_correo_electronico').append('<span id="s_correo_electronico" class="form-control-feedback"></span>');
	$('#id_correo_electronico').focus(function(){
		$(this).keyup(function(){
			$('#d_correo_electronico').removeClass('has-success has-error');
			$('#s_correo_electronico').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexMail)) {
				$('#d_correo_electronico').addClass('has-success');
				$('#s_correo_electronico').addClass('glyphicon glyphicon-ok');
				f_correo_electronico = true;
			} else if ($(this).val() === '') {
				$('#d_correo_electronico').removeClass('has-success has-error');
				$('#s_correo_electronico').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_correo_electronico = false;
			} else {
				$('#d_correo_electronico').addClass('has-error');
				$('#s_correo_electronico').addClass('glyphicon glyphicon-remove');
				f_correo_electronico = false;
			}
			formValido();
		});
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//VERIFICACION INICIAL
	if ($('#id_username').val().match(regexUser)) {
		$('#d_username').addClass('has-success');
		$('#s_username').addClass('glyphicon glyphicon-ok');
		f_primer_nombre = true
	}
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
	if ($('#id_correo_electronico').val().match(regexMail)) {
		$('#d_correo_electronico').addClass('has-success');
		$('#s_correo_electronico').addClass('glyphicon glyphicon-ok');
		f_correo_electronico = true;
	}

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//VERIFICA ERROR
	if ($('#alertError').is(':visible')) {
		f_err = true;
		$('#d_username').removeClass('has-success has-error');
		$('#s_username').removeClass('glyphicon glyphicon-ok glyphicon-remove');
		$('#d_username').addClass('has-error');
		$('#s_username').addClass('glyphicon glyphicon-remove');
		f_username = false;
	}

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//ACTIVA BOTON
	function formValido() {
		if ((f_username === true) && (f_password1 === true) && (f_password2 === true) && (f_primer_nombre === true) && (f_segundo_nombre === true) && (f_primer_apellido === true) && (f_segundo_apellido === true) && (f_correo_electronico === true)) {
			$('#btnForm').removeClass('disabled');
			$('#btnForm').removeAttr('disabled','disabled');
		} else {
			$('#btnForm').addClass('disabled');
			$('#btnForm').attr('disabled','disabled');
		}
	}

});