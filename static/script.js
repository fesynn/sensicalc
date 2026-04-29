document.getElementById("btn-convert").addEventListener("click", async () => {
  // Pega os valores do formulário
  const payload = {
    from_game: document.getElementById("from_game").value,
    to_game: document.getElementById("to_game").value,
    sensitivity: document.getElementById("sensitivity").value,
    from_dpi: document.getElementById("from_dpi").value || null,
    to_dpi: document.getElementById("to_dpi").value || null,
    from_weight: document.getElementById("from_weight").value || null,
    to_weight: document.getElementById("to_weight").value || null,
  };

  // Esconde resultado e erro anteriores
  document.getElementById("result").style.display = "none";
  document.getElementById("error").style.display = "none";

  try {
    const response = await fetch("/convert", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const data = await response.json();

    if (data.error) {
      document.getElementById("error").textContent = data.error;
      document.getElementById("error").style.display = "block";
      return;
    }

    // Monta os detalhes do resultado
    let details = `${data.from_game} → ${data.to_game}`;
    if (data.from_dpi && data.to_dpi) {
      details += ` • DPI ${data.from_dpi} → ${data.to_dpi}`;
    }
    if (data.from_weight && data.to_weight) {
      details += ` • Peso ${data.from_weight}g → ${data.to_weight}g`;
    }

    document.getElementById("result-value").textContent = data.converted_sensitivity;
    document.getElementById("result-details").textContent = details;
    document.getElementById("result").style.display = "block";

  } catch (err) {
    document.getElementById("error").textContent = "Erro ao conectar com o servidor.";
    document.getElementById("error").style.display = "block";
  }
});