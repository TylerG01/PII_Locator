import csv
import re
import os

# Change these directories
INPUT_DIR = "input_data"
OUTPUT_DIR = "output_data"
OUTPUT_FILE = "pii_matches.txt"

# Define regex patterns for PII detection
patterns = {
    "Full Name": re.compile(r"\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+\b"),
    "National ID (Generic)": re.compile(r"\b[A-Z]?\d{6,12}[A-Z]?\b"),

    # Country-Specific National ID# for US, CA, AUS and 24 european countries
    "National ID Number": re.compile(
        r"""\b(
            \d{3}-\d{2}-\d{4} |
            \d{3}-\d{3}-\d{3} |
            \d{6}[-/]\d{3,4} |
            \d{11,13} |
            [A-Z]{1,2}\d{6,9} |
            \d{2}[0-1]\d[0-3]\d-\d{3}-\d{2} |
            \d{6}[-+]\d{4} |
            [3-6]\d{10} |
            \d{10}
        )\b""", re.VERBOSE
    ),

    # Phone number for any coutnry
    "Phone Number": re.compile(
        r"""(?x)
        (?:(?:\+|00)\d{1,3}[\s.-]?)?
        (?:\(?\d{1,4}\)?[\s.-]?)?
        \d{2,4}[\s.-]?\d{2,4}[\s.-]?\d{2,4}
        """
    ),

    # Passport Numbers (by country) for the US, Canada, Australia and 24 European countries
    "Passport Number": re.compile(
        r"""\b(
            \d{9} |
            [A-Z]{2}\d{6,7} |
            [A-Z]{1}\d{7} |
            \d{2}[A-Z]{1,2}\d{5} |
            [C-F][A-Z0-9]{8} 
        )\b""", re.VERBOSE
    ),
    
    # Generatic
    "Driver License": re.compile(r"\b[A-Z0-9]{5,15}\b"),
    "Address": re.compile(r"\d+\s+[A-Za-z]+\s+(Street|St|Road|Rd|Avenue|Ave|Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct|Way|Square|Sq|Trail|Trl|Parkway|Pkwy|Commons)\b", re.IGNORECASE),
    "IP Address": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "MAC Address": re.compile(r"\b(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})\b"),
    "IMEI": re.compile(r"\b\d{15}\b"),
    "Race/Ethnicity": re.compile(r"\b(Asian|Black|White|Hispanic|Latino|Indigenous|Native American|Pacific Islander|Middle Eastern|Multiracial)\b", re.IGNORECASE),
    "Gender": re.compile(r"\b(Male|Female|Non-binary|Other|Transgender|Intersex)\b", re.IGNORECASE)
}

def line_contains_pii(row):
    joined = " ".join(row)
    for label, pattern in patterns.items():
        if pattern.search(joined):
            return True
    return False

def extract_pii_from_csv_file(csv_path, output_file):
    with open(csv_path, mode="r", newline='', encoding="utf-8") as infile:
        reader = csv.reader(infile)
        for row in reader:
            if line_contains_pii(row):
                output_file.write(",".join(row) + "\n")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)

    with open(output_path, mode="w", encoding="utf-8") as out_file:
        for filename in os.listdir(INPUT_DIR):
            if filename.endswith(".csv"):
                csv_path = os.path.join(INPUT_DIR, filename)
                print(f"🔍 Processing: {csv_path}")
                extract_pii_from_csv_file(csv_path, out_file)

    print(f"\nAll matches saved to: {output_path}")

if __name__ == "__main__":
    main()
