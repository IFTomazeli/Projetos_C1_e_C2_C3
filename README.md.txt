# 🐱🐶 Classificador de Imagens: Gatos vs Cachorros

Este projeto é uma aplicação web de Machine Learning capaz de classificar imagens entre "Gatos" e "Cachorros". Foi desenvolvido como parte do projeto prático da C1.

## 🛠️ Tecnologias Utilizadas
* **Teachable Machine (Google):** Para o treinamento inicial do modelo.
* **TensorFlow.js:** Para carregar o modelo treinado e executar as predições no navegador.
* **HTML, CSS e JavaScript:** Para a interface de usuário e lógica da aplicação web.
* **Python (Google Colab / Scikit-Learn):** Para aplicar o Princípio de Pareto (80/20) e gerar as métricas de avaliação rigorosa (Acurácia, F1-Score, Matriz de Confusão).

## 🚀 Como Executar o Projeto

1. Clone ou faça o download deste repositório.
2. Certifique-se de que os arquivos do modelo (`model.json`, `metadata.json`, `weights.bin`) estão na raiz da pasta junto com o `index.html`.
3. **Importante:** Por questões de segurança (CORS) do navegador, o projeto não funcionará se o arquivo HTML for aberto diretamente com um duplo clique.
4. Abra a pasta do projeto no **Visual Studio Code**.
5. Utilize a extensão **Live Server** (clicando em "Go Live" no rodapé) para iniciar um servidor local.
6. A página abrirá no seu navegador. Faça o upload de uma foto de um gato ou cachorro e veja a predição!