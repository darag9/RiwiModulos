//manejo de errores

// try {
//     const num = 0;
//     if (num === 1) {
//         console.log("The number is one.");
//     } else {
//         throw new Error("The number is not one.");
//     }

// } catch (error) {
//     console.error("Error:", error.message);
// }

//Operador de encadenamiento opcional

const usuario = {
    nombre: 'Daniel',
    direccion: {
        ciudad: 'Medellin'
    },
    contacto: {
        telefono: '123456789'
    }
};

console.log(usuario.nombre);
console.log(usuario.direccion.ciudad);
console.log(usuario.contacto.telefono);

console.log(usuario?.isActive);