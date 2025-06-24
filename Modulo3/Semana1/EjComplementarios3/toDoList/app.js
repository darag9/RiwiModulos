let taskList = [];
const form = document.querySelector('form')


form.addEventListener("submit", function(event) {
    event.preventDefault()
    addTask()
})

function addTask() {
    const showTask = document.querySelector('#showTask');
    const task = document.querySelector('input').value;
    if (task) {

        const taskInfo = document.createElement('li');
        showTask.appendChild(taskInfo);
        taskList.push(task);
        taskInfo.innerHTML = task;

        const doneButton = document.createElement('button');
        doneButton.textContent = 'Done';
        taskInfo.appendChild(doneButton);

        const textDone = document.createElement('p');

        doneButton.addEventListener("click", (e) => {
            textDone.innerHTML = 'Done!';
            
            if (!taskInfo.classList.contains('done')) {
                const check = document.createElement('span');
                check.className = 'checkmark';
                check.innerHTML = '✔';
                taskInfo.insertBefore(check, taskInfo.firstChild);
                taskInfo.classList.add('done');
                taskInfo.appendChild(textDone);
                doneButton.textContent = "undone";
            }else{
                const span = document.querySelector('span')
                const p = document.querySelector('p')
                taskInfo.classList.remove('done')
                taskInfo.removeChild(span)
                taskInfo.removeChild(p)
                doneButton.textContent = "Done"
            }

        });


        const deleteButton = document.createElement('button');
        deleteButton.className = 'delete'
        deleteButton.textContent = 'delete';

        taskInfo.appendChild(deleteButton);

        deleteButton.addEventListener("click", (e) => {
            showTask.removeChild(taskInfo);
            taskList.pop(task);
        });

        document.querySelector('input').value ="";
    } else {
        alert('input required');
    }
    console.log(taskList);
    
}

