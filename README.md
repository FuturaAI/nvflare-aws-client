# NVFlare AWS Client Setup
Simple Python scripts to download sites and job results from an API server.

## Prerequisites
- Python 3.x
- CUDA (GPU support)

Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration
1. Copy `.env.default` to `.env`:
```bash
cp .env.default .env
```

2. Edit `.env` with your server details:
```
SERVER_URL="http://<server-ip>:<port>"
```

## Starting NVFlare Client
1. Download and extract client:
```bash
python get_client.py <site-id>
unzip downloads/site-<site-id>.zip -d /<site-id>
```

2. Start the client:
```bash
cd /<site-id>/startup/
./start.sh
```

## Project Structure
```
.
├── downloads/                   # Downloaded files directory
├── notebooks/                   # Notebooks directory
│   └── advanced_nvflare/       # Advanced NVFlare notebooks
│       ├── models/             # Trained models directory
│       ├── tenseal_context/    # Encryption contexts
│       ├── test/               # Test dataset
│       ├── nvflare_inference.ipynb
│       └── nvflare_inference_HE.ipynb
├── get_client.py               # Site download script
├── get_job_result.py           # Job results download script
├── requirements.txt            # Python dependencies
└── .env.default                # Environment template
```

## Job Results
Downloads and extracts job results:
```bash
python get_job_result.py <job-id>
```

## Output
Files are saved to the `downloads` directory:
- Site downloads: `downloads/site-<site-id>.zip`
- Job results: `downloads/workspace_<job-id>.zip` (automatically extracted to `downloads/<job-id>/`)

## Notebooks
See `notebooks/advanced_nvflare/README.md` for details on available notebooks for inference with standard and homomorphic encryption (HE) models. The downloaded job results contain trained models that can be tested using these notebooks - just copy the model files from `downloads/<job-id>/` to `notebooks/advanced_nvflare/models/` to get started.