function validateIdea() {
    const idea = document.getElementById("ideaInput").value;
    fetch("http://127.0.0.1:5000/validate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ idea })
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById("output").textContent = data.result;
    })
    .catch(error => {
      document.getElementById("output").textContent = "Error: " + error;
    });
  }
  