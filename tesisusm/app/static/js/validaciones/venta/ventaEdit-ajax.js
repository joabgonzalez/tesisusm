var limit = 0;

$(document).ready(function(){

	var total = $("#id_cantidad").val();
	var c = 0;
	$("#id_cantidad").on('keyup', producto);
	$("#id_cantidad").on('keyup', producto_inventario);

	function producto(){
		var valor = $("#id_producto").val();
		$.ajax({
			data: { 'id': valor },
			url: '/ventas/registrar/producto_ajax/',
			type: 'get',
			success: function(data) {
				//console.log(data);
				for (var i = 0; i < data.length; i++) {
					var unit = data[i].fields.precio_unitario;
				}
				//console.log(unit);
				$('#id_cantidad').on('keyup',function(){
					var cant = $(this).val();
					var res = parseFloat((((unit*50)*cant)*1.12)).toFixed(2);
					$('#id_total_venta').val(res);
					$("#id_form").submit(function(){
						$("#id_total_venta").removeAttr('disabled');
					});
				});
			},
			error: function(xhr,errmsg,err) {
				//console.log(xhr.status + ": " + xhr.responseText);
				console.log(err);
			}
		});
	}//function

	function producto_inventario(){
		var valor = $("#id_producto").val();
		$.ajax({
			data: { 'id_inv': valor },
			url: '/ventas/registrar/stock_ajax/',
			type: 'get',
			success: function(data) {
				//console.log(data);
				for (var i = 0; i < data.length; i++) {
					limit = data[i].fields.cantidad_producto;
				}
				limit = parseInt(limit) + parseInt(total);
				c = c + 1;
				if (c == 1) {
					$('#d_cantidad').append('<p id="p_cantidad" class="help-block">Los cantidad maxima dispinible es: '+limit+'</p>');
				};
			},
			error: function(xhr,errmsg,err) {
				//console.log(xhr.status + ": " + xhr.responseText);
				console.log(err);
			}
		});
	}//function

});