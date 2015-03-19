
f = open('data/msa_locations.tsv')
mappings = {}
last_seen_ad, last_seen_loc = f.readline().strip().split('\t')

skip = False

# The same ad id is guaranteed to be consecutive
for line in f:
    ad, loc = line.strip().split('\t')
    
    # If the last entry wasn't skipped, put it in the mapping
    if ad != last_seen_ad:
        skip = False

    # Ad is same, location not the same: skip all ads
    if ad == last_seen_ad and loc != last_seen_loc:
        skip = True
    
    last_seen_ad = ad
    last_seen_loc = loc
