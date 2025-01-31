**Experimento de Seleção de Modelo para Interpretação Comparativa na Plataforma TaskSense.AI**

## **1. Introdução**
Este documento descreve o experimento conduzido para selecionar o modelo mais adequado para interpretação comparativa textual na plataforma **TaskSense.AI for Processes (TSAI)**. O objetivo do estudo é definir qual modelo apresentará maior precisão na identificação de similaridades entre as atividades coletadas pelos agentes da plataforma e as atividades, tarefas, subprocessos e processos definidos no sistema.

## **2. Objetivo do Experimento**
A plataforma TSAI busca identificar padrões e similaridades em instâncias de execução de atividades operacionais. Para isso, foi conduzida uma comparação entre diferentes modelos de **Natural Language Inference (NLI)** para identificar qual apresenta melhor performance em ranqueamento de similaridade textual.

## **3. Modelos Avaliados**
Foram testados os seguintes modelos:

1. **BERT** (`facebook/bart-large-mnli`)
2. **RoBERTa** (`joeddav/xlm-roberta-large-xnli`)
3. **DeBERTa** (`cross-encoder/nli-deberta-v3-large`)

Cada modelo foi avaliado em um contexto de **classificação de similaridade**, comparando um texto de entrada com uma lista de atividades cadastradas.

## **4. Metodologia**
Cada modelo foi utilizado para processar a seguinte frase base:

> "Abrir o navegador, acessar o portal ERP, clicar em 'Baixar', salvar arquivo 'relatorio_financeiro.xlsx'"

As atividades a serem comparadas foram carregadas a partir de um arquivo JSON, representando as tarefas comuns em processos empresariais.

Cada modelo gerou um **ranking de similaridade**, ordenando as atividades conforme sua relevância em relação ao texto de entrada.

## **5. Resultados Obtidos**
Os rankings gerados por cada modelo foram os seguintes:

### **BERT (`facebook/bart-large-mnli`)**
O modelo BERT, na versão `bart-large-mnli`, mostrou o pior desempenho entre os modelos testados. Isso se deve à sua arquitetura baseada em _masked language modeling_, que é otimizada para preenchimento de lacunas em frases, mas menos eficaz para inferência textual. Como resultado, o modelo teve dificuldades em capturar a relação semântica exata entre o texto de entrada e as atividades candidatas. 

A classificação apresentou inconsistências, priorizando atividades que não estavam semanticamente alinhadas ao propósito do texto. Isso ocorre porque o modelo depende fortemente de _entailment_ (relação de implicação), sem uma forte capacidade de _cross-encoding_, resultando em um ranking distorcido.

### **RoBERTa (`joeddav/xlm-roberta-large-xnli`)**
A versão RoBERTa do modelo apresentou uma melhoria significativa em relação ao BERT, devido à sua capacidade de aprendizado contextual aprimorada através do treinamento sem _next sentence prediction_ (NSP), o que lhe permite compreender relações textuais de forma mais eficiente. 

Entretanto, o modelo ainda apresentou alguns problemas com pesos incoerentes no ranking, possivelmente porque sua arquitetura ainda é baseada na classificação de _entailment_, e não em uma abordagem _cross-encoder_. Isso significa que ele avalia cada par de frases de forma independente, sem levar em consideração a interdependência semântica global entre todas as atividades candidatas.

### **DeBERTa (`cross-encoder/nli-deberta-v3-large`)**
O modelo DeBERTa superou os demais devido ao seu mecanismo **Disentangled Attention**, que permite uma representação mais sofisticada da semântica textual. Diferentemente dos outros modelos, **DeBERTa utiliza embeddings de palavras e de relação separadamente**, permitindo um entendimento mais profundo do contexto e das relações entre as palavras. 

Isso resultou em um ranking mais coerente, onde a atividade "Baixar relatório financeiro mensal" ficou melhor posicionada, refletindo a relação contextual correta. Além disso, por ser um **cross-encoder**, o modelo avalia simultaneamente todas as atividades candidatas, permitindo uma classificação global mais precisa e consistente.

## **6. Conclusão e Modelo Selecionado**
Com base nos testes realizados, o modelo **DeBERTa (`cross-encoder/nli-deberta-v3-large`)** foi eleito como a melhor opção para ser implementado na plataforma **TaskSense.AI**. Ele apresentou maior coerência na similaridade entre atividades capturadas e atividades definidas no sistema.

O próximo passo será a integração desse modelo nas **pipelines de interpretação comparativa por similaridade**, permitindo a identificação precisa de instâncias de atividades e tarefas operacionais na TSAI.

## **7. Referências**
- [Documentação oficial do modelo DeBERTa](https://huggingface.co/cross-encoder/nli-deberta-v3-large)
- [Transformers - Hugging Face](https://huggingface.co/docs/transformers/index)

