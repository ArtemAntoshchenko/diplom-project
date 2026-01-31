async function get_habits(event) {
    event.preventDefault();
    try {
        const response=await fetch('/habits/main/getHabits', {method:'GET', headers:{'Accept':'application/json'}})
        if (!response.ok) {
            alert('Произошла ошибка при обновлении привычки')
            return; 
        }
        const habits=await response.json()
        const rows=document.querySelector('#tbodyHabits')
        habits.forEach(habit=>rows.append(row(habit)))
        } catch (error) {
            console.error('Ошибка:', error);
            alert('Произошла ошибка. Пожалуйста, попробуйте снова');
            }
}

async function get_active_habits(event) {
    event.preventDefault();
    try {
        const response=await fetch('/habits/main/getActiveHabits', {method:'GET', headers:{'Accept':'application/json'}})
        if (!response.ok) {
            alert('Произошла ошибка при обновлении привычки')
            return; 
        }
        const habits=await response.json()
        const rows=document.querySelector('#tbodyActiveHabits')
        habits.forEach(habit=>rows.append(row(habit)))
        } catch (error) {
            console.error('Ошибка:', error);
            alert('Произошла ошибка. Пожалуйста, попробуйте снова');
            }
}

async function createHabit() {
    window.location.href='/habits/main/createNewHabit'
}

async function editHabit(event, habit_id, habit_name) {
    event.preventDefault();
    try {
        const response=await fetch('/main/updateHabit', {
            method:'PUT',
            headers:{'Accept':'application/json', 'Content-Type': 'application/json'},
            body: JSON.stringify({id:habit_id, name:habit_name, description:descriptionTd, goal:goalTd})
        })
        if (!response.ok) {
            alert('Произошла ошибка при обновлении привычки')
            return; 
        }
        const result=await response.json();
        document.querySelector('data-rowid'==result.id).replaceWith(row(result))
        } catch (error) {
            console.error('Ошибка:', error);
            alert('Произошла ошибка. Пожалуйста, попробуйте снова');
            }
}

async function deleteHabit(event, habit_id) {
    event.preventDefault();
    try {
        const response=await fetch(`/main/delete/${habit_id}`, {
        method:'DELETE',
        headers:{'Accept':'application/json'}
    })
        if (!response.ok) {
            alert('Произошла ошибка при удалении привычки')
            return; 
        }
        const result=await response.json();
        document.querySelector(nameTd=result.name).replaceWith(row(result))
        } catch (error) {
            console.error('Ошибка:', error);
            alert('Произошла ошибка. Пожалуйста, попробуйте снова');
            }
    const respons=await fetch(`/main/delete/${habit_id}`, {
        method:'DELETE',
        headers:{'Accept':'application/json'}
    })
    if (respons.ok===true){
        const car=await respons.json()
        document.querySelector(`tr[data-rowid='${car.id}']`).remove()
    }
    else {
        const error=await respons.json()
        console.log(error.message)
    }
}


function row(habit) {
    const tr=document.createElement('tr')
    tr.setAttribute('data-rowid', habit.id)

    const nameTd=document.createElement('td')
    nameTd.append(habit.name)
    tr.append(nameTd)

    const descriptionTd=document.createElement('td')
    descriptionTd.append(habit.description)
    tr.append(descriptionTd)

    const goalTd=document.createElement('td')
    goalTd.append(habit.goal)
    tr.append(goalTd)

    const progressTd=document.createElement('td')
    progressTd.append(habit.progress)
    tr.append(progressTd)

    const linksTd=document.createElement('td')

    const editLink=document.createElement('button')
    editLink.append('Редактировать привычку')
    editLink.addEventListener('click', async()=>await editHabit(habit.id))
    linksTd.append(editLink)

    const deleteLink=document.createElement('button')
    deleteLink.append('Удалить привычку')
    deleteLink.addEventListener('click', async()=>await deleteHabit(habit.id))
    linksTd.append(deleteLink)

    tr.appendChild(linksTd)
    return tr
}