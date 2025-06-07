import tkinter as tk
from tkinter import filedialog, messagebox
import os
import json
import yaml
import xml.etree.ElementTree as ET
import threading


def convert_file(input_path, output_path):
    try:
        # Wczytywanie
        with open(input_path, 'r', encoding='utf-8') as file:
            if input_path.endswith('.json'):
                data = json.load(file)
            elif input_path.endswith(('.yml', '.yaml')):
                data = yaml.safe_load(file)
            elif input_path.endswith('.xml'):
                tree = ET.parse(file)
                root = tree.getroot()
                data = {child.tag: child.text for child in root}
            else:
                raise ValueError("Nieobsługiwany format wejściowy.")

        # Zapis
        if output_path.endswith('.json'):
            with open(output_path, 'w', encoding='utf-8') as outfile:
                json.dump(data, outfile, indent=4, ensure_ascii=False)
        elif output_path.endswith(('.yml', '.yaml')):
            with open(output_path, 'w', encoding='utf-8') as outfile:
                yaml.dump(data, outfile, allow_unicode=True)
        elif output_path.endswith('.xml'):
            root = ET.Element("root")
            for key, value in data.items():
                element = ET.SubElement(root, key)
                element.text = str(value)
            tree = ET.ElementTree(root)
            tree.write(output_path, encoding="utf-8", xml_declaration=True)
        else:
            raise ValueError("Nieobsługiwany format wyjściowy.")

        messagebox.showinfo("Sukces", f"Zapisano do pliku:\n{output_path}")

    except Exception as e:
        messagebox.showerror("Błąd", str(e))


def open_input_file():
    path = filedialog.askopenfilename()
    if path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, path)


def save_output_file():
    path = filedialog.asksaveasfilename(defaultextension=".json",
                                        filetypes=[("JSON", "*.json"),
                                                   ("YAML", "*.yml *.yaml"),
                                                   ("XML", "*.xml")])
    if path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, path)


def start_conversion():
    input_path = input_entry.get()
    output_path = output_entry.get()
    if not input_path or not output_path:
        messagebox.showwarning("Uwaga", "Podaj oba pliki.")
        return
    threading.Thread(target=convert_file, args=(input_path, output_path)).start()



# UI
root = tk.Tk()
root.title("Konwerter danych")
root.geometry("400x200")

tk.Label(root, text="Plik wejściowy:").pack()
input_entry = tk.Entry(root, width=50)
input_entry.pack()
tk.Button(root, text="Wybierz...", command=open_input_file).pack()

tk.Label(root, text="Plik wyjściowy:").pack()
output_entry = tk.Entry(root, width=50)
output_entry.pack()
tk.Button(root, text="Zapisz jako...", command=save_output_file).pack()

tk.Button(root, text="Konwertuj", command=start_conversion, bg="#4CAF50", fg="white").pack(pady=10)

root.mainloop()
