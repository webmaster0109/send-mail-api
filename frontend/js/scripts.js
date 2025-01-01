const form = document.querySelector('form');

form.addEventListener('submit', async function(e) {
    e.preventDefault();
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);
    console.log(data);

    try {
        const response = await fetch('http://localhost:8000/api/contact-form/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const result = await response.json();

        
        if (response.ok) {
            alert('Form submitted');
            console.log(result);
            console.log(JSON.stringify(data));
            form.reset();
        } else if (response.status === 400) {
            console.log(result);
            alert('Please fill in all fields');
        } else if (response.status === 500) {
            console.log(result);
            alert('Something went wrong, please try again');
        }
    } catch (error) {
        console.error(error);
    } finally {
        console.log('done');
    }

});
    