# AI-Powered Academic Research Workshop 🎓

A comprehensive workshop demonstrating how to use AI tools (OpenAI GPT) for academic research tasks including literature reviews, paper analysis, and categorizing open-ended survey responses.

## 🌟 Features

- **Literature Review Automation**: Extract key information from academic papers
- **Batch Processing**: Analyze multiple papers in parallel
- **Open-Ended Response Categorization**: Automatically categorize qualitative survey data
- **Validation Tools**: Compare AI categorization with human coding
- **Real Dataset Examples**: Uses actual academic datasets from Kaggle

## 📚 Workshop Materials

### Notebooks

1. **`workshop_notebook.ipynb`** - Main workshop notebook covering:
   - Secure API key management
   - Basic API queries and testing
   - Single paper analysis
   - Batch processing with parallelization
   - Literature review synthesis

2. **`open_ended_categorization.ipynb`** - Advanced categorization notebook:
   - Download real Food Choices dataset from Kaggle
   - Categorize open-ended survey responses
   - Validate against existing human coding
   - Generate accuracy metrics and confusion matrices

3. **`api_calls (1).ipynb`** - Original examples with NBER papers

### Python Modules

- **`paper_processing.py`** - PDF download and text extraction utilities
- **`meta_analysis_processing.py`** - Advanced paper analysis with parallel processing

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- (Optional) Kaggle account for dataset access

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/phd_ai_workshop.git
cd phd_ai_workshop
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your API key:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

### Running the Workshop

1. Start Jupyter:
```bash
jupyter notebook
```

2. Open `workshop_notebook.ipynb` for the main tutorial

3. For advanced categorization, open `open_ended_categorization.ipynb`

## 📊 Datasets

### Food Choices Dataset
- **Source**: Kaggle ([borapajo/food-choices](https://www.kaggle.com/datasets/borapajo/food-choices))
- **Size**: 126 college students
- **Features**: 61 attributes including open-ended responses about comfort food
- **Use Case**: Categorizing qualitative survey responses

### NBER Working Papers
- **Source**: National Bureau of Economic Research
- **Use Case**: Literature review and paper analysis
- **Format**: PDF documents

## 💻 Code Examples

### Basic API Query
```python
import openai

def simple_query(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful research assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']
```

### Categorize Open-Ended Response
```python
def categorize_response(text, categories):
    # AI categorizes text into predefined categories
    # Returns category, confidence, and key phrases
    ...
```

## 📈 Workshop Learning Outcomes

By completing this workshop, you will be able to:

1. ✅ Set up and manage OpenAI API connections securely
2. ✅ Extract structured information from academic papers
3. ✅ Process multiple papers efficiently using batch operations
4. ✅ Categorize open-ended survey responses automatically
5. ✅ Validate AI outputs against human coding
6. ✅ Generate literature review syntheses
7. ✅ Calculate accuracy metrics and create visualizations

## 🔧 Configuration

### Environment Variables

Create a `.env` file with:
```
OPENAI_API_KEY=your_api_key_here
DEFAULT_MODEL=gpt-3.5-turbo
MAX_WORKERS=10
```

### Cost Optimization

- Use `gpt-3.5-turbo` for most tasks (10x cheaper than GPT-4)
- Implement caching to avoid repeated API calls
- Process in batches to optimize token usage
- Monitor usage with included token counting utilities

## 📝 Best Practices

### For Open-Ended Response Categorization

1. **Define Clear Categories**: Ensure categories are mutually exclusive and comprehensive
2. **Validate Results**: Always compare a subset with human coding
3. **Review Low Confidence**: Manually check responses with confidence < 0.7
4. **Iterative Refinement**: Adjust prompts based on validation results
5. **Document Everything**: Keep detailed records of coding schemes and decisions

### For Literature Reviews

1. **Start Small**: Test with a few papers before processing large batches
2. **Structure Extraction**: Define clear fields to extract
3. **Cross-Reference**: Validate important findings manually
4. **Citation Management**: Keep track of sources and page numbers

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for providing the GPT API
- Kaggle and Bora Pajo for the Food Choices dataset
- NBER for academic paper access
- The academic community for valuable feedback

## 📧 Contact

For questions or support, please open an issue on GitHub or contact the workshop organizer.

## 🔗 Useful Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [NBER Working Papers](https://www.nber.org/papers)
- [Best Practices for API Usage](https://platform.openai.com/docs/guides/best-practices)

---

**Note**: Remember to keep your API keys secure and never commit them to version control!