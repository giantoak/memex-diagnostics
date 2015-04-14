# coding: utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import datetime

root_dir = '/mnt/memex-diagnostics/'
data_dir = os.path.join(root_dir, 'data', 'dump4')

# Minimum and maximum number of providers to be considered a cluster
MIN_CLUSTER_SIZE=5
MAX_CLUSTER_SIZE=200

df = pd.read_csv(os.path.join(data_dir,
'made/doc-provider-sorted.tsv'), header=None,
        names=['cluster_id', 'timestamp', 'ad_id'])

# Convert timestamp type
df['timestamp'] = pd.to_datetime(df['timestamp'], coerce=True)

# Clean dataset of unreasonable timestamps
df = df[df['timestamp'] > datetime.datetime(2010, 1, 1)]

# Filter by min cluster size
clusters = df.groupby('cluster_id')
df = clusters.filter(lambda x: len(x) > MIN_CLUSTER_SIZE & len(x) < MAX_CLUSTER_SIZE)

# Calculate interarrival times and convert them to days
clusters = df.groupby('cluster_id')
df['diffs'] = pd.to_timedelta(clusters['timestamp'].transform(
        lambda x: x-x.shift())) / np.timedelta64(1,'D')
df['time_since_first_started'] = pd.to_timedelta(clusters['timestamp'].transform(
        lambda x: x-x.iloc[0])) / np.timedelta64(1,'D')

# Create median and mean summary statistics
clusters = df.groupby('cluster_id')
means = clusters.agg({'diffs': lambda x: x.mean()})
medians = clusters.agg({'diffs': lambda x: x.median()})

# Output files
df.to_csv(os.path.join(data_dir, 'made/timediffs.csv'), columns=['cluster_id', 'ad_id', 'timestamp', 'diffs'])

