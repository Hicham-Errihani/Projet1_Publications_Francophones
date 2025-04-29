import pandas as pd
import os

def export_txt_for_nvivo():
    try:
        df = pd.read_csv("data/publications_clean.csv")
    except Exception as e:
        print(f"❌ Erreur lors de la lecture du CSV : {e}")
        return

    if df.empty:
        print("⚠️ Le fichier CSV est vide.")
        return

    os.makedirs("nvivo_txt", exist_ok=True)

    print(f"Nombre de publications à exporter : {len(df)}")

    count = 0
    for i, row in df.iterrows():
        try:
            filename = f"nvivo_txt/pub_{i:04d}_{row['annee']}.txt"
            with open(filename, "w", encoding="utf-8-sig") as f:
                f.write(f"Titre : {row.get('titre', 'N/A')}\n")
                f.write(f"Auteur(s) : {row.get('auteur', 'N/A')}\n")
                f.write(f"Source : {row['source'] if pd.notna(row['source']) else 'N/A'}\n")
                f.write(f"Lien : {row.get('lien', 'N/A')}\n")
            count += 1
        except Exception as e:
            print(f"❌ Erreur à la ligne {i} : {e}")

    print(f"✅ {count} fichiers exportés avec succès dans le dossier nvivo_txt/")

if __name__ == "__main__":
    export_txt_for_nvivo()
