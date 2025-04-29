from extract import extract_hal_publications
from clean import clean_publications
from analyze import analyze_publications
from nvivo_export import export_txt_for_nvivo

def run_project():
    extract_hal_publications()
    clean_publications()
    analyze_publications()
    export_txt_for_nvivo()

if __name__ == "__main__":
    run_project()
