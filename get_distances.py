import sqlite3
from geopy.distance import geodesic

def main():
    conn = sqlite3.connect('./databases/geolocation.db')
    c = conn.cursor()
    data = c.execute('SELECT * FROM geolocation').fetchall()

    conn2 = sqlite3.connect('./databases/oceanDistance.db')
    c2 = conn2.cursor()

    c2.execute('DROP TABLE IF EXISTS "oceanDistance";')
    c2.execute('CREATE TABLE oceanDistance(name TEXT, distance REAL, region TEXT)')

    for _, name, lon, lat in data:
        ocean_points = [
            (61.2194, -149.9003),  # Pacific Ocean near Anchorage, AK
            (34.0522, -118.2437),  # Pacific Ocean near Los Angeles, CA
            (32.7157, -117.1611),  # Pacific Ocean near San Diego, CA
            (37.7749, -122.4194),  # Pacific Ocean near San Francisco, CA
            (47.6062, -122.3321),  # Pacific Ocean near Seattle, WA
            (25.7617, -80.1918),   # Atlantic Ocean near Miami, FL
            (40.7128, -74.0060),   # Atlantic Ocean near New York City, NY
            (38.9072, -77.0369),   # Atlantic Ocean near Washington, DC
            (33.7490, -84.3880),   # Atlantic Ocean near Atlanta, GA
            (39.0997, -94.5786),   # Atlantic Ocean near Kansas City, MO
            (41.8781, -87.6298),   # Atlantic Ocean near Chicago, IL
            (35.2271, -80.8431),   # Atlantic Ocean near Charlotte, NC
            (29.7604, -95.3698),   # Gulf of Mexico near Houston, TX
            (27.9659, -82.8001),   # Gulf of Mexico near Tampa, FL
            (25.7785, -80.1316),   # Atlantic Ocean near Miami Beach, FL
            (33.6189, -117.9289),  # Pacific Ocean near Newport Beach, CA
            (33.6803, -118.0058),  # Pacific Ocean near Long Beach, CA
            (34.0141, -118.2879),  # Pacific Ocean near Santa Monica, CA
            (33.8522, -118.3694),  # Pacific Ocean near Redondo Beach, CA
            (32.7157, -117.1611),  # Pacific Ocean near Coronado, CA
            (21.3069, -157.8583),  # Pacific Ocean near Honolulu, HI
            (21.3422, -158.0558),  # Pacific Ocean near Pearl Harbor, HI
            (22.0964, -159.5261),  # Pacific Ocean near Lihue, HI
            (41.4901, -71.3128),   # Atlantic Ocean near Newport, RI
            (38.8951, -77.0364),   # Atlantic Ocean near Alexandria, VA
            (44.4759, -73.2121),   # Atlantic Ocean near Burlington, VT
        ]
        
        distances_to_ocean = [geodesic((lat, lon), point).km for point in ocean_points]
        distance = min(distances_to_ocean)
        
        c2.execute('INSERT INTO oceanDistance VALUES(?, ?, ?)', (name, distance, ''))
    conn2.commit()

if __name__ == '__main__':
    main()