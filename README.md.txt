# Projeto C2: Reconhecimento de Objetos com YOLOv8

Este projeto implementa um sistema de detecção de objetos em tempo real utilizando o algoritmo YOLOv8 (You Only Look Once) e a biblioteca OpenCV. O sistema utiliza a webcam para identificar e classificar múltiplos objetos simultaneamente (dataset COCO).

## 🛠️ Pré-requisitos e Instalação

Certifique-se de ter o Python instalado na sua máquina.

1. Clone este repositório ou acesse a pasta do projeto.
2. Instale as dependências executando o comando abaixo no terminal:
   ```bash
   pip install ultralytics opencv-python


## 📂 Estrutura do Repositório (Evolução do Projeto)

Este repositório contém a evolução contínua das avaliações da disciplina:

* **`pipeline_inteligente.py`**: 🟢 **[AVALIAÇÃO C3]** Código principal atualizado. Contém o pipeline completo integrado com a LLM (Groq) para análise de contexto em tempo real.
* **`reconhecimento.py`**: 🟡 **[AVALIAÇÃO C2]** Script da etapa anterior, contendo apenas o laço de captura da webcam e inferência isolada com YOLOv8.
* **`.gitignore`**: Regras de segurança implementadas na C3 para ocultar credenciais (`.env`).


## 🧠 Engenharia de Prompt e Integração com LLM (C3)

Para a camada de inteligência generativa, o sistema integra a API do Groq.

**Modelo Escolhido:** `llama-3.3-70b-versatile`. A escolha justifica-se pelo excelente equilíbrio entre velocidade de inferência (LPU) e o alto raciocínio lógico de um modelo de 70 bilhões de parâmetros, ideal para estruturar saídas JSON em análises técnicas coerentes.

**Configuração de Inferência:**
- **Temperatura (0.2):** Utilizada uma temperatura baixa para reduzir a aleatoriedade (alucinações) e garantir respostas objetivas, já que estamos lidando com dados de monitoramento.
- **Max Tokens (500):** Limite estabelecido para garantir concisão na leitura do dashboard do usuário e economizar requisições.

**Estrutura dos Prompts:**
- **System Prompt:** "Você é um especialista em Visão Computacional e Monitoramento de Ambientes Inteligentes. Sua tarefa é analisar relatórios estruturados em JSON vindos de uma câmera de segurança com YOLOv8 e gerar uma análise executiva clara, apontando possíveis padrões, anomalias e recomendações de segurança ou organização. Seja conciso e use tópicos."
- **User Prompt:** Recebe o payload (JSON) contendo as estatísticas de detecção (tempo decorrido e pico de objetos no frame) e exige uma saída padronizada em 3 tópicos (Resumo do cenário, Análise de riscos/padrões e Sugestão prática).


