import requests

base = 'http://api.censusreporter.org/1.0/geo/tiger2013/16000US{}/parents'

def get_msa(place_fips):
    q = base.format(place_fips)
    r = requests.get(q)
    js = r.json()

    for entry in js['parents']:
        try:
            if entry['sumlevel'] == '310':
                return entry['geoid']
        except KeyError:
            return ''
