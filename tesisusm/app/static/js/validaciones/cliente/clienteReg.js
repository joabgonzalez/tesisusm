$(document).ready(function(){

	var regexRif = /^([JjVvEeGg]{1}-[0-9]{8}-[1-9]{1})$/;
	var regexName = /^([A-Za-zÁáÉéÍíÓóÚúÜüÑñ'"-,\d\s\.\/]{2,50})$/;
	var regexAdress = /^([A-Za-zÁáÉéÍíÓóÚúÜüÑñ#,-\.\d\s]{6,100})$/;
	var regexPhone = /^([0]{1}[24]{1}[0-9]{2}-[0-9]{7})$/;
	var regexFax = /^([0]{1}[2]{1}[0-9]{2}-[0-9]{7})$/;
	var regexMail = /^([\da-z_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/;
	var valRif = $('#id_rif').val();
	var f_err = false;

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//RIF
	var f_rif = false;
	$('#id_rif').mask('a-99999999-9');
	$('#id_rif').tooltip({'trigger':'focus'});
	$('#id_rif').wrap('<div id="d_rif" class="has-feedback"> </div>');
	$('#d_rif').append('<span id="s_rif" class="form-control-feedback"></span>');
	$('#id_rif').focus(function(){
		$(this).keyup(function(){
			$('#d_rif').removeClass('has-success has-error');
			$('#s_rif').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexRif)) {
				if (f_err === true && $(this).val() === valRif) {
					$('#d_rif').addClass('has-error');
					$('#s_rif').addClass('glyphicon glyphicon-remove');
					f_rif = false;
				} else {
					$('#d_rif').addClass('has-success');
					$('#s_rif').addClass('glyphicon glyphicon-ok');
					f_rif = true;
				}
			} else if ($(this).val() === '') {
				$('#d_rif').removeClass('has-success has-error');
				$('#s_rif').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_rif = false;
			} else {
				$('#d_rif').addClass('has-error');
				$('#s_rif').addClass('glyphicon glyphicon-remove');
				f_rif = false;
			}
			formValido();
		});
	});
	$('#id_rif').blur(function(){
		 if ($(this).val() === '') {
			$('#d_rif').removeClass('has-success has-error');
			$('#s_rif').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			f_rif = false;
		}
		formValido();
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//RAZON SOCIAL
	var f_cliente = false;
	$('#id_cliente').tooltip({'trigger':'focus'});
	$('#id_cliente').wrap('<div id="d_cliente" class="has-feedback"> </div>');
	$('#d_cliente').append('<span id="s_cliente" class="form-control-feedback"></span>');
	$('#id_cliente').focus(function(){
		$(this).keyup(function(){
			$('#d_cliente').removeClass('has-success has-error');
			$('#s_cliente').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexName)) {
				$('#d_cliente').addClass('has-success');
				$('#s_cliente').addClass('glyphicon glyphicon-ok');
				f_cliente = true;
			} else if ($(this).val() === '') {
				$('#d_cliente').removeClass('has-success has-error');
				$('#s_cliente').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_cliente = false;
			} else {
				$('#d_cliente').addClass('has-error');
				$('#s_cliente').addClass('glyphicon glyphicon-remove');
				f_cliente = false;
			}
			formValido();
		});
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
	//TELEFONO 1
	var f_telefono_1 = false;
	$('#id_telefono_1').mask('9999-9999999');
	$('#id_telefono_1').tooltip({'trigger':'focus'});
	$('#id_telefono_1').wrap('<div id="d_telefono_1" class="has-feedback"> </div>');
	$('#d_telefono_1').append('<span id="s_telefono_1" class="form-control-feedback"></span>');
	$('#id_telefono_1').focus(function(){
		$(this).keyup(function(){
			$('#d_telefono_1').removeClass('has-success has-error');
			$('#s_telefono_1').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexPhone) && ($(this).val() !== $('#id_telefono_2').val())) {
				$('#d_telefono_1').addClass('has-success has-feedback');
				$('#s_telefono_1').addClass('glyphicon glyphicon-ok form-control-feedback');
				f_telefono_1 = true;
			} else if ($(this).val() === '') {
				$('#d_telefono_1').removeClass('has-success has-error');
				$('#s_telefono_1').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_telefono_1 = false;
			} else {
				$('#d_telefono_1').addClass('has-error');
				$('#s_telefono_1').addClass('glyphicon glyphicon-remove');
				f_telefono_1 = false;
			}
			formValido();
		});
	});
	$('#id_telefono_1').blur(function(){
		 if ($(this).val() === '') {
			$('#d_telefono_1').removeClass('has-success has-error');
			$('#s_telefono_1').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			f_telefono_1 = false;
		}
		formValido();
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//TELEFONO 2
	var f_telefono_2 = true;
	$('#id_telefono_2').mask('9999-9999999');
	$('#id_telefono_2').tooltip({'trigger':'focus'});
	$('#id_telefono_2').wrap('<div id="d_telefono_2" class="has-feedback"> </div>');
	$('#d_telefono_2').append('<span id="s_telefono_2" class="form-control-feedback"></span>');
	$('#id_telefono_2').focus(function(){
		$(this).keyup(function(){
			$('#d_telefono_2').removeClass('has-success has-error');
			$('#s_telefono_2').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexPhone) && $(this).val() !== $('#id_telefono_1').val() && $(this).val() !== $('#id_fax').val()) {
				$('#d_telefono_2').addClass('has-success has-feedback');
				$('#s_telefono_2').addClass('glyphicon glyphicon-ok form-control-feedback');
				f_telefono_2 = true;
			} else if ($(this).val() === '') {
				$('#d_telefono_2').removeClass('has-success has-error');
				$('#s_telefono_2').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_telefono_2 = true;
			} else {
				$('#d_telefono_2').addClass('has-error');
				$('#s_telefono_2').addClass('glyphicon glyphicon-remove');
				f_telefono_2 = false;
			}
			formValido();
		});
	});
	$('#id_telefono_2').blur(function(){
		if ($(this).val() === '') {
			$('#d_telefono_2').removeClass('has-success has-error');
			$('#s_telefono_2').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			f_telefono_2 = true;
		}
		formValido();
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//FAX
	var f_fax = true;
	$('#id_fax').mask('9999-9999999');
	$('#id_fax').tooltip({'trigger':'focus'});
	$('#id_fax').wrap('<div id="d_fax" class="has-feedback"> </div>');
	$('#d_fax').append('<span id="s_fax" class="form-control-feedback"></span>');
	$('#id_fax').focus(function(){
		$(this).keyup(function(){
			$('#d_fax').removeClass('has-success has-error');
			$('#s_fax').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexFax) && ($(this).val() !== $('#id_telefono_2').val())) {
				$('#d_fax').addClass('has-success has-feedback');
				$('#s_fax').addClass('glyphicon glyphicon-ok form-control-feedback');
				f_fax = true;
			} else if ($(this).val() === '') {
				$('#d_fax').removeClass('has-success has-error');
				$('#s_fax').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_fax = true;
			} else {
				$('#d_fax').addClass('has-error');
				$('#s_fax').addClass('glyphicon glyphicon-remove');
				f_fax = false;
			}
			formValido();
		});
	});
	$('#id_fax').blur(function(){
		 if ($(this).val() === '') {
			$('#d_fax').removeClass('has-success has-error');
			$('#s_fax').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			f_fax = true;
		}
		formValido();
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
			if ($(this).val().length >= 1 && $(this).val().match(regexMail)) {
				$('#d_correo').addClass('has-success has-feedback');
				$('#s_correo').addClass('glyphicon glyphicon-ok form-control-feedback');
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
	//VERIFICACION INICIAL
	if ($('#id_rif').val().match(regexRif)) {
		$('#d_rif').addClass('has-success has-feedback');
		$('#s_rif').addClass('glyphicon glyphicon-ok form-control-feedback');
		f_rif = true;
	}
	if ($('#id_cliente').val().match(regexName)) {
		$('#d_cliente').addClass('has-success');
		$('#s_cliente').addClass('glyphicon glyphicon-ok');
		f_cliente = true;
	}
	if ($('#id_direccion').val().match(regexAdress)) {
		$('#d_direccion').addClass('has-success has-feedback');
		$('#s_direccion').addClass('glyphicon glyphicon-ok form-control-feedback');
		f_direccion = true;
	}
	if ($('#id_telefono_1').val().match(regexPhone)) {
		$('#d_telefono_1').addClass('has-success has-feedback');
		$('#s_telefono_1').addClass('glyphicon glyphicon-ok form-control-feedback');
		f_telefono_1 = true;
	}
	if ($('#id_telefono_2').val().match(regexPhone)) {
		$('#d_telefono_2').addClass('has-success has-feedback');
		$('#s_telefono_2').addClass('glyphicon glyphicon-ok form-control-feedback');
		f_telefono_2 = true;
	}
	if ($('#id_fax').val().match(regexFax)) {
		$('#d_fax').addClass('has-success has-feedback');
		$('#s_fax').addClass('glyphicon glyphicon-ok form-control-feedback');
		f_fax = true;
	}
	if ($('#id_correo').val().match(regexMail)) {
		$('#d_correo').addClass('has-success has-feedback');
		$('#s_correo').addClass('glyphicon glyphicon-ok form-control-feedback');
		f_correo = true;
	}

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//VERIFICA ERROR
	if ($('#alertError').is(':visible')) {
		f_err = true;
		$('#d_rif').removeClass('has-success has-error');
		$('#s_rif').removeClass('glyphicon glyphicon-ok glyphicon-remove');
		$('#d_rif').addClass('has-error');
		$('#s_rif').addClass('glyphicon glyphicon-remove');
		f_rif = false;
	}

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//ACTIVA BOTON
	function formValido() {
		if ((f_rif === true) && (f_cliente === true) && (f_direccion === true) && (f_telefono_1 === true) && (f_telefono_2 === true) && (f_fax === true) && (f_correo == true)) {
			$('#btnForm').removeClass('disabled');
			$('#btnForm').removeAttr('disabled','disabled');
		} else {
			$('#btnForm').addClass('disabled');
			$('#btnForm').attr('disabled','disabled');
		}
	}

});