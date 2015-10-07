$(document).ready(function(){

	var regexCod = /^([Pp]{1}[Kk]{1}-[0-9]{4})$/;
	var regexName = /^[A-Za-zÁáÉéÍíÓóÚúÜüÑñ'\s]{2,50}$/;
	var regexDesc = /^[A-Za-zÁáÉéÍíÓóÚúÜüÑñ'"-_,\.\d\s]{4,100}$/;
	var regexP1 = /^([\d]*\.[\d]{1,8})$/;
	var regexP2 = /^([\d]*)$/;

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//CODIGO
	var f_codigo = false;
	$('#id_codigo').mask('PK-9999');
	$('#id_codigo').tooltip({'trigger':'focus'});
	$('#id_codigo').wrap('<div id="d_codigo" class="has-feedback"> </div>');
	$('#d_codigo').append('<span id="s_codigo" class="form-control-feedback"></span>');
	$('#id_codigo').focus(function(){
		$(this).keyup(function(){
			$('#d_codigo').removeClass('has-success has-error');
			$('#s_codigo').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexCod)) {
				$('#d_codigo').addClass('has-success has-feedback');
				$('#s_codigo').addClass('glyphicon glyphicon-ok form-control-feedback');
				f_codigo = true;
			} else if ($(this).val() === '') {
				$('#d_codigo').removeClass('has-success has-error');
				$('#s_codigo').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_codigo = false;
			} else {
				$('#d_codigo').addClass('has-error');
				$('#s_codigo').addClass('glyphicon glyphicon-remove');
				f_codigo = false;
			}
			formValido();
		});
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//NOMBRE DE PRODUCTO
	var f_producto = false;
	$('#id_producto').tooltip({'trigger':'focus'});
	$('#id_producto').wrap('<div id="d_producto" class="has-feedback"> </div>');
	$('#d_producto').append('<span id="s_producto" class="form-control-feedback"></span>');
	$('#id_producto').focus(function(){
		$(this).keyup(function(){
			$('#d_producto').removeClass('has-success has-error');
			$('#s_producto').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexName)) {
				$('#d_producto').addClass('has-success has-feedback');
				$('#s_producto').addClass('glyphicon glyphicon-ok form-control-feedback');
				f_producto = true;
			} else if ($(this).val() === '') {
				$('#d_producto').removeClass('has-success has-error');
				$('#s_producto').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_producto = false;
			} else {
				$('#d_producto').addClass('has-error');
				$('#s_producto').addClass('glyphicon glyphicon-remove');
				f_producto = false;
			}
			formValido();
		});
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//TIPO DE PRODUCTO
	var f_tipo_producto = false;
	$('#id_tipo_producto').wrap('<div id="d_tipo_producto" class="has-feedback"> </div>');
	$('#d_tipo_producto').append('<span id="s_tipo_producto" style="margin-right: 10px" class="form-control-feedback"></span>');
	$('#id_tipo_producto').change(function(){
		$('#d_tipo_producto').removeClass('has-success has-error');
		$('#s_tipo_producto').removeClass('glyphicon glyphicon-ok glyphicon-remove');
		if ($(this).val().trim() !== "") {
			$('#d_tipo_producto').addClass('has-success');
			$('#s_tipo_producto').addClass('glyphicon glyphicon-ok');
			f_tipo_producto = true;
		} else {
			$('#d_tipo_producto').addClass('has-error');
			$('#s_tipo_producto').addClass('glyphicon glyphicon-remove');
			f_tipo_producto = false;
		}
		formValido();
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//DESCRIPCION
	var f_descripcion = true;
	$('#id_descripcion').tooltip({'trigger':'focus'});
	$('#id_descripcion').wrap('<div id="d_descripcion" class="has-feedback"> </div>');
	$('#d_descripcion').append('<span id="s_descripcion" class="form-control-feedback"></span>');
	$('#id_descripcion').focus(function(){
		$(this).keyup(function(){
			$('#d_descripcion').removeClass('has-success has-error');
			$('#s_descripcion').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && $(this).val().match(regexName)) {
				$('#d_descripcion').addClass('has-success has-feedback');
				$('#s_descripcion').addClass('glyphicon glyphicon-ok form-control-feedback');
				f_descripcion = true;
			} else if ($(this).val() === '') {
				$('#d_descripcion').removeClass('has-success has-error');
				$('#s_descripcion').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_descripcion = true;
			} else {
				$('#d_descripcion').addClass('has-error');
				$('#s_descripcion').addClass('glyphicon glyphicon-remove');
				f_descripcion = false;
			}
			formValido();
		});
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//PRECIO UNITARIO
	var f_precio_unitario = false;
	$('#id_precio_unitario').numeric(",");
	$('#id_precio_unitario').tooltip({'trigger':'focus'});
	$('#id_precio_unitario').wrap('<div id="d_precio_unitario" class="has-feedback"> </div>');
	$('#d_precio_unitario').append('<span id="s_precio_unitario" class="form-control-feedback"></span>');
	$('#id_precio_unitario').focus(function(){
		$(this).keyup(function(){
			//console.log(parseFloat($(this).val()).toFixed(2));
			$('#d_precio_unitario').removeClass('has-success has-error');
			$('#s_precio_unitario').removeClass('glyphicon glyphicon-ok glyphicon-remove');
			if ($(this).val().length >= 1 && ($(this).val().match(regexP1) || $(this).val().match(regexP2))) {
				$('#d_precio_unitario').addClass('has-success has-feedback');
				$('#s_precio_unitario').addClass('glyphicon glyphicon-ok form-control-feedback');
				f_precio_unitario = true;
			} else if ($(this).val() === '') {
				$('#d_precio_unitario').removeClass('has-success has-error');
				$('#s_precio_unitario').removeClass('glyphicon glyphicon-ok glyphicon-remove');
				f_precio_unitario = false;
			} else {
				$('#d_precio_unitario').addClass('has-error');
				$('#s_precio_unitario').addClass('glyphicon glyphicon-remove');
				f_precio_unitario = false;
			}
			formValido();
		});
	});
	$('#id_precio_unitario').blur(function(){
		$(this).val(parseFloat($(this).val()).toFixed(2));
	});

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//VERIFICACION INICIAL
	if ($('#id_codigo').val().match(regexCod)) {
		$('#d_codigo').addClass('has-success has-feedback');
		$('#s_codigo').addClass('glyphicon glyphicon-ok form-control-feedback');
		f_codigo = true;
	}
	if ($('#id_producto').val().match(regexName)) {
		$('#d_producto').addClass('has-success has-feedback');
		$('#s_producto').addClass('glyphicon glyphicon-ok form-control-feedback');
		f_producto = true;
	}
	if ($('#id_tipo_producto').val().trim() !== "") {
		$('#d_tipo_producto').addClass('has-success');
		$('#s_tipo_producto').addClass('glyphicon glyphicon-ok');
		f_tipo_producto = true;
	}
	if ($('#id_descripcion').val().match(regexName)) {
		$('#d_descripcion').addClass('has-success has-feedback');
		$('#s_descripcion').addClass('glyphicon glyphicon-ok form-control-feedback');
		f_descripcion = true;
	}
	if ($('#id_precio_unitario').val().match(regexP1) || $(this).val().match(regexP2)) {
		$('#d_precio_unitario').addClass('has-success has-feedback');
		$('#s_precio_unitario').addClass('glyphicon glyphicon-ok form-control-feedback');
		f_precio_unitario = true;
	}

	//#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	//ACTIVA BOTON
	function formValido() {
		if ((f_codigo === true) && (f_producto === true) && (f_tipo_producto === true) && (f_descripcion === true) && (f_precio_unitario === true)) {
			$('#btnForm').removeClass('disabled');
			$('#btnForm').removeAttr('disabled','disabled');
		} else {
			$('#btnForm').addClass('disabled');
			$('#btnForm').attr('disabled','disabled');
		}
	}

});