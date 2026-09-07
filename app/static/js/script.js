// Glass Classification Prediction
document.getElementById('predictionForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData);

    // Sayıya çevir
    Object.keys(data).forEach(key => {
        data[key] = parseFloat(data[key]);
    });

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        displayResult(result);
    } catch (error) {
        console.error('Error:', error);
        showError('Tahmin yapılırken hata oluştu. Lütfen tekrar deneyin.');
    }
});

function displayResult(result) {
    const resultDiv = document.getElementById('result');

    // Ana bilgileri göster
    document.getElementById('glassType').textContent = result.glass_type;
    document.getElementById('glassTypeNumber').textContent = `Type ${result.glass_type_number}`;

    // Güven oranını göster
    const confidencePercent = (result.probability * 100).toFixed(2);
    document.getElementById('confidencePercent').textContent = `${confidencePercent}%`;
    document.getElementById('confidenceBar').style.width = `${confidencePercent}%`;

    // Tüm türlerin olasılıklarını göster
    const confidenceLevels = document.getElementById('confidenceLevels');
    confidenceLevels.innerHTML = '';

    Object.entries(result.confidence_levels).forEach(([type, probability]) => {
        const percent = (probability * 100).toFixed(1);
        const confidence = getConfidenceLevel(probability);

        const item = document.createElement('div');
        item.className = `confidence-level-item ${confidence}`;
        item.innerHTML = `
            <div class="type">${type}</div>
            <div class="percent">${percent}%</div>
        `;
        confidenceLevels.appendChild(item);
    });

    // Sonuç göster
    resultDiv.classList.remove('hidden');
    resultDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function getConfidenceLevel(probability) {
    if (probability >= 0.5) return 'high';
    if (probability >= 0.2) return 'medium';
    return 'low';
}

function showError(message) {
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `<div class="error">${message}</div>`;
    resultDiv.classList.remove('hidden');
    resultDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function resetForm() {
    document.getElementById('predictionForm').reset();
    document.getElementById('result').classList.add('hidden');
    document.getElementById('predictionForm').focus();
}
