# DataEye

DataEye is an intelligent Python library that automatically analyzes tabular data using a large language model (LLM). It scans your dataset, extracts column information, and generates insightful interpretations.

## Features
- Reads CSV and Excel files from a directory
- Extracts column names and first three rows for quick analysis
- Uses an LLM (e.g., GPT-4) to generate insights about the data
- Saves analysis results in JSON or HTML format

## Installation
```bash
pip install dataeye
```

## Usage
```python
import dataeye as eye

eye.see("path/to/data_folder")
```
This will generate a structured analysis of all tabular files in the specified folder.

## Output Options
- **JSON:** Stores insights in a machine-readable format
- **HTML:** Generates a human-friendly report for easy visualization

## Author
Developed by **Suat ATAN**.

## License
MIT License

