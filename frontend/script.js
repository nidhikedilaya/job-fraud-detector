async function predict() {
  const data = {
    title: document.getElementById("title").value,
    description: document.getElementById("description").value,
  };

  const response = await fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  const result = await response.json();
  document.getElementById(
    "result"
  ).innerText = `Prediction: ${result.prediction}`;
}
