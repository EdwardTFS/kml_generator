import math

# środek okręgu
lat = 50.936667 # 50°56'12''N
lon = 16.861389 # 16°51'41''E

# promień okręgu w metrach
radius = 50

# liczba punktów na okręgu
num_points = 16

# kąt między kolejnymi punktami na okręgu
angle = 2 * math.pi / num_points

# tworzenie pliku KML
with open("punkty.kml", "w") as kml_file:
    # nagłówek pliku KML
    kml_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    kml_file.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
    kml_file.write('<Document>\n')

    # tworzenie punktów na okręgu
    for i in range(num_points):
        # obliczanie współrzędnych punktu na okręgu
        point_lat = lat + (radius * math.cos(i * angle))
        point_lon = lon + (radius * math.sin(i * angle))

        # tworzenie znacznika placemarker dla punktu
        kml_file.write('<Placemark>\n')
        kml_file.write('<name>Point {}</name>\n'.format(i+1))
        kml_file.write('<Point>\n')
        kml_file.write('<coordinates>{},{},0</coordinates>\n'.format(point_lon, point_lat))
        kml_file.write('</Point>\n')
        kml_file.write('</Placemark>\n')

    # tworzenie osi
    for i in range(8):
        # obliczanie kąta osi
        axis_angle = i * math.pi / 4

        # tworzenie punktów na osi
        for j in range(4):
            # obliczanie odległości punktu od środka okręgu
            distance = radius + j * 25

            # obliczanie współrzędnych punktu na osi
            point_lat = lat + (distance * math.cos(axis_angle))
            point_lon = lon + (distance * math.sin(axis_angle))

            # tworzenie znacznika placemarker dla punktu
            kml_file.write('<Placemark>\n')
            kml_file.write('<name>Axis {} Point {}</name>\n'.format(i+1, j+1))
            kml_file.write('<Point>\n')
            kml_file.write('<coordinates>{},{},0</coordinates>\n'.format(point_lon, point_lat))
            kml_file.write('</Point>\n')
            kml_file.write('</Placemark>\n')

    # zamknięcie pliku KML
    kml_file.write('</Document>\n')
    kml_file.write('</kml>\n')

print("Plik KML został wygenerowany.")
