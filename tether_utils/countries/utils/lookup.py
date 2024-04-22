from json import load
from os.path import dirname, join

from .classes import CountryData

path = join(dirname(__file__), 'data', 'countries.json')

def iso2_lookup(iso2: str):
    with open(path, 'r') as f:
        data = load(f)
        return data.get(iso2, None)
    
def countries_iso():
    with open(path, 'r') as f:
        data = load(f)
        return sorted(data.keys())
    
def all_countries():
    with open(path, 'r') as f:
        all_data = load(f)
        return (CountryData(v) for v in sorted(all_data.values(), key=lambda item: item.get('name')))
