var limit = 0;

$(document).ready(function(){
	
	$("#id_producto").on('change', producto);
	$("#id_producto").on('change', producto_inventario);

	function producto(){
		var valor = $(this).val();
		$.ajax({
			data: { 'id': valor },
			url: '/ventas/registrar/producto_ajax/',
			type: 'get',
			success: function(data) {
				console.log(data);
				for (var i = 0; i < data.length; i++) {
					var unit = data[i].fields.precio_unitario;
				}
				//console.log(unit);
				if ($('#id_cliente').val().trim() !== "" && $('#id_producto').val().trim() !== "") {

					//$("#id_cantidad").removeAttr('disabled');
					$('#id_cantidad').on('keyup',function(){
						var cant = $(this).val();
						var res = parseFloat((((unit*50)*cant)*1.12)).toFixed(2);
						$('#id_total_venta').val(res);
						$("#id_form").submit(function(){
							$("#id_total_venta").removeAttr('disabled');
						});
					});

				};
			},
			error: function(x, e) {
				if (x.status == 500) {
					alert('Internel Server Error.');
				}
			}
		});
	}//function

	function producto_inventario(){
		var valor = $(this).val();
		$.ajax({
			data: { 'id_inv': valor },
			url: '/ventas/registrar/stock_ajax/',
			type: 'get',
			success: function(data) {
				console.log(data);
				for (var i = 0; i < data.length; i++) {
					limit = data[i].fields.cantidad_producto;
				}
				//console.log(limit);
				$('#d_cantidad').append('<p class="help-block">Los cantidad maxima dispinible es: '+limit+'</p>');
			},
			error: function(xhr,errmsg,err) {
				//console.log(xhr.status + ": " + xhr.responseText);
				console.log(err);
			}
		});
	}//function

});