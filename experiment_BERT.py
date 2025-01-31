import json
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch

# Definir modelo e tokenizer
model_name = "facebook/bart-large-mnli"  # Modelo especializado para classificação zero-shot
classifier = pipeline("zero-shot-classification", model=model_name, device=0 if torch.cuda.is_available() else -1)

# Texto do Cluster de Sessões
text = "Abrir o navegador, acessar o portal ERP, clicar em 'Baixar', salvar arquivo 'relatorio_financeiro.xlsx'"

# Ler atividades candidatas do arquivo JSON
with open("candidates.json", "r", encoding="utf-8") as f:
    candidate_labels = json.load(f)

# Obter previsões de similaridade
result = classifier(text, candidate_labels, multi_label=False)

# Criar ranking ordenado
ranked_results = sorted(zip(result["labels"], result["scores"]), key=lambda x: x[1], reverse=True) # type: ignore

# Exibir resultado com ranking
print("\nRanking de Similaridade:")
for rank, (label, score) in enumerate(ranked_results, start=1):
    print(f"{rank}. {label} - Score: {score:.2f}")
