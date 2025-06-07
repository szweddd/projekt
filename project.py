import sys
import os
import json
import yaml

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

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            if input_path.endswith('.json'):
                data = json.load(file)
                print("Plik .json został poprawnie wczytany.")
            elif input_path.endswith(('.yml', '.yaml')):
                data = yaml.safe_load(file)
                print("Plik .yml został poprawnie wczytany.")
            else:
                print("Błąd: Nieobsługiwany format wejściowy.")
                sys.exit(1)
                
    except json.JSONDecodeError as e:
        print(f"Błąd składni JSON: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Błąd: plik {input_path} nie istnieje.")
        sys.exit(1)
    except Exception as e:
        print(f"Inny błąd: {e}")
        sys.exit(1)
    if output_path.endswith('.json'):
        try:
            with open(output_path, 'w', encoding='utf-8') as outfile:
                json.dump(data, outfile, indent=4, ensure_ascii=False)
                print(f"Zapisano dane do pliku {output_path}")
        except Exception as e:
            print(f"Błąd podczas zapisu do pliku .json: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()