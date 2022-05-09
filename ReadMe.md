1. rechteck.py und punkt.py als separate skripte
2. ein main.py schreiben, das aus diesen "modulen" importiert und das programm ausführt
3. korrekte verwendung von `if __name__ == "__main__": ...`.
4. tests schreiben: pytest installieren, was muss ich machen um überhaupt einen test zum laufen zu bekommen? (hinweis: pytest durchsucht bestimmte verzeichnisse, eventuell muss man ihm explizit sagen welche datei die tests beinhaltet)
5. wenn die tests funktionieren, schreibe typen anotations. teste mit mypy/pytest ob main.py passt. Provoziere einen Fehler, findet ihn mypy/pytest?
6. source code hübsch machen: lass black oder yapf über deine skripte laufen.
7. Dokumentation: Sphinx soll aus deinem Paket heraus es schaffen, ein paar HTML Dateien zu generieren.
