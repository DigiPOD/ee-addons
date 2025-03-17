#!/usr/bin/env python3

import argparse
import csv
import os
import re

import requests

DIGIPOD_CONCEPT_OFFSET = 2000000000
vocab_id = "DIGIPOD"


def to_variable_name(s: str) -> str:
    """
    Convert a concept_name to a valid Python identifier:
    1) Convert to uppercase.
    2) Replace all non-alphanumeric characters with underscores.
    3) If the resulting name starts with a digit, replace that digit with its word equivalent.
    """
    # Convert to uppercase and replace non-alphanumeric characters with underscores.
    var_name = re.sub(r"[^\w]+", "_", s.upper()).strip("_")

    # Mapping for digits to their word equivalents.
    digit_mapping = {
        "0": "ZERO",
        "1": "ONE",
        "2": "TWO",
        "3": "THREE",
        "4": "FOUR",
        "5": "FIVE",
        "6": "SIX",
        "7": "SEVEN",
        "8": "EIGHT",
        "9": "NINE",
    }

    # If the name starts with a digit, replace it with the corresponding word.
    if var_name and var_name[0].isdigit():
        var_name = digit_mapping[var_name[0]] + var_name[1:]

    return var_name


def main() -> None:
    """
    Read CUSTOM_CONCEPTS.csv from the DigiPOD ETL GitHub repo and generate Python code for custom concepts.
    """

    script_dir = os.path.dirname(os.path.realpath(__file__))
    default_output_path = os.path.join(script_dir, "../terminology/custom_concepts.py")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--github-url", help="Raw GitHub URL to the CSV file.", required=True
    )
    parser.add_argument(
        "--output-file",
        help="Path to the output Python file.",
        default=default_output_path,
    )
    args = parser.parse_args()

    response = requests.get(args.github_url, timeout=10)
    response.raise_for_status()
    lines = response.text.splitlines()

    reader = csv.reader(lines, delimiter=";")
    _ = next(reader)  # Skip the header row

    # Example header text to write at the top of the generated code file.
    header_text = (
        "# ------------------------------------------------------------\n"
        "# AUTO-GENERATED CONCEPT DEFINITIONS\n"
        "# DO NOT EDIT BY HAND\n"
        "# ------------------------------------------------------------\n\n"
        "from execution_engine.omop.concepts import Concept\n\n"
        f"DIGIPOD_CONCEPT_OFFSET = {DIGIPOD_CONCEPT_OFFSET}\n"
        f'vocab_id = "{vocab_id}"\n\n'
    )

    with open(args.output_file, "w", encoding="utf-8") as f:
        f.write(header_text)

        for row in reader:
            # Each row: concept_id, concept_name, domain_id, ...
            concept_id = int(row[0])
            concept_name = row[1]
            domain_id = row[2]
            concept_code = row[6]

            # Skip 'Relationship' if you don't want to generate code for them
            if domain_id == "Relationship":
                continue

            var_name = to_variable_name(concept_name)
            offset = concept_id - DIGIPOD_CONCEPT_OFFSET

            f.write(f"{var_name} = Concept(\n")
            f.write(f"    concept_id=DIGIPOD_CONCEPT_OFFSET + {offset},\n")
            f.write(f'    concept_name="{concept_name}",\n')
            f.write(f'    concept_code="{concept_code}",\n')
            f.write(f'    domain_id="{domain_id}",\n')
            f.write("    vocabulary_id=vocab_id,\n")
            f.write('    concept_class_id="Custom",\n')
            f.write(")\n\n")


if __name__ == "__main__":
    main()
