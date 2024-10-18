import os
import requests
import zipfile

# Function to download a file from a URL
def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

# Function to extract a zip file
def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

# URLs for downloading the zip files
app_zip_url = 'https://e-sh4rk.github.io/CodeGenerator/app.zip'
repo_zip_url = 'https://github.com/E-Sh4rk/EmeraldACE_web/archive/refs/heads/main.zip'

# File paths
app_zip_path = 'app.zip'
repo_zip_path = 'repo.zip'

# Directory paths
app_dir = 'app'
config_file_path = os.path.join(app_dir, 'config.js')

# Create the app directory if it doesn't exist
os.makedirs(app_dir, exist_ok=True)

# Download and extract app.zip
print(f"Downloading {app_zip_url}...")
download_file(app_zip_url, app_zip_path)
print(f"Extracting {app_zip_path} to {app_dir}...")
extract_zip(app_zip_path, app_dir)

# Download and extract repo.zip
print(f"Downloading {repo_zip_url}...")
download_file(repo_zip_url, repo_zip_path)
print(f"Extracting {repo_zip_path} to {app_dir}...")
extract_zip(repo_zip_path, app_dir)

# Write the config.js file
with open(config_file_path, 'w') as config_file:
    config_file.write('let repository = "EmeraldACE_web-main/"\n')
print(f"Configuration written at {config_file_path}")

# Clean
print(f"Cleaning...")
os.remove(app_zip_path)
os.remove(repo_zip_path)
