import pandas as pd
import matplotlib.pyplot as plt
import os

def analyze_publications():
    # 📂 Créer le dossier de sortie si besoin
    os.makedirs("outputs", exist_ok=True)

    source_file = "data/publications_clean.csv"
    if not os.path.exists(source_file):
        print("❌ Fichier nettoyé introuvable.")
        return

    df = pd.read_csv(source_file)

    # 📊 Graphe : publications par année
    plt.figure(figsize=(10, 6))
    df['annee'] = df['annee'].astype(str)
    df['annee'].value_counts().sort_index().plot(kind='bar')
    plt.title("📚 Publications par année")
    plt.xlabel("Année")
    plt.ylabel("Nombre de publications")
    plt.tight_layout()
    plt.savefig("outputs/publications_par_annee.png")
    plt.close()

    # 🥧 Graphe circulaire : Top 5 sources
    top_sources = df['source'].value_counts().head(5)
    plt.figure(figsize=(6, 6))
    top_sources.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title("🔝 Top 5 Sources de publication")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("outputs/publications_par_source.png")
    plt.close()

    print("✅ Graphiques générés dans le dossier outputs/.")

# ✅ Appel automatique
if __name__ == "__main__":
    analyze_publications()
