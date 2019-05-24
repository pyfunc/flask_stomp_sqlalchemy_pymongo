$(document).ready(function(){

$("#comprar").click(function(){
  var nome = $("#nome").val();
  var quantidade = $("#quantidade").val();
  //$.post("/activemq_enviar",
  $.post("/rabbit_enviar",
  {
    nome: nome,
    quantidade: quantidade
  },
  function(data, status){
    alert("Data: " + data + "\nStatus: " + status);
  });
});

});