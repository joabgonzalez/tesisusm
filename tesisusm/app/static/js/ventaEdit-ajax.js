$(document).ready(function(){
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
					var res = unit*cant;
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
	}

	function producto_inventario(){
		var valor = $("#id_producto").val();
		$.ajax({
			data: { 'id_inv': valor },
			url: '/ventas/registrar/stock_ajax/',
			type: 'get',
			success: function(data) {
				//console.log(data);
				for (var i = 0; i < data.length; i++) {
					var limit = data[i].fields.cantidad_producto;
				}
				//console.log(limit);
				$('#id_cantidad').attr("max",limit);
			},
			error: function(xhr,errmsg,err) {
				//console.log(xhr.status + ": " + xhr.responseText);
				console.log(err);
			}
		});
	}

});