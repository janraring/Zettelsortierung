# Landschaften, Kreise, Orte

**Auf dieser Seite behandelte Dateien:**
- `data/raw/KreiseOrte.html`
- `data/processed/Landschaften.csv`
- `data/processed/Kreise.csv`
- `data/processed/Orte.csv`
- `notebooks/01_KreiseOrte.csv`


## Datenquelle
Die Daten zu den Landschaften, Kreisen und Orten stammen aus dem Beiband des Westfälischen Wörterbuchs. Sie sind im [Trierer Wörterbuchnetz](https://www.woerterbuchnetz.de/Woerterbuecher/WWB/KreiseOrte.html) digital abrufbar. Im übrigen ist dort folgende nähere Erklärung zu den Ortsangaben zu finden.

> Die Kreise werden im nachfolgenden Verzeichnis wie auf der beigefügten Karte mit drei, die Orte innerhalb der Kreise mit zwei Buchstaben abgekürzt, z. B. Arn En Mü, Sos Am, d. h. Endorf und Müschede im Kreise Arnsberg, Ampen im Kreise Soest. Ein vom Gewährsmann nicht namentlich genannter Ort im Kreise wird mit Xy bezeichnet. Eine Kreisangabe ohne folgenden Ort bedeutet, daß das betreffende Wort bzw. die betreffende Wortform aus dem genannten Kreis öfter belegt ist.
>
> In einigen Fällen wurden mehrere kreisfreie Städte unter einer einheitlichen Abkürzung zusammengefaßt, z. B. Bochum, Herne und Wattenscheid zu Bch = Bochum, ebenso die westfälisch sprechenden Teile des Bergischen Landes, genauer der kreisfreien Stadt Wuppertal und des Rhein-Wupper-Kreises, als Brg, die niederdeutsch sprechenden Teile der Kreise Waldeck und Frankenberg als Wal.
>
>Vereinzelt konnten kleinere Abweichungen von der heutigen Kreiszugehörigkeit nicht mehr berücksichtigt werden. Im übrigen gelten die Grenzen des Jahres 1967.
>
>Bei Bauerschaften und kleineren Orten werden im nachfolgenden Verzeichnis in () Hinweise auf die Ortslage gegeben.
>
>Mit dem Zeichen = wird darauf hingewiesen, daß der jeweilige Ort unter zwei verschiedenen Signaturen erscheint. Das Zeichen → bedeutet: der Ort ist auf der Karte unter dem angegebenen Kreis zu suchen. Die mit * bezeichneten Orte sind nicht in der Karte eingezeichnet.

Die oben verlinkte Seite im Wörterbuchnetz ist als `data/raw/KreiseOrte.html` gespeichert worden und dient der Generierung von Ortslisten als Grundlage.


## Datenverarbeitung

Die Datenverarbeitung wird in `notebooks/01_KreiseOrte.ipynb` vorgenommen....

Die HTML-Seite ist runtergeladen worden und befindet sich in `data/raw`. In dem Notebook `01_KreiseOrte` wird aus der HTML-Seite jeweils eine Tabelle für Kreise und Orte generiert. Die Tabelle der Landschaften ist manuell erstellt.


## Todo
- Dokumentation vervollständigen
- Angaben der Form Kre Xy müssten noch irgendwie berücksichtigt werden.