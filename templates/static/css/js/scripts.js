document.getElementById('predictionForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const exampleInput = document.getElementById('exampleInput').value;

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ exampleInput: exampleInput }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = 'Prediction: ' + data.prediction;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
