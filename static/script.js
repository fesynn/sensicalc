document.getElementById("btn-convert").addEventListener("click", async () => {
  const payload = {
    from_game: document.getElementById("from_game").value,
    to_game: document.getElementById("to_game").value,
    sensitivity: document.getElementById("sensitivity").value,
    from_dpi: document.getElementById("from_dpi").value || null,
    to_dpi: document.getElementById("to_dpi").value || null,
    from_weight: document.getElementById("from_weight").value || null,
    to_weight: document.getElementById("to_weight").value || null,
  };

  // Esconde erro anterior
  const errorEl = document.getElementById("error");
  const resultValue = document.getElementById("result-value");
  const resultDetails = document.getElementById("result-details");

  errorEl.style.display = "none";

  try {
    const response = await fetch("/convert", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const data = await response.json();

    if (data.error) {
      errorEl.textContent = data.error;
      errorEl.style.display = "block";
      resultValue.textContent = "—";
      resultDetails.textContent = "";
      return;
    }

    // Monta detalhes
    let details = `${data.from_game}  →  ${data.to_game}`;
    if (data.from_dpi && data.to_dpi) {
      details += `\nDPI: ${data.from_dpi} → ${data.to_dpi}`;
    }
    if (data.from_weight && data.to_weight) {
      details += `\nWEIGHT: ${data.from_weight}g → ${data.to_weight}g`;
    }

    resultValue.textContent = data.converted_sensitivity;
    resultDetails.textContent = details;

  } catch (err) {
    errorEl.textContent = "ERROR: Could not connect to server.";
    errorEl.style.display = "block";
  }
});