# coding: utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Minimum number of providers to be considered a cluster
MIN_CLUSTER_SIZE=5

df = pd.read_csv('data/doc-provider-timestamp-cluster-sorted.tsv', header=None,
        names=['cluster_id', 'ad_id', 'timestamp'])

# Filter DataFrame for null values
df = df[df.cluster_id!='\N']
df = df[df.timestamp !='\N']
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Filter by min cluster size
clusters = df.groupby('cluster_id')
df = clusters.filter(lambda x: len(x) > MIN_CLUSTER_SIZE)

# Sort within clusters by timestamps
clusters = df.groupby('cluster_id')
df = clusters.transform(lambda x: x.sort('timestamp'))

# Calculate interarrival times and convert them to days
clusters = df.groupby('cluster_id')
df['diffs'] = pd.to_timedelta(clusters['timestamp'].transform(
        lambda x: x-x.shift())) / np.timedelta64(1,'D')

# Create median and mean summary statistics
clusters = df.groupby('cluster_id')
means = clusters.agg({'diffs': lambda x: x.mean()})
medians = clusters.agg({'diffs': lambda x: x.median()})

# Output files
means.to_csv('interarrival_means.csv')
medians.to_csv('interarrival_medians.csv')

# Function for drawing plots
def draw(dataframe, x_range, output_filename):
    plt.clf()
    dataframe.diffs.plot(kind='kde')
    axes = plt.gca()
    axes.set_xlim(x_range)
    plt.savefig(output_filename)

draw(means, [0, 90], 'interarrival_means.png')
draw(medians, [0, 90], 'interarrival_medians.png')

