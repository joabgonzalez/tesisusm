$(document).ready(function(){

	var regexAno = /^(20)\d{2}$/;

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//VENTA ANUAL
	var f_ano = true;
	$('#id_ano').mask('2019');
	$('#id_ano').tooltip({'trigger':'focus'});
	$('#id_ano').wrap('<div id="d_ano" class="has-feedback"> </div>');
	$('#d_ano').append('<span id="s_ano" class="form-control-feedback"></span>');
	$('#id_ano').focus(function(){
		$(this).keyup(function(){
			$('#d_ano').removeClass('has-success has-error');
			$('#s_ano').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexAno) && $(this).val() === '2015' || $(this).val() === '2016' || $(this).val() === '2017' || $(this).val() === '2018' || $(this).val() === '2019') {
				$('#d_ano').addClass('has-success has-feedback');
				$('#s_ano').addClass('glyphicon glyphicon-ok form-control-feedback');
				f_ano = true;
			} else if ($(this).val() === '') {
				$('#d_ano').removeClass('has-success has-error');
				$('#s_ano').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_ano = false;
			} else {
				$('#d_ano').addClass('has-error');
				$('#s_ano').addClass('glyphicon glyphicon-remove');
				f_ano = false;
			}
			formValido();
		});
	});
	$('#id_ano').blur(function(){
		 if ($(this).val() === '') {
			$('#d_ano').removeClass('has-success has-error');
			$('#s_ano').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			f_ano = false;
		}
		formValido();
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//ACTIVA BOTON
	function formValido() {
		if (f_ano === true) {
			$('#btnVentaForm').removeClass('disabled');
			$('#btnVentaForm').removeAttr('disabled','disabled');
		} else {
			$('#btnVentaForm').addClass('disabled');
			$('#btnVentaForm').attr('disabled','disabled');
		}
	}

});