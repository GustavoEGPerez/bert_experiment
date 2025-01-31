# Projeto de Comparação de Modelos para Interpretação Comparativa

Este projeto implementa um experimento comparativo entre três modelos de inferência textual para determinar qual apresenta melhor desempenho na identificação de similaridade entre atividades operacionais. Os modelos analisados são:

- **BERT** (`facebook/bart-large-mnli`)
- **RoBERTa** (`joeddav/xlm-roberta-large-xnli`)
- **DeBERTa** (`cross-encoder/nli-deberta-v3-large`)

Os experimentos utilizam a infraestrutura configurada em home (~), que abriga o ambiente de desenvolvimento e os modelos utilizados no ambiente atual.

## 📂 Estrutura do Laboratório
O laboratório foi configurado conforme a seguinte estrutura:

```
~/ailabs/
├── models/          # Modelos de IA
│   ├── transformers/ # Modelos baseados em Transformer
├── datasets/        # Conjuntos de dados
├── workspaces/      # Projetos e experimentos
│   ├── tsaI_experiments/  # Diretório dos experimentos
├── dependencies/    # Dependências e ambientes virtuais
│   ├── venvs/       # Ambientes virtuais Python
│       ├── tsaI_env/  # Ambiente virtual Python para o experimento
```

## 🛠️ Preparação do Ambiente
### 1️⃣ **Criando e ativando o ambiente virtual**
```bash
python3.12 -m venv ~/ailabs/dependencies/venvs/tsaI_env
source ~/ailabs/dependencies/venvs/tsaI_env/bin/activate
```

### 2️⃣ **Instalando as dependências necessárias**
```bash
pip install --upgrade pip
pip install torch torchvision torchaudio transformers datasets numpy scikit-learn matplotlib ipykernel
```

### 3️⃣ **Download dos Modelos**
Na primeira execução de cada experimento, os modelos serão baixados automaticamente pela biblioteca `transformers`. Para realizar o download manualmente e armazenar no cache local, execute:

```bash
python -c "from transformers import AutoModel, AutoTokenizer; \
            models = ['facebook/bart-large-mnli', 'joeddav/xlm-roberta-large-xnli', 'cross-encoder/nli-deberta-v3-large']; \
            [AutoModel.from_pretrained(m, cache_dir='~/ailabs/models/transformers/') for m in models]; \
            [AutoTokenizer.from_pretrained(m, cache_dir='~/ailabs/models/transformers/') for m in models]"
```

Isso garantirá que os modelos estejam disponíveis localmente para uso offline.

## 🚀 Configuração no VSCode
1. Abra o diretório do projeto no VSCode:
```bash
cd ~/ailabs/workspaces/tsaI_experiments
code .
```

2. Selecione o ambiente virtual no VSCode:
   - Pressione **Ctrl + Shift + P**
   - Pesquise por **"Python: Select Interpreter"**
   - Escolha o caminho:
     ```
     ~/ailabs/dependencies/venvs/tsaI_env/bin/python
     ```

Agora o ambiente está pronto para executar os experimentos com os diferentes modelos de inferência textual. 🚀

