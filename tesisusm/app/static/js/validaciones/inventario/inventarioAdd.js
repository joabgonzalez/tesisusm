$(document).ready(function(){

	var regexCant = /^([\d]*)$/;
	var actual = parseInt($('#id_cantidad_producto').val());

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//CANTIDAD DE PRODUCTO
	var f_nuevo = false;
	$('#id_nuevo').numeric();
	$('#id_nuevo').attr('maxlength',3);
	$('#id_nuevo').tooltip({'trigger':'focus'});
	$('#id_nuevo').wrap('<div id="d_nuevo" class="has-feedback"> </div>');
	$('#d_nuevo').append('<span id="s_nuevo" class="form-control-feedback"></span>');
	$('#id_nuevo').focus(function(){
		$(this).keyup(function(){
			var nuevo = parseInt($(this).val());
			$('#d_nuevo').removeClass('has-success has-error');
			$('#s_nuevo').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexCant) && parseInt($(this).val()) !== 0) {
				$('#d_nuevo').addClass('has-success has-feedback');
				$('#s_nuevo').addClass('glyphicon glyphicon-ok form-control-feedback');
				$('#id_cantidad_producto').val(actual+nuevo);
				f_nuevo = true;
			} else if ($(this).val() === '') {
				$('#d_nuevo').removeClass('has-success has-error');
				$('#s_nuevo').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				$('#id_cantidad_producto').val(actual);
				f_nuevo = false;
			} else {
				$('#d_nuevo').addClass('has-error');
				$('#s_nuevo').addClass('glyphicon glyphicon-remove');
				f_nuevo = false;
			}
			formValido();
		});
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//ACTIVA BOTON
	function formValido() {
		if (f_nuevo === true) {
			$('#btnForm').removeClass('disabled');
			$('#btnForm').removeAttr('disabled','disabled');
		} else {
			$('#btnForm').addClass('disabled');
			$('#btnForm').attr('disabled','disabled');
		}
	}

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//DESACTIVA CAMPOS
	$('#id_form').submit(function(){
		$('#id_cantidad_producto').removeAttr('disabled');
	});


});	