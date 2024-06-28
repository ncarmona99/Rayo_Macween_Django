const rut = document.getElementById('rut');
const nombre = document.getElementById("nombre");
const appaterno = document.getElementById("appaterno");
const apmaterno = document.getElementById("apmaterno");
const edad = document.getElementById("edad");
const genero = document.getElementById("genero");
const celular = document.getElementById("celular");
const carta = document.getElementById("carta");

function validar(){
  if(rut.value.length > 10 || rut.value.length < 8 || rut.value.includes('-') == false || /[a-z]/i.test(rut.value) == true){
    alert('rut inválido, debe estar escribir en formato 99999999-9');
    console.log("No se respeta length de rut");
  }

  if(nombre.value.length > 50){
    alert('El nombre no puede superar 50 caracteres');
    console.log("No se respeta length de nombre");
  }

  if(appaterno.value.length > 50){
    alert('El apellido paterno no puede superar 50 caracteres');
    console.log("No se respeta length de apellido paterno");
  }

  if(apmaterno.value.length > 50){
    alert('El apellido materno no puede superar 50 caracteres');
    console.log("No se respeta length de apellido materno");
  }

  if(edad.value <= 0){
    alert('La edad no puede ser 0 ni un número negativo');
    console.log("La edad no puede ser 0 ni negativa");
  }

  if(genero.value == '0'){
    alert('Error: Debe seleccionar su género');
  }

  if(celular.value.length !== 9){
    alert('Error: el celular debe contener 9 dígitos');
  }

  if(rut.value.trim() === '' || nombre.value.trim() === '' || appaterno.value.trim() === '' || apmaterno.value.trim() === '' || edad.value.trim() === '' || celular.value.trim() === '' || carta.value.trim() === ''){
    alert('ERROR: Ningún campo puede quedar vacío')
  }
}