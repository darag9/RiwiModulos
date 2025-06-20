let enviar = document.getElementById("enviar");
let mostrar = document.getElementById("mostrar");
let notas = [];
let sumaNotas = 0;

enviar.addEventListener("click", (i) => {

    let nota = parseFloat(document.getElementById("notas").value)

    if (isNaN(nota)) {
        estado.innerHTML = "Debes ingresar una nota valida"
    } else if (nota < 0) {
        estado.innerHTML = "La nota debe ser un numero positivo"
    } else {
        notas.push(nota);
        sumaNotas += nota;
        estado.innerHTML = "Nota Ingresada!"
    }

    console.log(nota);
    console.log(notas);
    
});

mostrar.addEventListener("click", (e) => {

    let promedio = sumaNotas / notas.length
    console.log(notas);
    console.log(promedio);

    let span = document.getElementById("prom");
    span.innerHTML = promedio

    let estado = document.getElementById("estado");
    
    if (promedio >= 3) {
        estado.innerHTML = "Aprobaste!"
    } else {
        estado.innerHTML = "Reprobaste :c"
    }
});