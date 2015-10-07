$(document).ready(function(){

	var regexCant = /^([\d]*)$/;

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//CANTIDAD DE BULTOS
	var f_cantidad_producto = false;
	$('#id_cantidad_producto').numeric();
	$('#id_cantidad_producto').tooltip({'trigger':'focus'});
	$('#id_cantidad_producto').wrap('<div id="d_cantidad_producto" class="has-feedback"> </div>');
	$('#d_cantidad_producto').append('<span id="s_cantidad_producto" class="form-control-feedback"></span>');
	$('#id_cantidad_producto').focus(function(){
		$(this).keyup(function(){
			//console.log(parseFloat($(this).val()).toFixed(2));
			$('#d_cantidad_producto').removeClass('has-success has-error');
			$('#s_cantidad_producto').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexCant)) {
				$('#d_cantidad_producto').addClass('has-success has-feedback');
				$('#s_cantidad_producto').addClass('glyphicon glyphicon-ok form-control-feedback');
				f_cantidad_producto = true;
			} else if ($(this).val() === '') {
				$('#d_cantidad_producto').removeClass('has-success has-error');
				$('#s_cantidad_producto').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_cantidad_producto = false;
			} else {
				$('#d_cantidad_producto').addClass('has-error');
				$('#s_cantidad_producto').addClass('glyphicon glyphicon-remove');
				f_cantidad_producto = false;
			}
			formValido();
		});
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//ACTIVA BOTON
	function formValido() {
		if (f_cantidad_producto === true) {
			$('#btnForm').removeClass('disabled');
			$('#btnForm').removeAttr('disabled','disabled');
		} else {
			$('#btnForm').addClass('disabled');
			$('#btnForm').attr('disabled','disabled');
		}
	}

});	