import json
from transformers import XLMRobertaTokenizer, XLMRobertaForSequenceClassification, pipeline
import torch

# Verificar e instalar protobuf e sentencepiece se necessário
try:
    import google.protobuf
except ImportError:
    print("Erro: protobuf não encontrado. Instale com `pip install protobuf`.")

try:
    import sentencepiece
except ImportError:
    print("Erro: sentencepiece não encontrado. Instale com `pip install sentencepiece`.")

# Definir modelo e tokenizer
model_name = "joeddav/xlm-roberta-large-xnli"
tokenizer = XLMRobertaTokenizer.from_pretrained(model_name)
model = XLMRobertaForSequenceClassification.from_pretrained(model_name, ignore_mismatched_sizes=True)

# Verificar dispositivo
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)# type: ignore

classifier = pipeline("zero-shot-classification", model=model, tokenizer=tokenizer, device=device.index if torch.cuda.is_available() else -1)

# Texto do Cluster de Sessões
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