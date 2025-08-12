# AI-Powered Academic Research Workshop

Workshop materials for using OpenAI GPT to analyze academic papers and categorize open-ended survey responses.

## Quick Start

1. **Clone repository**
```bash
git clone https://github.com/yourusername/phd_ai_workshop.git
cd phd_ai_workshop
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Add OpenAI API key**
```bash
cp .env.example .env
# Edit .env with your API key
```

4. **Run notebooks**
```bash
jupyter notebook
```

## Workshop Contents

### Main Notebooks
- `workshop_notebook.ipynb` - Core tutorial for API usage and paper analysis
- `open_ended_categorization.ipynb` - Categorizing survey responses with validation

### Python Modules
- `paper_processing.py` - PDF text extraction
- `meta_analysis_processing.py` - Batch paper analysis

### Datasets
- Food Choices Survey (Kaggle) - 126 students' open-ended responses
- NBER Working Papers - Academic paper PDFs

## Requirements
- Python 3.7+
- OpenAI API key
- $5-10 OpenAI credits

## License
MIT