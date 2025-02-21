# PDF Batch Downloader Script

This Python script is designed to extract and download PDF files from a list of URLs or HTML pages. It works by finding all links to PDF files on the given pages and downloading them in parallel using threading to speed up the process. It also logs the download progress and errors for troubleshooting.

## Features
- Extracts PDF links from provided URLs or HTML files.
- Downloads PDF files in parallel using threading for faster downloads.
- Saves the PDFs in a folder named `DownloadedPdfs/`.
- Logs download progress and errors in `download_progress.log`.

## Usage
You can use the script in two ways: via command-line arguments or interactively.

### 1. **Command-Line Usage**
You can run the script with URLs as command-line arguments to start downloading PDFs:

```bash
python pdf_batch_downloader.py https://doi.org/10.1038/s41592-021-01128-0 https://example.com
```

### 2. **Interactive Usage**

If you don’t want to pass URLs as command-line arguments, you can run the script without them, and it will prompt you to enter URLs manually:

```bash
python pdf_batch_downloader.py
```

Then, you can input a comma-separated list of URLs or HTML filenames. For example:

```bash
https://doi.org/10.1038/s41592-021-01128-0, https://example.com
```

The script will automatically extract and download all PDFs from the provided links.

## File Structure
- `pdf_batch_downloader.py` – The main Python script for downloading the PDFs.
- `download_progress.log` – The log file that records the download progress and any errors.
- `DownloadedPdfs/` – The folder where the downloaded PDF files are saved.

## Logging
All download progress and errors are recorded in the `download_progress.log` file. You can check this file for information about the success or failure of downloads.
