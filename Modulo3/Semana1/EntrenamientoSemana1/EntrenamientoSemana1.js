console.log("Welcome to the interactive message system!");

let sum = 0;
let prom = 0;
let cont = 0
let notas = [];

let nombre = prompt("Input your name!");
let edad = prompt("Input your age!");
edad = parseInt(edad);

// Age validation
if (nombre == null || nombre == '') {
    alert('please input a valid name!')
} else if (isNaN(edad)) {
    alert("Invalid age input");
} else {
    
    if (edad < 0) {
        alert("the age must be a positive number");
    } else if (edad >= 18) {
        alert(`Congrats ${nombre}! you're an adult with ${edad} years!`);
    } else if (edad < 18) {
        alert(`Cheer up ${nombre}, you'll be an adult in no time!`);
    }

    let numNotas = prompt("How many grades are you going to add");
    console.log(typeof(numNotas));

    // Amount of grades validation
    if (isNaN(numNotas)) {
        alert("Invalid grades quantity input");
    } else if (numNotas < 0) {
        alert('Grades quantity must be positive');
    } else {
        numNotas = parseInt(numNotas);
    }

    // Grade input and validation
    for (let i=0;i<numNotas;i++) {

        let numero = prompt("Input your grade");

        if (isNaN(numero)){
            alert("Invalid grade input");
        } else if (numero < 0) {
            alert('Grades must be positive');
        } else {
            numero = parseFloat(numero);
            notas.push(numero);
        }
    }

    for (let nota of notas) {
        sum += nota;
        cont += 1;
    }

    prom = sum / cont;
    prom = parseFloat(prom);

    // Grades validation

    if (isNaN(prom)) {
        alert("There's no grades to average");
    } else {
        alert(`${nombre} you have a ${prom} GPA`);
    }


}
