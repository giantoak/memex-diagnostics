# coding: utf-8
import pandas as pd
import numpy as np
import matplotlib

matplotlib.use('Agg')

df = pd.read_csv('sorted_time_diffs.csv')
df['diffs'] = pd.to_timedelta(df['diffs'])
clusters = df.groupby('cluster_id')
means = clusters.agg({'diffs': lambda x: x.mean()})
means['diffs'] = means['diffs'] / np.timedelta64(1,'D')

def draw(col, x, fn):
	pylab.clf()
	col.plot(kind='kde')
	axes = pylab.gca()
	axes.set_xlim(x)
	pylab.savefig(fn)	
