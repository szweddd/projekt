# Projekt - Konwerter plików danych

- JSON (.json)  
- XML (.xml)  
- YAML (.yml / .yaml)

---

## Zawartość repozytorium

- project.py - główny program (wersja terminalowa)
- gui.py - wersja z graficznym interfejsem (dodatkowo)
- installResources.ps1 - instalacja wymaganych zależności
- test.json - przykładowy plik wejściowy
- wynik.xml - przykładowy plik wynikowy po konwersji
- .github/workflows/build-exe.yml - GitHub Actions do budowy .exe
- project.exe - zbudowany plik wykonywalny (generowany przez workflow)

---

## Przykład działania (konsola)


project.exe test.json wynik.xml 

* Upewnij się, że plik .json zawiera prawidłowy format JSON (z klamrami, cudzysłowami itd.) i jest w tej samej lokacji

---

## Wymagania

- Python 3.10+
- Pakiety:
    - pyyaml
    - json (standard)
    - xml.etree.ElementTree (standard)

Zależności mozna zainstalować automatycznie poprzez 

./installResources.ps1

---

## GUI

Dla wersji gui.py dostępna jest wersja tkinterowa - pozwala uruchomić program z graficznym interfejsem.
Dodatkowa część projektu.

---

## GitHub Actions

Repozytorium automatycznie buduje plik .exe z project.py po wypchnięciu zmian na main.

Wygenerowany plik project.exe jest dostępny jako artifact w zakładce Actions.

---

## Dokumentacja

Konfiguracja GitHub Actions została przygotowana na podstawie oficjalnej dokumentacji:

https://docs.github.com/en/actions

---

## Autor

Oskar 58081, informatyka 1rok, 2sem.
