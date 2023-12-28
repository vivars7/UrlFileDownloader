# File Downloader Script from URLs

## Description

This Python script is designed to download files from URLs listed in a text file. It reads each URL from the specified text file and downloads the files to a designated output folder, automatically creating the directory structure if it does not exist.

## Requirements

- Python 3.x
- `requests` library

Please ensure Python 3.x is installed on your system. You can install the required `requests` library using the following command:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should contain:

```
requests
```

## URL File Format (`url.txt`)

Create a text file named `url.txt` and list each URL on a new line. For example:

```
https://example.com/file1.jpg
https://example.com/file2.pdf
http://example.com/file3.png
```

## Output Folder

The script will download the files to the specified output folder (`d:\temp\downloads` by default). If the folder does not exist, the script will create it along with the necessary subdirectories.

## Running the Script

To run the script, use the following command in the terminal:

```bash
python download_script.py
```

Ensure that the `url.txt` file is in the same directory as the script or provide the correct path to it in the script.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
