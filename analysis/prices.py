# coding: utf-8
import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pylab

# Requires input data with columns: `ad_id`, `cluster`, and `price_per_hour`
prices_by_ad = pd.read_csv('data/ad_prices_by_ad.csv')

prices_by_ad['cluster'] = prices_by_ad.apply(lambda x: mappings.get(x.ad_id, ''), 1)
cluster = prices_by_ad.groupby('cluster')
df = cluster.filter(lambda x: len(x) > MIN_CLUSTER_SIZE)
df = df[df.cluster.str.startswith('cluster:')]

cluster = prices_by_ad.groupby('cluster')

def draw(column, x, fn):
    pylab.clf()
    column.plot(kind='kde')
    axes = pylab.gca()
    axes.set_xlim(x)
    pylab.savefig(fn)

def draw_scatter(x, y, fn):
    pylab.clf()
    pylab.scatter(x, y, alpha=0.3)
    pylab.savefig(fn)

draw(cluster.price_per_hour.std(), [0, 300], 'price_std_kde.png')
draw(cluster.price_per_hour.std(), [0, 90], 'price_std_kde_90.png')

both = cluster.agg({'price_per_hour': [np.std, len]})
draw_scatter(both['std'], both['len'], 'std_cluster_vs_std_price.png')

std_size = both['len'].std()
std_std = both['std'].std()
both_pruned = both[(both['len'] < std_size*2) & (both['std'] < std_std*2)]
draw_scatter(both_pruned['std'], both_pruned['len'], 'std_cluster_vs_std_price_pruned.png')

