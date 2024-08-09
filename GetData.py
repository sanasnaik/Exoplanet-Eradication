import requests, random

# base URL
tap_url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"

# adql query for planet name and number of planets in system
query_sy_pnum = """
    SELECT pl_name, sy_pnum
    FROM ps
"""
params = {
    "request": "doQuery",
    "lang": "ADQL", 
    "query": query_sy_pnum, 
    "format": "json" 
}

response = requests.get(tap_url, params)
exoplanets = response.json() 
random.shuffle(exoplanets)

for exoplanet in exoplanets[:10]:
    print(f"Exoplanet: {exoplanet['pl_name']}, Number of Planets: {exoplanet['sy_pnum']}")