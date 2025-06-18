// console.log("Bienvenido al Sistema interactivo de mensajes!");

// let arreglo = [];
// arreglo.push(1);
// arreglo.push(2);
// arreglo.push(3);
// arreglo.push(4);
// console.log(arreglo);

// arreglo.pop();

// for (i of arreglo) {
//     console.log(i);
// }

// let nombre = prompt("Ingresa tu nombre!");
// let edad = prompt("Ingresa tu edad!");
// edad = parseInt(edad);

// if (isNaN(edad)) {
//     console.error("La edad no es reconocible por el programa");
// } else if (edad >= 18) {
//     alert(`Felicidades ${nombre}! eres mayor de edad con ${edad} años!`);
// } else if (edad < 18) {
//     alert(`Animo ${nombre}, en unos años ya seras mayor de edad!`);
// }


let sum = 0;
let prom = 0;
let cont = 0
let notas = [];
let numNotas = 0

numNotas = prompt("Ingrese cuantas notas va a registrar");

if (isNaN(numNotas)) {
    console.error("el valor ingresado no es numero");
} else {
    numNotas = parseInt(numNotas)
}


for (let i=0;i<numNotas;i++) {

    let numero = prompt("Ingrese una nota");

    if (isNaN(numero)){
        console.error("la nota ingresada no es un numero");
    } else {
        numero = parseFloat(numero)
        notas.push(numero)
    }
    
}

for (let nota of notas) {
    sum += nota
    cont += 1
}

prom = sum / cont
prom = parseFloat(prom)

if (isNaN(prom)) {
    console.error("No hay valores para promediar");
}else {
    console.log(prom)
}

