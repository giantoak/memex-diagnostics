'''
Preprocessing step for associating ad_ids with their msa centroids
'''

import os
data_dir = '/mnt/memex-diagnostics/data/dump4'

msa_centroids = {}
with open('msa_centroids.csv') as f_centroids:
    for line in f_centroids:
        msa, lon, lat = line.strip().split(',')
        msa_centroids[msa] = (lat, lon)

with open(os.path.join(data_dir, 'msa_locations.tsv')) as f_ad_msas, \
    open(os.path.join(data_dir, 'made/ad_centroids.csv'), 'w') as f_out:
    
    for line in f_ad_msas:
        # ad is the string ad_id, msa is the full geo_id
        ad, msa = line.strip().split('\t')
        lat, lon = msa_centroids[msa]
        f_out.write('{},{},{}\n'.format(ad, lat, lon))
