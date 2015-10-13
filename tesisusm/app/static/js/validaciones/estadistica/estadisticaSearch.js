$(document).ready(function(){

	var regexAno = /^(20)\d{2}$/;

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//VENTA ANUAL
	var f_search_venta = true;
	$('#id_search_venta').mask('2099');
	$('#id_search_venta').tooltip({'trigger':'focus'});
	$('#id_search_venta').wrap('<div id="d_search_venta" class="has-feedback"> </div>');
	$('#d_search_venta').append('<span id="s_search_venta" class="form-control-feedback"></span>');
	$('#id_search_venta').focus(function(){
		$(this).keyup(function(){
			$('#d_search_venta').removeClass('has-success has-error');
			$('#s_search_venta').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexAno)) {
				$('#d_search_venta').addClass('has-success has-feedback');
				$('#s_search_venta').addClass('glyphicon glyphicon-ok form-control-feedback');
				f_search_venta = true;
			} else if ($(this).val() === '') {
				$('#d_search_venta').removeClass('has-success has-error');
				$('#s_search_venta').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_search_venta = false;
			} else {
				$('#d_search_venta').addClass('has-error');
				$('#s_search_venta').addClass('glyphicon glyphicon-remove');
				f_search_venta = false;
			}
			formValido();
		});
	});
	$('#id_search_venta').blur(function(){
		 if ($(this).val() === '') {
			$('#d_search_venta').removeClass('has-success has-error');
			$('#s_search_venta').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			f_search_venta = false;
		}
		formValido();
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//ACTIVA BOTON
	function formValido() {
		if (f_search_venta === true) {
			$('#btnVentaForm').removeClass('disabled');
			$('#btnVentaForm').removeAttr('disabled','disabled');
		} else {
			$('#btnVentaForm').addClass('disabled');
			$('#btnVentaForm').attr('disabled','disabled');
		}
	}

});