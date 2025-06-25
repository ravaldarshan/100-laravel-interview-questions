import pandas as pd
from google.colab import files

uploaded = files.upload()  # Upload your Excel file here

filename = list(uploaded.keys())[0]
df = pd.read_excel(filename)

with open("README.md", "w", encoding="utf-8") as f:
    for i, row in df.iterrows():
        f.write(f"### {i+1}. {row['Question']}\n")
        f.write(f"**Answer:** {row['Answer']}\n\n")

files.download("README.md")