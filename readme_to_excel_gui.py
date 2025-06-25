# ✅ Step 1: Install required library
!pip install -q pandas openpyxl

# ✅ Step 2: Upload your README.md file
from google.colab import files
uploaded = files.upload()

# ✅ Step 3: Extract question-answer from README
import re
import pandas as pd

# Get uploaded file name
readme_filename = list(uploaded.keys())[0]

# Read file content
with open(readme_filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Regex to match Question and Answer format
pattern = r"###\s*(\d+)\.\s*(.*?)\n\*\*Answer:\*\*\s*(.*?)\n(?=###|\Z)"
matches = re.findall(pattern, content, re.DOTALL)

# Prepare data
data = [{'Question': q.strip(), 'Answer': a.strip()} for _, q, a in matches]
df = pd.DataFrame(data)

# ✅ Step 4: Save as Excel
output_file = "laravel_interview_questions_with_answers.xlsx"
df.to_excel(output_file, index=False)

# ✅ Step 5: Download the Excel file
files.download(output_file)
