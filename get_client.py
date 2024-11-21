import requests
import os
from pathlib import Path
from dotenv import load_dotenv
import sys
from zipfile import ZipFile

load_dotenv(dotenv_path=".env")

# API configuration
BASE_URL = os.getenv("SERVER_URL")
# API_KEY = "your_api_key_here"  # Replace with your API key
# HEADERS = {
#    "X-API-Key": API_KEY
# }

def download_site(site_id: str, output_dir: str):
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    try:
        # Download zip file
        response = requests.get(
            f"{BASE_URL}/download/site/{site_id}", 
            #    headers=HEADERS,
            stream=True  # Good for large files
        )
        response.raise_for_status()
        
        # Save zip file
        output_file = os.path.join(output_dir, f"site-{site_id}.zip")
        with open(output_file, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                
        print(f"Downloaded to {output_file}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading site: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 get_client.py <site_id>")
        sys.exit(1)
        
    site_id = sys.argv[1]
    output_dir = "downloads"
    download_site(site_id, output_dir)

    with ZipFile(f"downloads/site-{site_id}.zip", 'r') as zip_ref:
        zip_ref.extractall(f"./site-{site_id}")