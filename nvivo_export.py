# scripts/nvivo_export.py

import pandas as pd
import os

def export_txt_for_nvivo():
    df = pd.read_csv("data/publications_clean.csv")
    os.makedirs("nvivo_txt", exist_ok=True)

    for i, row in df.iterrows():
        filename = f"nvivo_txt/pub_{i:04d}_{row['annee']}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Titre : {row['titre']}\n")
            f.write(f"Auteur(s) : {row['auteur']}\n")
            f.write(f"Source : {row['source']}\n")
            f.write(f"Lien : {row['lien']}\n")

    print("✅ Fichiers NVivo exportés.")
