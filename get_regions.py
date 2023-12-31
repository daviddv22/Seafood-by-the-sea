import sqlite3

def main():
    conn = sqlite3.connect('./databases/wholedata.db')
    c = conn.cursor()
    data = c.execute('SELECT name, state FROM resturants').fetchall()

    conn2 = sqlite3.connect('./databases/oceanDistance.db')
    c2 = conn2.cursor()
    state_to_region = {
        "AL": "South",
        "AK": "West",
        "AZ": "West",
        "AR": "South",
        "CA": "West",
        "CO": "West",
        "CT": "Northeast",
        "DE": "Northeast",
        "FL": "South",
        "GA": "South",
        "HI": "West",
        "ID": "West",
        "IL": "Midwest",
        "IN": "Midwest",
        "IA": "Midwest",
        "KS": "Midwest",
        "KY": "South",
        "LA": "South",
        "ME": "Northeast",
        "MD": "Northeast",
        "MA": "Northeast",
        "MI": "Midwest",
        "MN": "Midwest",
        "MS": "South",
        "MO": "Midwest",
        "MT": "West",
        "NE": "Midwest",
        "NV": "West",
        "NH": "Northeast",
        "NJ": "Northeast",
        "NM": "West",
        "NY": "Northeast",
        "NC": "South",
        "ND": "Midwest",
        "OH": "Midwest",
        "OK": "South",
        "OR": "West",
        "PA": "Northeast",
        "RI": "Northeast",
        "SC": "South",
        "SD": "Midwest",
        "TN": "South",
        "TX": "South",
        "UT": "West",
        "VT": "Northeast",
        "VA": "South",
        "WA": "West",
        "WV": "South",
        "WI": "Midwest",
        "WY": "West"
    }

    # Loop through each restaurant address
    for name, state in data:    

        region = state_to_region[state]    
        c2.execute("UPDATE oceanDistance SET region = ? WHERE name = ?", (region, name))
    conn2.commit()

if __name__ == "__main__":
    main()