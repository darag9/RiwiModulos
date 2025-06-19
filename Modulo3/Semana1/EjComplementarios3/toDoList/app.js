let enviar = document.getElementById("enviar")

let lista_tareas = [];
let tareas_html = [];

enviar.addEventListener("click", (e) => {

    let tarea = document.getElementById("tarea").value;
    let mostrar = document.getElementById("mostrar");
    

    lista_tareas.push(tarea);
    tareas_html.push(tarea);

    mostrar.style.display="flex";
    mostrar.style.flexDirection="column";

    console.log(lista_tareas);

    for (let i=0; i<tareas_html.length;i++) {
        mostrar.innerHTML += tareas_html[i];
        
        tareas_html.pop()
    }
});




