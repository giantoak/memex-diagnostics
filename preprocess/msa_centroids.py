import sys
import json
import codecs
import numpy as np

from centroids import centroid_of_polygon

def get_centroid(coords):
    '''
    Given either an iterable of coordinate pairs,
    or an iterable of iterables of coordinate pairs,
    find the arithmetic mean of the centroids of each
    iterable of coordinate pairs.

    '''

    try:
        centroids = map(centroid_of_polygon, coords)
    except TypeError:
        # coords is nested too tightly
        centroids = map(get_centroid, coords)
    except IndexError, ZeroDivisionError:
        # base case: coords is already the solution
        return coords
    
    if len(centroids) == 1:
        centroids = centroids[0]
    
    # I think this might only work with nestings 2 deep

    try:
        # There are multiple centroids -- return average
        centroids = tuple(map(np.mean, zip(*centroids)))
    except TypeError:
        # There was only one centroid, return it
        pass
    
    return centroids

sys.stderr = codecs.getwriter('utf8')(sys.stderr)

with open('data/all_msa_geo.json') as f:
    geojs = json.load(f)

geoid_to_centroid = {}

for msa_all_data in geojs['features']:
    geoid = msa_all_data['properties']['geoid']
    
    # Assuming that there is only one set of coordinates
    centroid = get_centroid(msa_all_data['geometry']['coordinates'])

    geoid_to_centroid[geoid] = centroid

for geoid, (lon, lat) in geoid_to_centroid.iteritems():
    print '{},{},{}'.format(geoid, lon, lat)
