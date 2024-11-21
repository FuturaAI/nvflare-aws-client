# NVFlare AWS Client setup

Simple Python scripts to download sites and job results from an API server.

## Prerequisites

- Python 3.x

Install dependencies:
```bash
pip install requests python-dotenv
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

## Scripts

### get_client.py
Downloads a site as a ZIP file.

```bash
python get_client.py <site-id>
unzip downloads/site-<site-id>.zip -d /<site-id>
```

### get_job_result.py
Downloads and extracts job results.

```bash
python get_job_result.py <job-id>
```

## Output

Files are saved to the `downloads` directory:
- Site downloads: `downloads/site-<site-id>.zip` (manually unzip using command above)
- Job results: `downloads/workspace_<job-id>.zip` (automatically extracted to `downloads/<job-id>/`)