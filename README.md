# Colab AI Project Collection

These notebooks were developed in **2024** for **learning and experimentation**—exploring NLP and modern LLMs end-to-end rather than serving production systems.

A portfolio of **hands-on NLP and transformer notebooks**, originally built in **Google Colab**, covering classical text pipelines through modern LLM fine-tuning with **Hugging Face Transformers**, **parameter-efficient adaptation (LoRA)**, and **standard evaluation metrics**.

Each notebook is self-contained and includes an **Open in Colab** badge pointing at this repository.

---

## What’s inside (project-by-project)

| Notebook | What you explore | Stack & datasets (high level) |
|----------|------------------|-------------------------------|
| [`Text_Cleaning_Project.ipynb`](Text_Cleaning_Project.ipynb) | End-to-end **text normalization** for downstream NLP: regex cleanup, punctuation, chat-word handling, light spell correction, **stop-word** removal, and **emoji** stripping, on real review text. | pandas; IMDB sentiment corpus (CSV via URL in notebook) |
| [`Word2Vec_Project.ipynb`](Word2Vec_Project.ipynb) | Train a **Word2Vec** model from scratch with **Gensim**, preprocess long-form fiction text, and inspect **similarity** and **doesn’t-match** behavior—classic **static embeddings** before transformers. | NLTK, Gensim; Game of Thrones books (Kaggle-style layout referenced in notebook) |
| [`Sentence_Embedding_Project.ipynb`](Sentence_Embedding_Project.ipynb) | **BERT-based sentence embeddings**: tokenization with **`bert-base-uncased`**, forward pass through **`BertModel`**, pooling/context vectors, and decoding back to readable tokens. | Hugging Face Transformers; PyTorch/CUDA where available |
| [`NER_with_BERT_Project.ipynb`](NER_with_BERT_Project.ipynb) | **Named Entity Recognition** as token classification: fine-tune **`bert-base-uncased`** with **`AutoModelForTokenClassification`**, aligned token–label encoding, training with **`Trainer`**, and evaluation (**seqeval** / **`evaluate`**). Optional **push to Hugging Face Hub**. | `datasets` (**CoNLL-2003**), Transformers, Accelerate |
| [`Q&A_with_LM.ipynb`](Q&A_with_LM.ipynb) | **Extractive question answering** on **SQuAD-style** data: predict an answer **span** in the passage (or “unanswerable” behavior as supported by the pipeline). Uses a BERT-style reader via **SimpleTransformers** for fast training/eval. | **SimpleTransformers**; `bert-base-cased`; Stanford QA data (paths in notebook) |
| [`Text_Summarization_Project.ipynb`](Text_Summarization_Project.ipynb) | **Abstractive summarization** with a **seq2seq transformer**: start from **Pegasus** (`google/pegasus-cnn_dailymail`), **fine-tune** on **dialogue → summary** data (**`Samsung/samsum`**), use **`TrainingArguments` + `Trainer`**, and measure quality with **ROUGE** via **`evaluate`**. | Transformers, Datasets, ROUGE |
| [`Llama2_LoRA_Project.ipynb`](Llama2_LoRA_Project.ipynb) | **Instruction tuning** for **Llama 2 7B** with **LoRA** (**PEFT**), **quantization-friendly** tooling (**bitsandbytes** where applicable), and **TRL**-style supervised fine-tuning on an instruction dataset (`mlabonne/guanaco-llama2-1k`). Illustrates **efficient LLM adaptation** vs full fine-tuning. | PEFT, TRL, Accelerate, Transformers |
| [`clear_format.ipynb`](clear_format.ipynb) | Small **utility** used to normalize or strip noisy notebook output/metadata across the project notebooks (helpful when syncing from Colab to Git). | — |

---

## Skills and themes reflected in this repo

These notebooks map cleanly to common hiring and portfolio keywords:

- **Natural Language Processing**: cleaning, tokenization, embeddings, span QA, NER, summarization  
- **Transformers & LLMs**: BERT (encoder), Pegasus (encoder–decoder), **Llama 2** (decoder)  
- **Fine-tuning**: full fine-tuning (NER, summarization), **LoRA / PEFT** (Llama 2)  
- **Hugging Face ecosystem**: `transformers`, `datasets`, `evaluate`, Hub workflows  
- **Model evaluation**: span metrics for QA/NER, **ROUGE** for summarization  
- **Efficient training**: mixed precision / Trainer patterns, parameter-efficient LLM tuning  

**GPT-class APIs, LangChain, RAG, AWS Bedrock, and Azure AI** are important parts of the modern LLM stack but are **not implemented as standalone projects in this repository**. If you use those in production or other repos, call them out on your profile or add a short “Elsewhere” section there—keep this README tightly aligned with what visitors can actually run from these notebooks.

---

## Tech stack (from the notebooks)

`Python` · `Jupyter` / **Google Colab** · **PyTorch** · **Hugging Face** (`transformers`, `datasets`, `accelerate`, `evaluate`, `peft`, `trl`) · **NLTK** · **Gensim** · **SimpleTransformers** (QA) · **ROUGE** · **seqeval** (NER)

---

## How to run

1. **Recommended:** open any notebook on **Google Colab** via the badge at the top of the file (points to `jackychh7878/Colab_AI_Project` on GitHub).  
2. **Locally:** use Python 3.10+ (as in the Colab logs), install dependencies per notebook (`pip install …` cells), and ensure **GPU** availability for larger models (BERT fine-tunes, Pegasus, Llama 2 + LoRA).  
3. **Secrets:** notebooks that use the Hugging Face Hub may expect a token (`notebook_login` / `HF_TOKEN` patterns)—add your own token where prompted.

---

## Repository layout

```
Colab_AI_Project/
├── Text_Cleaning_Project.ipynb
├── Word2Vec_Project.ipynb
├── Sentence_Embedding_Project.ipynb
├── NER_with_BERT_Project.ipynb
├── Q&A_with_LM.ipynb
├── Text_Summarization_Project.ipynb
├── Llama2_LoRA_Project.ipynb
├── clear_format.ipynb
└── README.md
```

---

## Reference

- **Author:** Jacky Chong — Colab AI project collection.
- **Medical chatbot (Retrieval-Augmented Generation)** — write-up / notes: [Google Doc](https://docs.google.com/document/d/1R8icwL_6vgVJ83ORigfPjhwPHN3afIqL_XFFEKTjbLc/edit?tab=t.0)
- **Google Drive backup** of materials: [folder](https://drive.google.com/drive/folders/1Phk8Jul0e_Quw4CNhxtqbLci0VSPA7B5?usp=sharing)

---