let taskList = [];
let send = document.getElementById('send');
let showTask = document.getElementById('showTask');

function addTask() {
    let task = document.getElementById('task').value;
    if (task != '') {

        let taskInfo = document.createElement('li');
        showTask.appendChild(taskInfo);
        taskList.push(task);
        taskInfo.innerHTML = task;

        let doneButton = document.createElement('button');
        doneButton.textContent = 'Done';
        taskInfo.appendChild(doneButton);

        let textDone = document.createElement('p');

        doneButton.addEventListener("click", (e) => {
            textDone.innerHTML = 'Done!';
            taskInfo.appendChild(textDone);
        });

        let deleteButton = document.createElement('button');
        deleteButton.textContent = 'delete';
        taskInfo.appendChild(deleteButton);

        deleteButton.addEventListener("click", (e) => {
            showTask.removeChild(taskInfo);
            taskList.pop(task);
        });

        
    } else {
        alert('input required');
    }
    console.log(taskList);
}

