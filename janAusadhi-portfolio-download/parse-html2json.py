import json
import argparse
from bs4 import BeautifulSoup

def html_table_to_json(html_string):
    """
    Parses an HTML table string and returns a JSON formatted string.

    Args:
        html_string: An HTML string containing table rows (divs with role="row" and class "rdt_TableRow")
                     and cells (divs with role="cell" and class "rdt_TableCell").

    Returns:
        A JSON formatted string representing the table data.
    """
    soup = BeautifulSoup(html_string, 'html.parser')
    rows = soup.find_all(role="row", class_="rdt_TableRow")
    json_output = []
    column_names = ["id", "drug_code", "generic_name", "unit_size", "price", "group_name"]
    for row in rows:
        cells = row.find_all(role="cell", class_="rdt_TableCell")
        row_values = {}
        for index, cell in enumerate(cells):
            text = cell.text.strip()
            if index < len(column_names):
                row_values[column_names[index]] = text
            else:
                row_values[f"col{index+1}"] = text # in case there are more columns than expected
        json_output.append(row_values)
    return json.dumps(json_output, indent=2)

def parseInput(fileName):
    html_content = ''
    try:
        with open(fileName, 'r') as f:
            html_content = ''.join(f.readlines())
            return html_content
    except FileNotFoundError:
        print(f"Error: File '{fileName}' not found.")
        return

def main():
    parser = argparse.ArgumentParser(description="Parse HTML table to JSON.")
    parser.add_argument("-f", "--filename", default="index.html", help="HTML file to parse (default: index.html)")
    parser.add_argument('-o','--outfile',default='parsed-json.json',help='output file for json(default: parsed-json.json)')
    args = parser.parse_args()

    filename = args.filename
    outFile = args.outfile

    html_content = parseInput(filename)
    #print(type(html_content))

    json_output_string = html_table_to_json(html_content)
    #print(json_output_string)

    with open(outFile, 'w') as outfile:
        outfile.write(json_output_string)
    print(f"JSON output saved to {outFile}")


if __name__ == '__main__':
    main()