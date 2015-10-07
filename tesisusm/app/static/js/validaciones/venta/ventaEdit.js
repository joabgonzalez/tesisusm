$(document).ready(function(){

	var regexCant = /^([\d]*)$/;

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//CANTIDAD
	var f_cantidad = false;
	$('#id_cantidad').numeric();
	$('#id_cantidad').tooltip({'trigger':'focus'});
	$('#id_cantidad').wrap('<div id="d_cantidad" class="has-feedback"> </div>');
	$('#d_cantidad').append('<span id="s_cantidad" class="form-control-feedback"></span>');
	$('#id_cantidad').focus(function(){
		$(this).keyup(function(){
			console.log(limit);
			$('#d_cantidad').removeClass('has-success has-error');
			$('#s_cantidad').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexCant) && $(this).val() <= limit) {
				$('#d_cantidad').addClass('has-success');
				$('#s_cantidad').addClass('glyphicon glyphicon-ok');
				f_cantidad = true;
			} else if ($(this).val() === '') {
				$('#d_cantidad').removeClass('has-success has-error');
				$('#s_cantidad').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_cantidad = false;
			} else {
				$('#d_cantidad').addClass('has-error');
				$('#s_cantidad').addClass('glyphicon glyphicon-remove');
				f_cantidad = false;
			}
			formValido();
		});
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//VERIFICACION INICIAL
	if ($(this).val().match(regexCant) && $(this).val() <= limit) {
		$('#d_cantidad').addClass('has-success');
		$('#s_cantidad').addClass('glyphicon glyphicon-ok');
		f_cantidad = true;
	}

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//ACTIVA BOTON
	function formValido() {
		if (f_cantidad === true) {
			$('#btnForm').removeClass('disabled');
			$('#btnForm').removeAttr('disabled','disabled');
		} else {
			$('#btnForm').addClass('disabled');
			$('#btnForm').attr('disabled','disabled');
		}
	}

});