#!/bin/sh

# Remove lines with missing cluster ids and/or dates
grep -v '\N' doc-provider-timestamp.tsv > doc-provider-pruned.tsv

# Rearrange columns for sorting (sort cluster and date in one swoop)
csvcut -t -c 2,3,1 doc-provider-pruned.tsv > doc-provider-arranged.tsv
sort doc-provider-arranged.tsv > doc-provider-sorted.tsv
