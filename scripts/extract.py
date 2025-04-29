import requests
import csv
import os

def extract_hal_publications(lang='fr', rows=1000, max_pages=20):
    os.makedirs("data", exist_ok=True)

    url = "https://api.archives-ouvertes.fr/search/"
    params = {
        'q': f'language_s:{lang}',
        'rows': rows,
        'wt': 'json',
        'fl': 'docid,title_s,authFullName_s,publicationDate_s,journalTitle_s,uri_s'
    }

    data = []
    start = 0
    page = 0

    while page < max_pages:
        params['start'] = start
        response = requests.get(url, params=params)

        print(f"\n➡️ Requête URL : {response.url}")
        print(f"📡 Statut HTTP : {response.status_code}")

        if response.status_code != 200:
            print("❌ Erreur HTTP")
            print(response.text)
            break

        try:
            json_data = response.json()
        except Exception as e:
            print(f"❌ Erreur JSON : {e}")
            break

        if 'response' not in json_data:
            print("❌ Structure inattendue")
            print(json_data)
            break

        docs = json_data['response']['docs']
        if not docs:
            print("✅ Fin de la pagination : aucun document.")
            break

        for doc in docs:
            data.append({
                'id': doc.get('docid', ''),
                'titre': doc.get('title_s', [''])[0],
                'auteur': '; '.join(doc.get('authFullName_s', [])),
                'annee': doc.get('publicationDate_s', '')[:4],
                'source': doc.get('journalTitle_s', [''])[0],
                'lien': doc.get('uri_s', [''])[0]
            })

        page += 1
        start += rows

    if data:
        with open("data/publications_raw.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

        print(f"\n✅ {len(data)} publications extraites et enregistrées.")
    else:
        print("⚠️ Aucune donnée extraite.")

# ✅ Appel auto
if __name__ == "__main__":
    extract_hal_publications()
