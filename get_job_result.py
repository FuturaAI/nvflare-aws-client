import requests
import base64
import os
from pathlib import Path
from zipfile import ZipFile
from dotenv import load_dotenv
import sys
load_dotenv()

# API configuration
BASE_URL = os.getenv("SERVER_URL")
# API_KEY = os.getenv("SERVER_API_KEY")  # Your API key
# HEADERS = {
#    "X-API-Key": API_KEY
# }

def download_job(job_id: str, output_dir: str):
   # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
   
    try:
       # Get base64 encoded zip
        response = requests.get(
                f"{BASE_URL}/jobs/{job_id}/download",
                # headers=HEADERS
                )
        response.raise_for_status()  # Raises exception for 4XX/5XX status codes
        
        # Decode base64 to bytes
        zip_bytes = base64.b64decode(response.json()["data"])
        
        # Save zip file
        output_file = os.path.join(output_dir, f"workspace_{job_id}.zip")
        with open(output_file, "wb") as f:
            f.write(zip_bytes)
            
        print(f"Downloaded to {output_file}")
       
    except requests.exceptions.RequestException as e:
        print(f"Error downloading job: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 get_job_result.py <job-id>")
        sys.exit(1) 

    job_id = sys.argv[1]
    output_dir = "downloads"  # Directory where files will be saved
    download_job(job_id, output_dir)
    
    with ZipFile(f"downloads/workspace_{job_id}.zip", 'r') as zip_ref:
        zip_ref.extractall(f"downloads/{job_id}")