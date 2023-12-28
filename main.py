import requests
import os
from urllib.parse import urlparse, unquote

def download_file(url, output_folder):
    response = requests.get(url)
    if response.status_code == 200:
        parsed_url = urlparse(url)
        path = unquote(parsed_url.path)
        file_path = os.path.join(output_folder, path.lstrip("/"))
        
        # Create directories if they don't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Downloaded {file_path}")
    else:
        print(f"Failed to download from URL {url}")

def main():
    txt_file = "url.txt"  # TXT file name
    output_folder = r"d:\temp\downloads"  # path for downloads

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        with open(txt_file, "r") as file:
            url_list = file.read().splitlines()

        for url in url_list:
            download_file(url, output_folder)
    except FileNotFoundError:
        print(f"File {txt_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
