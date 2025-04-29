import pandas as pd
import os

def clean_publications():
    # ✅ Crée le dossier data s'il n'existe pas
    os.makedirs("data", exist_ok=True)

    source_file = "data/publications_raw.csv"
    cleaned_file = "data/publications_clean.csv"

    # ✅ Vérifie que le fichier brut existe
    if not os.path.exists(source_file):
        print("❌ Fichier publications_raw.csv introuvable.")
        return

    # ✅ Lecture du fichier brut
    df = pd.read_csv(source_file)

    # ✅ Nettoyage :
    df.drop_duplicates(subset='titre', inplace=True)          # Supprime les doublons par titre
    df = df[df['annee'].notna()]                              # Enlève les lignes sans année
    df['annee'] = df['annee'].astype(str).str[:4]             # Formate l’année sur 4 caractères
    df['date_scraping'] = pd.Timestamp.now().strftime('%Y-%m-%d')  # Ajoute la date de traitement

    # ✅ Sauvegarde du fichier nettoyé
    df.to_csv(cleaned_file, index=False)

    print(f"✅ {len(df)} publications nettoyées et enregistrées dans {cleaned_file}.")

# ✅ Appel automatique si exécuté directement
if __name__ == "__main__":
    clean_publications()
