$(document).ready(function(){
    $("#cep_paciente").blur(function(){
        var cep = $(this).val().replace(/[^0-9]/g, '');
        if(cep !== ""){
            var url = 'http://cep.correiocontrol.com.br/'+cep+'.json';
            $.getJSON(url, function(json){
                $("#logradouro_paciente").val(json.logradouro);
                $("#bairro_paciente").val(json.bairro);
                $("#cidade_paciente").val(json.localidade);
                $("#uf_paciente").val(json.uf);
            });
        }
    });
});