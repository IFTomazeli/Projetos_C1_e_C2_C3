// O caminho para a pasta onde você salvou os arquivos do modelo
const URL = "./";

let model, maxPredictions;

// Carrega o modelo assim que a página abre
async function init() {
    const modelURL = URL + "model.json";
    const metadataURL = URL + "metadata.json";

    try {
        model = await tmImage.load(modelURL, metadataURL);
        maxPredictions = model.getTotalClasses();
        
        document.getElementById("status").innerText = "Modelo pronto! Envie uma imagem.";
        document.getElementById("imageUpload").disabled = false; // Libera o botão de upload
    } catch (error) {
        document.getElementById("status").innerText = "Erro ao carregar o modelo. Verifique a pasta 'modelo'.";
        console.error(error);
    }
}

// Lida com o upload da imagem
const imageUpload = document.getElementById('imageUpload');
const imagePreview = document.getElementById('imagePreview');

imageUpload.addEventListener('change', async (e) => {
    const file = e.target.files[0];
    if (file) {
        document.getElementById("status").innerText = "Analisando a imagem...";
        const reader = new FileReader();
        
        reader.onload = function(event) {
            imagePreview.src = event.target.result;
            imagePreview.style.display = 'block';
            
            // Aguarda a imagem carregar na tela para fazer a predição
            imagePreview.onload = () => predict();
        }
        reader.readAsDataURL(file);
    }
});

// Faz a predição e mostra os resultados
async function predict() {
    const prediction = await model.predict(imagePreview);
    let resultText = "<strong>Resultados:</strong><br>";
    
    for (let i = 0; i < maxPredictions; i++) {
        // Formata a probabilidade para porcentagem (ex: 98.50%)
        const probability = (prediction[i].probability * 100).toFixed(2);
        resultText += `${prediction[i].className}: ${probability}% <br>`;
    }
    
    document.getElementById("label-container").innerHTML = resultText;
    document.getElementById("status").innerText = "Análise concluída!";
}

// Inicia o carregamento
init();