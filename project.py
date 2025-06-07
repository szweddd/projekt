import sys
import os

def validate_file_extension(filename):
    valid_extensions = ['.json', '.xml', '.yml', '.yaml']
    _, ext = os.path.splitext(filename)
    return ext.lower() in valid_extensions

def main():
    if len(sys.argv) != 3:
        print("Użycie: python project.py plik_wejsciowy plik_wyjsciowy")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    if not validate_file_extension(input_path) or not validate_file_extension(output_path):
        print("Błąd: obsługiwane formaty to .json, .xml, .yml, .yaml")
        sys.exit(1)

    print(f"Plik wejściowy: {input_path}")
    print(f"Plik wyjściowy: {output_path}")

if __name__ == "__main__":
    main()