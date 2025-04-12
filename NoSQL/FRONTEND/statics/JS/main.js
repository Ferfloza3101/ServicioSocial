document.getElementById('data').addEventListener('submit', (e) => {
    e.preventDefault();
    data_body = { 
        "user": document.querySelector("#userName").value, 
        "password": document.querySelector("#userpwd").value 
    };
    fetch('http://localhost:3000/login', {
        method: 'POST',
        body: JSON.stringify(data_body),
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.mdb_data == null) {
            alert("Usuario y contraseña incorrectos");
        } else {
            alert("Usuario y contraseña correctos");
        }
    });
});
