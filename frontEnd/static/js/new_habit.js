async function createHabit(event) {
    event.preventDefault();
    const form=document.getElementById('new_habit-form');
    const formData=new FormData(form);
    const data=Object.fromEntries(formData.entries());
    try {
        const response=await fetch('/habits/main/createNewHabit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        if (!response.ok) {
            const errorData=await response.json();
            displayErrors(errorData);  
            return; 
        }
        const result=await response.json();
        if (result.message) { 
            window.location.href='/habits/main';
        } else {
            alert(result.message || 'Неизвестная ошибка');
        }
    } catch (error) {
        console.error('Ошибка:', error);
        alert('Произошла ошибка при создании привычки. Пожалуйста, попробуйте снова.');
    }
}

function displayErrors(errorData) {
    let message='Произошла ошибка';
    if (errorData && errorData.detail) {
        if (Array.isArray(errorData.detail)) {
            message = errorData.detail.map(error=> {
                if (error.type==='string_too_short') {
                    return `Поле "${error.loc[1]}" должно содержать минимум ${error.ctx.min_length} символов.`;
                }
                return error.msg || 'Произошла ошибка';
            }).join('\n');
        } else {
            message=errorData.detail || 'Произошла ошибка';
        }
    }
    alert(message);
}