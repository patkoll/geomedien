def mapping():
    import json
    import folium
    import requests
    import time

#### Daten request ueber API

    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson"
    param = dict()
    resp = requests.get(url=url, params = param)
    data = resp.json()  

    #### Daten saeubern 

    ln = []
    lt = []
    mag = []
    place = []
    utc_time = []

    for j in data["features"]:
        longi = j["geometry"]["coordinates"][0]
        lati = j["geometry"]["coordinates"][1]
        magni = j["properties"]["mag"]
        ort = j["properties"]["place"]
        utc = time.ctime(j["properties"]["time"]/1000) # Unixzeit in UTC umwandeln
        lt.append(longi)
        ln.append(lati)
        mag.append(magni)
        place.append(ort)
        utc_time.append(utc)

    #### Karte erstellen ######

    map = folium.Map(location=[52.521918, 13.413215], zoom_start=2)
    fg = folium.FeatureGroup(name="Erdbeben")

    def colour(magnitude):
        if magnitude is not None:
            if magnitude < 4:
                return "green"
            elif 4 <= magnitude < 6:
                return "yellow"
            else:
                return "#FF0000"
        else:
            pass
    
    def radien(magnitude):
        if magnitude is not None:
            return magnitude**3/15
        else:
            pass
      
    for lon, lat, plc, mg, utctime in zip(ln,lt, place, mag, utc_time):
        fg.add_child(folium.CircleMarker(location=[lon,lat],tooltip= str(plc),
                                        popup=folium.Popup("Magnitude: " + str(mg)+"\n"+"Zeitpunkt: " + utctime), 
                                        fill_color = colour(mg),color="grey",fill_opacity=0.6, radius = radien(mg)))

    map.add_child(fg)
    return map.save("/Users/hoangvutuyen/Desktop/earthbeben/static/karte.html")
