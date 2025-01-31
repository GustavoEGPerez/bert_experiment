import json
from transformers import pipeline
import torch

# Definir o nome do modelo
model_name = "cross-encoder/nli-deberta-v3-large"

# Verificar dispositivo disponível
device = 0 if torch.cuda.is_available() else -1

# Inicializar o pipeline de classificação zero-shot
classifier = pipeline("zero-shot-classification", model=model_name, device=device)

# Texto base para classificação
text = "Abrir o navegador, acessar o portal ERP, clicar em 'Baixar', salvar arquivo 'relatorio_financeiro.xlsx'"

# Ler atividades candidatas do arquivo JSON
with open("candidates.json", "r", encoding="utf-8") as f:
    candidate_labels = json.load(f)

# Obter previsões de similaridade
result = classifier(text, candidate_labels, multi_label=True)

# Criar ranking ordenado
ranked_results = sorted(zip(result["labels"], result["scores"]), key=lambda x: x[1], reverse=True)# type: ignore

# Exibir resultado com ranking
print("\nRanking de Similaridade:")
for rank, (label, score) in enumerate(ranked_results, start=1):
    print(f"{rank}. {label} - Score: {score:.2f}")