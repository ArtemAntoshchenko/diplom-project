async function get_daily_list_habits() {
    const respons=await fetch('/main/getActiveHabits')
    if (respons.ok === true){
        const habits=await respons.json()
        const rows=document.querySelector('#dailyHabitsList')
        habits.forEach(habit=>rows.append(habit))
    }
}

async function complete_task(task_id) {
    const respons=await fetch('')
}


get_daily_list_habits()