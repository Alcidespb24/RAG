# HIPAA RAG System - Evaluation Project

A Retrieval-Augmented Generation (RAG) system for querying HIPAA documentation with optimized performance and accuracy metrics.

## Overview

This project implements an advanced RAG system that indexes and queries HIPAA regulatory documents. The system uses state-of-the-art language models and embeddings to provide accurate answers to questions about HIPAA regulations, evaluated against a ground truth dataset.

## Features

- **Best-in-class Models**: Uses GPT-5 and text-embedding-3-large for optimal performance
- **Optimized Chunking**: 256-token chunks with 25-token overlap for precise retrieval
- **Enhanced Prompting**: Custom prompt templates for accurate, fact-based responses
- **Comprehensive Evaluation**: Automated testing against ground truth dataset with detailed metrics
- **Performance Metrics**: Tracks number accuracy, term coverage, and page references

## Project Structure

```
RAG/
├── rag_evaluation.ipynb          # Main evaluation notebook (production-ready)
├── data_source/
│   ├── hipaa-simplification-201303.pdf    # Source HIPAA document
│   └── truth_dataset.json                 # Ground truth Q&A dataset
├── parsed_documents/
│   └── hipaa-simplification-201303_parsed.md  # Pre-parsed document
├── .env                           # API keys (not in repo)
├── pyproject.toml                 # Project dependencies
└── README.md                      # This file
```

## Setup

### Prerequisites

- Python 3.12+
- OpenAI API key
- LlamaParse API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Alcidespb24/RAG.git
cd RAG
```

2. Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows PowerShell
# or
source .venv/bin/activate  # Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your API keys:
```
OPENAI_API_KEY=your_openai_api_key_here
LLAMA_API_KEY=your_llama_api_key_here
```

## Usage

Open and run `rag_evaluation.ipynb` in Jupyter or VS Code:

1. **Setup**: Loads API keys and configurations
2. **Load Truth Dataset**: Loads 5 evaluation questions with expected answers
3. **Initialize RAG**: Configures GPT-5 model and embeddings
4. **Index Document**: Creates vector index from parsed HIPAA document
5. **Query Engine**: Sets up optimized query engine with enhanced prompts
6. **Evaluation**: Runs all questions and evaluates performance
7. **Metrics**: Displays detailed accuracy metrics

## Evaluation Results

Using GPT-5 with optimized settings:

- **Number Accuracy**: 40% (2/5 questions)
- **Term Coverage**: 84.5% average
- **Page Accuracy**: 0% (limitation of parsed format)

### Ground Truth Dataset

The system is evaluated on 5 key HIPAA questions:

1. What is a small health plan?
2. Who must serve the subpoena if the motion requesting issuance is granted?
3. The health care claim status transaction is the transmission of what?
4. What does data aggregation mean?
5. What are the additional rules for health care clearinghouses?

## Optimizations Applied

1. **Reduced Chunk Size**: 512 → 256 tokens for more precise retrieval
2. **Increased Retrieval Candidates**: similarity_top_k = 10
3. **Lowered Similarity Threshold**: 0.3 → 0.2
4. **Enhanced Prompt Template**: Explicit instructions for exact definitions and numbers
5. **Best Available Models**: GPT-5 for generation, text-embedding-3-large for embeddings
6. **Efficient Indexing**: Uses pre-parsed documents without expensive metadata extraction

## Technical Details

### Key Components

- **LlamaIndex**: Framework for RAG implementation
- **OpenAI GPT-5**: Language model for response generation
- **text-embedding-3-large**: Advanced embeddings for semantic search
- **LlamaParse**: Document parsing (already completed)
- **SentenceSplitter**: Optimized text chunking

### Configuration

```python
Settings.llm = OpenAI(model="gpt-5", temperature=0.1)
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-large")
Settings.chunk_size = 256
Settings.chunk_overlap = 25
```

## Future Improvements

- Add hybrid search (keyword + semantic)
- Implement re-ranking mechanism
- Preserve page number metadata in parsed documents
- Query expansion/reformulation
- Add more evaluation questions
- Fine-tune similarity thresholds per question type

## License

This project is for educational purposes as part of the MS Computer Science program at [University Name].

## Acknowledgments

- HIPAA documentation from HHS.gov
- LlamaIndex framework
- OpenAI API for GPT-5 and embeddings

## Contact

For questions or issues, please open an issue on GitHub or contact the repository owner.