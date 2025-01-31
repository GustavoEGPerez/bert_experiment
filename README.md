# Projeto BERT Experiment

Este projeto implementa um experimento utilizando o modelo `bert-base-multilingual-cased` do Hugging Face para testar a associação de combinações de palavras a um array de combinações e determinar o índice de correlação de assuntos.

## 📂 Estrutura do Laboratório
O laboratório foi configurado no disco `/saswdata` seguindo a seguinte estrutura:

```
/saswdata/ailab/
├── models/          # Modelos de IA
│   ├── transformers/ # Modelos baseados em Transformer
├── datasets/        # Conjuntos de dados
├── workspaces/      # Projetos e experimentos
│   ├── project_1/
│       ├── bert_experiment/  # Diretório deste projeto
├── dependencies/    # Dependências e ambientes virtuais
│   ├── venvs/       # Ambientes virtuais Python
│       ├── bert_experiment_01/  # Ambiente virtual Python desse experimento
```

## 🛠️ Preparação do Ambiente
1. **Foi criado e ativado o ambiente virtual**:
   ```bash
   python3.12 -m venv /saswdata/ailab/dependencies/venvs/bert_experiment
   source /saswdata/ailab/dependencies/venvs/bert_experiment/bin/activate
   ```

2. **Foi feita a instalação das dependências**:
   ```bash
   pip install --upgrade pip
   pip install torch torchvision torchaudio transformers datasets numpy scikit-learn matplotlib ipykernel
   ```

3. **Download do modelo BERT para uso offline**:
   ```bash
   python -c "from transformers import AutoModel, AutoTokenizer; \
              model_name = 'bert-base-multilingual-cased'; \
              model = AutoModel.from_pretrained(model_name, cache_dir='/saswdata/ailab/models/transformers/'); \
              tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir='/saswdata/ailab/models/transformers/')"
   ```

## 🚀 Configuração no VSCode
1. Abra o diretório do projeto no VSCode:
   ```bash
   cd /saswdata/ailab/workspaces/project_1/bert_experiment
   code .
   ```

2. Selecione o ambiente virtual no VSCode:
   - Pressione **Ctrl + Shift + P**
   - Pesquise por **"Python: Select Interpreter"**
   - Escolha o caminho:
     ```
     /saswdata/ailab/dependencies/venvs/bert_experiment/bin/python
     ```

Agora o ambiente está pronto para testar, executar e modificar o projeto! 🚀