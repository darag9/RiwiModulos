const input = document.querySelector('input');
let cont = 0;

input.addEventListener('click', () => {
    const listElement = document.createElement('li');
    const list = document.querySelector('ul');
    cont++;
    
    listElement.innerHTML = `Elemento ${cont}`;

    list.appendChild(listElement);
});