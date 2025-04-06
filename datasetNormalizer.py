import os
import cv2
import numpy as np
from PIL import Image
import json

# Diretório de entrada e saída
pasta_entrada = "dataset"
pasta_saida = "dataset_processado"

# Criar diretório de saída se não existir
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

# Obter a lista de pastas (classes) em ordem alfabética
classes = sorted(os.listdir(pasta_entrada))
mapeamento = {indice: classe for indice, classe in enumerate(classes)}
mapeamento_reverso = {classe: indice for indice, classe in enumerate(classes)}

# Salvar o dicionário de mapeamento em formato JSON para uso posterior
with open(os.path.join(pasta_saida, "mapeamento.json"), "w") as f:
    json.dump(mapeamento, f, indent=4)

print("Mapeamento de classes:")
for indice, classe in mapeamento.items():
    print(f"{indice}: {classe}")
    
    # Criar a pasta numerada correspondente no diretório de saída
    pasta_numerada = os.path.join(pasta_saida, str(indice))
    if not os.path.exists(pasta_numerada):
        os.makedirs(pasta_numerada)
    
    # Caminho para a pasta da classe original
    pasta_classe = os.path.join(pasta_entrada, classe)
    
    # Verificar se é diretório
    if not os.path.isdir(pasta_classe):
        continue
    
    # Processar imagens na pasta
    for arquivo in os.listdir(pasta_classe):
        caminho_completo = os.path.join(pasta_classe, arquivo)
        
        # Verificar se é uma imagem
        if os.path.isfile(caminho_completo) and arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            try:
                # Carregar e redimensionar a imagem para 256x256
                imagem = Image.open(caminho_completo)
                imagem_redimensionada = imagem.resize((256, 256), Image.LANCZOS)
                
                # Salvar imagem processada na pasta numerada correspondente
                caminho_saida = os.path.join(pasta_numerada, arquivo)
                imagem_redimensionada.save(caminho_saida)
                
                print(f"Processado: {arquivo} -> Classe: {classe} -> Label: {indice}")
            except Exception as e:
                print(f"Erro ao processar {arquivo}: {e}")

print("\nProcessamento concluído!")
print(f"Dataset processado salvo em: {pasta_saida}")
print(f"Mapeamento de classes salvo em: {os.path.join(pasta_saida, 'mapeamento.json')}")