$(document).ready(function(){

$("#comprar").click(function(){
  var produto = $("#produto").val();
  var quantidade = $("#quantidade").val();
  $.post("/rabbit_enviar",
  {
    name: produto,
    quantity: quantidade
  },
  function(data, status){
    alert("Data: " + data + "\nStatus: " + status);
  });
});

});