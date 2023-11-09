import os
import re
import PyPDF2
import shutil
from multiprocessing import Pool, cpu_count
import json


direc = ""
target_dir = ""


def get_pdf_keywords(filename, keywords_pattern, directory=direc):
    pdf_path = os.path.join(directory, filename)
    matches = []

    try:
        with open(pdf_path, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            num_pages = len(pdf_reader.pages)

            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                page_content = page.extract_text()

                for match in keywords_pattern.finditer(page_content):
                    matches.append(
                        {"filename": filename, "page_num": page_num, "keyword": match.group(0).lower()})

        return matches
    except Exception as e:
        print(f"Erro ao processar {filename}: {e}")
        return []


def consolidate_results(all_results_flat):
    consolidated_results = {}
    for result in all_results_flat:
        filename = result["filename"]
        page_num = result["page_num"]
        keyword = result["keyword"]

        if filename not in consolidated_results:
            consolidated_results[filename] = {
                "filename": filename, "page_num": [], "keyword": []}

        consolidated_results[filename]["page_num"].append(page_num + 1)
        if keyword not in consolidated_results[filename]["keyword"]:
            consolidated_results[filename]["keyword"].append(keyword)

    return list(consolidated_results.values())


def main():
    directory = direc
    target_directory = target_dir

    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    keywords = [
       r"exemplo",
    ]

    keywords_pattern = re.compile('|'.join(keywords), re.IGNORECASE)

    filenames = [f for f in os.listdir(directory) if f.endswith('.pdf')]
    args_list = [(filename, keywords_pattern) for filename in filenames]

    with Pool(cpu_count()) as pool:
        all_results = pool.starmap(get_pdf_keywords, args_list)

    all_results_flat = [item for sublist in all_results for item in sublist]
    consolidated_data = consolidate_results(all_results_flat)

    with open('results.json', 'w') as f:
        json.dump(consolidated_data, f, indent=4)

    moved_files = set()
    for result in consolidated_data:
        filename = result["filename"]
        if filename not in moved_files:
            source_path = os.path.join(directory, filename)
            destination_path = os.path.join(target_directory, filename)
            shutil.move(source_path, destination_path)
            moved_files.add(filename)


if __name__ == '__main__':
    main()
