$(document).ready(function() {
    // Máscara para CPF/CNPJ
    $('input[name="documento"]').on('input', function () {
      var val = $(this).val().replace(/\D/g, '');
      if (val.length <= 11) {
        $(this).val(val.replace(/(\d{3})(\d{3})(\d{3})(\d{0,2})/, "$1.$2.$3-$4"));
      } else {
        $(this).val(val.replace(/^(\d{2})(\d{3})(\d{3})(\d{4})(\d{0,2})/, "$1.$2.$3/$4-$5"));
      }
    });
  
    // Buscar dados do CEP
    $('input[name="cep"]').on('blur', function () {
      var cep = $(this).val().replace(/\D/g, '');
      if (cep.length === 8) {
        $.getJSON(`https://viacep.com.br/ws/${cep}/json/`, function(data) {
          if (!("erro" in data)) {
            $('input[name="logradouro"]').val(data.logradouro);
            $('input[name="bairro"]').val(data.bairro);
            $('input[name="cidade"]').val(data.localidade);
            $('input[name="uf"]').val(data.uf);
            $('input[name="pais"]').val("Brasil");
          }
        });
      }
    });
  });
  