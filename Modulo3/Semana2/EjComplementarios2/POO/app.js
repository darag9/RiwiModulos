//objetos

const persona = {
    nombre: "Daniel",
    edad: 25,
    ciudad: "Medellin",
    skills: {
        "uno": "Python",
        "dos": "HTML",
        "tres": "CSS",
    },
};

console.log(persona.nombre);

//Desestructuracion de objetos

const { nombre:nombreObject, barrio="belen" } = persona

console.log(nombreObject);
console.log(barrio);

//Desestructuracion de la desestructuracion del objeto persona


console.log(persona.skills.uno);

const {uno, dos, tres} = persona.skills

console.log(dos);

//desestructurar un arreglo

const persona2 = {
    nombre: "Daniel",
    apellido: "Ramirez",
    edad: 25,
    ciudad: "Medellin",
    skills: ["HTML", "CSS", "Python"]
};

const {nombre, apellido, edad, ciudad, skills} = persona2

console.log(persona2.skills);
console.log(persona2.skills[1]);

const {lenguaje1, lenguaje2, lenguaje3} = persona2.skills

console.log(lenguaje1);

//Crear un arreglo con obejetos que no se dupliquen

const letras = new Set([1, 2, 3, 4, 5]);

console.log(letras);

letras.add(1);
letras.add(2);
letras.add(6);

console.log(letras);

