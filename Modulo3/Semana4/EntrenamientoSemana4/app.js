const saveData = document.getElementById('saveButton');
const clearData = document.getElementById('clearButton');



saveData.addEventListener('click', () => {
    
    const nameInput = document.getElementById('name');
    const ageInput = document.getElementById('age');

    if (!nameInput || !ageInput) {
        alert('Error: The elements of the form doesnt exists.');    
    }

    const name = nameInput.value.trim();
    const age = ageInput.value;

    if (name && !isNaN(age)) {
        localStorage.setItem('userName', name);
        localStorage.setItem('userAge', age);
        displayData();
    } else {
        alert('Please input a valid name and age');
    }
});

function displayData() {
    const name = localStorage.getItem('userName');
    const age = localStorage.getItem('userAge');
    const outputDiv = document.getElementById('output');
    if (name && age) {
        outputDiv.textContent = `Hola ${name}, tienes ${age} años`;   
    } else {
        outputDiv.textContent = `No hay datos almacenados.`;
    }


}

window.onload = displayData;

if (!sessionStorage.getItem()
