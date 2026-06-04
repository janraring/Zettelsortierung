# Projekt Zettelsortierung

## Ausgangslage

Das Westfälische Wörterbuch (WWb) ist auf Grundlage eines umfangreichen Zettelarchivs entstanden. Das Archiv besteht aus ca. 1,35 Millionen Karteikarten (im Folgenden meist _Zettel_ genannt), die sich auf ein lautschriftliches Archiv (ca. 100.000 Zettel) und das eigentliche Belegearchiv (ca. 1,25 Millionen Zettel) aufteilen. Letzteres lässt sich in weitere Kategorien und Untersammlungen unterteilen. Eine genauere Erklärung hierüber liefert der zum WWb erschienene Beiband. Die vier wichtigsten Oberkategorien sind demnach die folgenden:
1. Kopien von Belegen aus dem lautschriftlichen Archiv,
2. Fragebogenabschrift,
3. Exzerpt aus schriftlichen Quellen,
4. Wortschatzsammlungen freiwilliger Mitarbeiter.

Viele Zettel sind mit einem Belegort versehen. Im Beiband und in der digitalen Fassung des WWb ist eine vollständige Liste aller Ortskürzel enthalten (siehe [_Landschaften — Kreise — Orte_](https://www.woerterbuchnetz.de/Woerterbuecher/WWB/KreiseOrte.html)). Ebenfalls im Beiband enthalten ist eine Aufschlüsselung der Fragebogen nach Serie, eine Liste der schriftlichen Quellen sowie eine Liste der wichtigsten freiwilligen Mitarbeiter (siehe [_Einführung: Zur Herkunft des Materials_](https://www.woerterbuchnetz.de/Woerterbuecher/WWB/Einf%C3%BChrung.html) sowie [_Quellen und Schrifttum_](https://www.woerterbuchnetz.de/Woerterbuecher/WWB/Quellen.html)).


## Projektziel und Lösungsansatz

In einem ersten Schritt der Digitalisierung sind die Zettel beider Archive vorder- und rückseitig eingescannt worden. Das Ziel des aktuellen Projektes bestand darin, den nächsten Schritt zur digitalen Aufbereitung dieses Datenschatzes zu gehen. Es galt, den Bestand in eine Datenbank zu überführen und soweit möglich für jeden Zettel die folgenden Metadaten zu erschließen:
1. zu welcher Oberkategorie der Zettel gehört,
2. zu welchem Ort der Zettel gehört,
3. für Fragebogen: zu welcher Serie der Fragebogen gehört,
4. für schriftliche Quellen: aus welcher Quelle der Beleg stammt.

Die Erschließung ebendieser Metadaten bildete die Hauptarbeit. Es sind hierzu zwei Ansätze verfolgt worden. Zum einen wurde automatische Zeichenerkennung (OCR) verwendet um das Zettelarchiv durchsuchbar zu machen. Wie zu erwarten war, reichte die Qualität der OCR alleine nicht aus, um eine Klassifizierung durchzuführen. Gerade bei handschriftlichen Notizen und insbesondere bei solchen, die in Sütterlin verfasst worden sind, stößt diese Technik an ihre Grenzen. Dennoch boten die Resultate eine hervorragende Grundlage, um im nächsten Schritt eine Sammlung manuell gelabelter Zettel aufzubauen. Diese wiederum dienten als Grundlage für das Training künstlicher neuronaler Netze zur Bilderkennung. Das ganze war ein iterativer Prozess, sodass die Qualität der automatischen Klassifizierungen nach und nach verbessert werden konnten.


## Ergebnis und Limitierungen

Das finale Modell ist mit 25.000 handgelabelten Zetteln trainiert worden, die sich auf 581 Klassen aufteilen. Auf einem Testdatensatz erreichte es eine Genauigkeit von ca. 93%. In der Praxis fällt die Genauigkeit etwas geringer aus, da ein gewisser Teil des Archives noch als _out of distribution_ anzusehen ist, d.h. einige Zettel gehören zu gar keiner der 581 im Training angesetzten Klassen. Am Ende ist das Modell auf alle 1.250.000 Zettel des Hauptarchivs angewandt und die Vorhersagen zusammen mit dem zugehörigen Maß an Vertrauenswürdigkeit (_confidence_) in einer Datenbank gespeichert worden. Einen weiteren Zugang zu den Daten bieten die zuvor erzeugten OCR-Ergebnisse und ein Satz auf diesen Ergebnissen beruhender Klassifizierungen nach Ort.

Die genaue Struktur der Datenbank und noch weitere Details zu den Daten selber sind dem nachfolgenden Kapitel zu entnehmen.

Der für das Projekt entwickelte Quellcode ist unter [github.com/janraring/Zettelsortierung](https://github.com/janraring/Zettelsortierung) veröffentlicht worden. Es muss jedoch betont werden, dass dies kein Teil des eigentlichen Projektergebnisses ist und daher keine Gewährleistung hierfür übernommen wird. Der Quellcode möge vor allem denjenigen nützen, die in Zukunft mit der Datenbank an sich oder mit den Archivdaten allgemein zu tun haben.


## Verwendete Technologien

- Zur Programmierung wurde Python 3.12 verwendet.
- Zur automatische Zeichenerkennung ist die Bilderkennungs-Bibliothek _OpenCV_ und ein künstliches Neuronales Netz aus der [PaddleOCRv5](https://huggingface.co/collections/PaddlePaddle/pp-ocrv5)-Familie zum Einsatz gekommen.
- Die Modelle zur automatischen Klassifizierung basieren auf [MobileNetV3-small](https://huggingface.co/docs/timm/models/mobilenet-v3).
- Für die manuelle Klassifizierung der Zettel ist eine graphische Benutzeroberfläche mit dem _NiceGUI_-Framework entwickelt worden.
- Die Datenbank selber verwendet SQL v3.45.1.

