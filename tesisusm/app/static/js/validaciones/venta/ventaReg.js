$(document).ready(function(){

	var regexCant = /^([\d]*)$/;

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//CLIENTE
	var f_cliente = false;
	$('#id_cliente').wrap('<div id="d_cliente" class="has-feedback"> </div>');
	$('#d_cliente').append('<span id="s_cliente" style="margin-right: 10px" class="form-control-feedback"></span>');
	$('#id_cliente').change(function(){
		$('#d_cliente').removeClass('has-success has-error');
		$('#s_cliente').removeClass('glyphicon glyphicon-ok glyphicon-remove');
		if ($(this).val().trim() !== "") {
			$('#d_cliente').addClass('has-success');
			$('#s_cliente').addClass('glyphicon glyphicon-ok');
			f_cliente = true;
		} else {
			$('#d_cliente').addClass('has-error');
			$('#s_cliente').addClass('glyphicon glyphicon-remove');
			f_cliente = false;
		}
		formValido();
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//PRODUCTO
	var f_producto = false;
	$('#id_producto').wrap('<div id="d_producto" class="has-feedback"> </div>');
	$('#d_producto').append('<span id="s_producto" style="margin-right: 10px" class="form-control-feedback"></span>');
	$('#id_producto').change(function(){
		$('#d_producto').removeClass('has-success has-error');
		$('#s_producto').removeClass('glyphicon glyphicon-ok glyphicon-remove');
		if ($(this).val().trim() !== "") {
			$('#d_producto').addClass('has-success');
			$('#s_producto').addClass('glyphicon glyphicon-ok');
			f_producto = true;
		} else {
			$('#d_producto').addClass('has-error');
			$('#s_producto').addClass('glyphicon glyphicon-remove');
			f_producto = false;
		}
		formValido();
	});

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
	//ACTIVA BOTON
	function formValido() {
		if ((f_cliente === true) && (f_producto === true) && (f_cantidad === true)) {
			$('#btnForm').removeClass('disabled');
			$('#btnForm').removeAttr('disabled','disabled');
		} else {
			$('#btnForm').addClass('disabled');
			$('#btnForm').attr('disabled','disabled');
		}
	}

});
