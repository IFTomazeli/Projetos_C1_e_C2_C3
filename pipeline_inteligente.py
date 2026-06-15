import os
import cv2
import json
import time
from dotenv import load_dotenv
from groq import Groq

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

def chamar_analise_groq(dados_contexto):
    """
    Envia o payload estruturado da C2 para o Groq
    """
    try:
        client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        
        if not os.environ.get("GROQ_API_KEY"):
            return "Erro: Chave GROQ_API_KEY não encontrada no arquivo .env"

        payload_json = json.dumps(dados_contexto, ensure_ascii=False, indent=2)
        
        system_prompt = (
            "Você é um especialista em Visão Computacional e Monitoramento de Ambientes Inteligentes. "
            "Sua tarefa é analisar relatórios estruturados em JSON vindos de uma câmera de segurança com YOLOv8 "
            "e gerar uma análise executiva clara, apontando possíveis padrões, anomalias e recomendações de segurança "
            "ou organização. Seja conciso e use tópicos."
        )
        
        user_prompt = f"""Analise os seguintes dados consolidados obtidos pela detecção da webcam em tempo real:

Dados da C2:
{payload_json}

Por favor, forneça:
1. Resumo do cenário detectado.
2. Análise de possíveis riscos, anomalias ou padrões observados.
3. Sugestão prática de ação com base nos objetos identificados.
"""

        print("\n[Groq API] Enviando dados para inferência ultra-rápida...")
        inicio_latencia = time.time()

        resposta = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.2,
            max_tokens=1000
        )
        
        latencia_final = time.time() - inicio_latencia
        print(f"[Groq API] Resposta recebida com sucesso! Latência: {latencia_final:.2f}s")
        
        return resposta.choices[0].message.content

    except Exception as e:
        return f"Falha na comunicação com o ecossistema generativo Groq: {str(e)}"


def executar_pipeline_c2_c3():
    """
    Executa a detecção do YOLOv8 e consolida os dados estruturados
    """
    from ultralytics import YOLO
    
    print("Inicializando modelo YOLOv8...")
    modelo = YOLO("yolov8n.pt")
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Erro: Não foi possível acessar o hardware da webcam.")
        return

    historico_deteccao = {}
    tempo_inicio = time.time()

    print("\n--- Sistema Operacional Iniciado ---")
    print("Monitore o ambiente pela janela de vídeo.")
    print("Pressione 'a' para DISPARAR A ANÁLISE GENERATIVA DA LLM.")
    print("Pressione 'q' para ENCERRAR o sistema.")

    while True:
        sucesso, frame = camera.read()
        if not sucesso:
            break

        resultados = modelo(frame, stream=True)
        objetos_no_frame = {}

        for resultado in resultados:
            frame_anotado = resultado.plot()
            
            for box in resultado.boxes:
                classe_id = int(box.cls[0])
                classe_nome = modelo.names[classe_id]
                objetos_no_frame[classe_nome] = objetos_no_frame.get(classe_nome, 0) + 1

        for nome_classe, quantidade in objetos_no_frame.items():
            if quantidade > historico_deteccao.get(nome_classe, 0):
                historico_deteccao[nome_classe] = quantidade

        cv2.imshow("Monitoramento Integrado C2 + C3", frame_anotado)
        
        tecla = cv2.waitKey(1) & 0xFF
        
        if tecla == ord('a'):
            dados_consolidados = {
                "ambiente": "Webcam de Monitoramento Local",
                "tempo_decorrido_segundos": round(time.time() - tempo_inicio, 2),
                "maior_pico_objetos_detectados": historico_deteccao
            }
            
            print("\n" + "="*50)
            print("DADOS BRUTOS DA C2 PRONTOS PARA SERIALIZAÇÃO:")
            print(json.dumps(dados_consolidados, indent=2))
            print("="*50)
            
            analise = chamar_analise_groq(dados_consolidados)
            
            print("\n" + "="*50)
            print("ANÁLISE INTERPRETATIVA GERADA PELA LLM (GROQ):")
            print(analise)
            print("="*50 + "\n")
            
        elif tecla == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    executar_pipeline_c2_c3()