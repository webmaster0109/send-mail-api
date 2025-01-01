const form = document.querySelector('form');

form.addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);
    console.log(data);

    fetch('http://localhost:8000/api/sponsor-mail-form/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
    alert('Form submitted');
    console.log(JSON.stringify(data));
    form.reset();

});
    