import os
import pandas as pd
import json
import aisuite as ai

def read_directory_files(directory):
    """
    Reads all CSV and Excel files in a given directory, extracts column names and the first three rows,
    and returns the data as a JSON string.
    """
    data_dict = {}

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if filename.endswith(".csv"):
            df = pd.read_csv(filepath)
        elif filename.endswith(".xlsx") or filename.endswith(".xls"):
            df = pd.read_excel(filepath)
        else:
            continue

        columns = df.columns.tolist()
        values = df.head(3).to_dict(orient='records')

        data_dict[filename] = {"columns": columns, "values": values}

    return json.dumps(data_dict, indent=4, ensure_ascii=False)

def analyze_json(json_data, model="openai:gpt-4"):
    """
    Uses an LLM model to analyze column names and the first three rows of data,
    providing a description of what the table might represent.
    """
    data = json.loads(json_data)
    
    client = ai.Client()

    analysis = {}
    for file_name, content in data.items():
        columns = content['columns']
        values = content['values']

        messages = [
            {"role": "system", "content": "Analyze the given table based on column names and the first three rows of values."},
            {"role": "user", "content": f"Column names: {columns}\nFirst three rows: {values}"}
        ]

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7
        )

        analysis[file_name] = response.choices[0].message.content

    return json.dumps(analysis, indent=4, ensure_ascii=False)

def save_output(json_data, output_format="json", output_path="analysis_output"):
    """
    Saves the analysis output either as a JSON file or an HTML report.
    """
    if output_format == "json":
        with open(f"{output_path}.json", "w", encoding="utf-8") as f:
            f.write(json_data)
    elif output_format == "html":
        html_content = "<html><body><h1>Analysis Report</h1><pre>" + json_data + "</pre></body></html>"
        with open(f"{output_path}.html", "w", encoding="utf-8") as f:
            f.write(html_content)
    else:
        raise ValueError("Unsupported format. Choose either 'json' or 'html'.")

# Example usage
if __name__ == "__main__":
    directory_path = "data"
    json_output = read_directory_files(directory_path)
    analysis_output = analyze_json(json_output)
    save_output(analysis_output, output_format="json")
