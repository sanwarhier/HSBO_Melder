# HSBO_Melder

## Client
Die Datei `map.html` kann einfach als Datei im Browser geöffnet werden. 

Oder, falls Visual Studio Code verwendet wird, mit der Live Server Extension (Rechtsklick auf die Datei -> Open with Live Server). Das hat den Vorteil, dass die Seite sich bei Änderungen im Skript automatisch aktualisiert.

Um das Aussehen auf Mobilgeräten zu simulieren, kann in den meisten Browsern unter Rechtsklick -> Untersuchen eine Gerätesymbolleiste / Geräteemulation geöffnet werden
![](2024-04-19%2016_08_55-Window.png)


## Server
Die Python-Datei kann zum Entwickeln einfach lokal ausgeführt werden.

## Datenbank
Am schnellsten kann man eine einfache Postgis-DB über Docker starten mit dem Befehl 

    docker run -p 5432:5432 --name postgis-leermelder -e POSTGRES_PASSWORD=mysecretpassword -d postgis/postgis

Weitere Infos: https://github.com/postgis/docker-postgis

Anschließend kann das Python-Skript `init_points.py` ausgeführt werden, um eine Tabelle `points` mit einem ersten Punkt darin anzulegen.