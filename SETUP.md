# Setup Instructions

## Prerequisites

### System Requirements
- Python 3.7 or higher
- 4GB RAM minimum (8GB recommended)
- 2GB free disk space
- Internet connection

### Required Accounts
1. **OpenAI Account** (Required)
   - Sign up at https://platform.openai.com/signup
   - Get API key from https://platform.openai.com/api-keys
   - Add credits to your account (minimum $5 recommended)

2. **Kaggle Account** (Optional, for datasets)
   - Sign up at https://www.kaggle.com
   - Get API credentials from https://www.kaggle.com/account

## Step-by-Step Setup

### 1. Clone the Repository

```bash
# Using HTTPS
git clone https://github.com/yourusername/phd_ai_workshop.git

# Using SSH
git clone git@github.com:yourusername/phd_ai_workshop.git

cd phd_ai_workshop
```

### 2. Set Up Python Environment

#### Option A: Using venv (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# Verify activation (should show venv path)
which python
```

#### Option B: Using conda
```bash
# Create conda environment
conda create -n phd_workshop python=3.9

# Activate environment
conda activate phd_workshop
```

### 3. Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install all requirements
pip install -r requirements.txt

# Verify installation
python -c "import openai; print('OpenAI installed successfully')"
```

### 4. Configure API Keys

#### OpenAI API Key
```bash
# Copy example environment file
cp .env.example .env

# Edit .env file
# On macOS/Linux:
nano .env

# On Windows:
notepad .env

# Add your API key:
# OPENAI_API_KEY=sk-...your_key_here...
```

#### Kaggle API (Optional)
```bash
# Create Kaggle directory
mkdir ~/.kaggle

# Create credentials file
echo '{"username":"your_username","key":"your_api_key"}' > ~/.kaggle/kaggle.json

# Set permissions (macOS/Linux only)
chmod 600 ~/.kaggle/kaggle.json
```

### 5. Verify Setup

Run the setup verification script:
```bash
python verify_setup.py
```

Or manually verify:
```python
# Test OpenAI connection
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=10
)
print("✅ OpenAI API working!")
```

### 6. Launch Jupyter Notebook

```bash
# Start Jupyter
jupyter notebook

# Or use Jupyter Lab
jupyter lab

# The browser should open automatically
# If not, navigate to http://localhost:8888
```

## Common Issues and Solutions

### Issue: `ModuleNotFoundError: No module named 'openai'`
**Solution**: 
```bash
pip install openai==0.28.1
```

### Issue: `openai.error.AuthenticationError`
**Solution**: 
- Check your API key is correct in `.env`
- Ensure you have credits in your OpenAI account
- Verify the key starts with `sk-`

### Issue: `jupyter: command not found`
**Solution**: 
```bash
pip install jupyter
# Or
python -m pip install jupyter
```

### Issue: Rate limiting errors
**Solution**: 
- Add delays between API calls
- Reduce batch size in notebooks
- Check your OpenAI usage limits

### Issue: Kaggle dataset download fails
**Solution**: 
```bash
# Install kagglehub
pip install kagglehub

# Or download manually from:
# https://www.kaggle.com/datasets/borapajo/food-choices
```

## Testing Your Setup

### Quick Test Script
Create `test_setup.py`:
```python
import sys
import importlib

required_packages = [
    'openai', 'pandas', 'numpy', 'matplotlib',
    'seaborn', 'tqdm', 'dotenv', 'PyPDF2'
]

print("Checking installed packages...")
for package in required_packages:
    try:
        importlib.import_module(package.replace('-', '_'))
        print(f"✅ {package}")
    except ImportError:
        print(f"❌ {package} - Please install with: pip install {package}")

print("\nChecking API key...")
import os
from dotenv import load_dotenv
load_dotenv()

if os.getenv('OPENAI_API_KEY'):
    print("✅ OpenAI API key found")
else:
    print("❌ OpenAI API key not found - Please add to .env file")
```

Run with:
```bash
python test_setup.py
```

## Workshop Day Checklist

Before the workshop, ensure:

- [ ] All notebooks open without errors
- [ ] API key is working
- [ ] You have at least $5 in OpenAI credits
- [ ] Jupyter notebook is accessible
- [ ] Sample data files are present
- [ ] Internet connection is stable

## Getting Help

- **GitHub Issues**: https://github.com/yourusername/phd_ai_workshop/issues
- **OpenAI Support**: https://help.openai.com
- **Kaggle Forums**: https://www.kaggle.com/discussions

## Next Steps

1. Open `workshop_notebook.ipynb` to start the main tutorial
2. Review the README for workshop overview
3. Check the cost optimization tips to manage API usage
4. Join the workshop Slack/Discord for live support

---

**Remember**: Never share your API keys publicly or commit them to Git!