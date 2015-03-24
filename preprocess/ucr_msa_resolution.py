# coding: utf-8
f = open('ucr_crosswalk1.csv')
f = open('ucr_crosswalk_with_micro.csv')
out = open('ucr_crosswalk_with_micro2.csv')
out = open('ucr_crosswalk_with_micro2.csv', 'w')
out = open('ucr_crosswalk_with_micro2.csv')
out = open('ucr_crosswalk_with_micro2.csv', 'w')
f = open('ucr_crosswalk_with_micro.csv')
for line in f:
    agency, place, geoid = line.strip().split('\t')
    out.write('{}\t{}\t{}\t{}\r\n'.format(agency, place, geoid, geoid.split('US')[1]))
    
import pandas as pd
parents = pd.read_csv('ucr/msas_parents.tsv', sep='\t')
parents = pd.read_csv('ucr/msas_parents.tsv', sep='\t', header=None, names=['agency', 'geoid', 'metroname', 'msa'])
raw = pd.read_excel('ucr/UCR_msa.xlsx')
raw.shape
raw.head()
parents.shape
parents['short_geoid'] = parents['geoid'].str.split('US')[1]
parents['short_geoid'] = parents['geoid'].str.split('US')
parents['short_geoid'].head()
parents['short_geoid'].str.get(1)
parents['short_geoid'] = parents['short_geoid'].str.get(1)
parents.head()
raw.head()
crosswalk = pd.read_csv('ucr/crosswalk.csv')
crosswalk.head()
crosswalk['full_agency'] = crosswalk['AGENCY'] + ', ' + crosswalk['STATE']
crosswalk.head()
crosswalk['fips
crosswalk['fips'] = crosswalk['FSTATE'].astype(str) + crosswalk['FCOUNTY'].astype(str) + crosswalk['FPLACE'].astype(str)
crosswalk['fips'].head()
pd.merge(raw, crosswalk, left_on='city', right_on='AGENCY')
raw.head()
crosswalk.columns
raw['full_agency'] = raw['city'] + ', ' + raw['state']
pd.merge(raw, crosswalk, on='full_agency'])
pd.merge(raw, crosswalk, on='full_agency')
raw.shape
crosswalk.shape
pd.merge(raw, crosswalk, on='full_agency', how='left')
raw
raw.columns
raw.dups
raw.dups.value_counts()
get_ipython().magic(u'history ')
raw_merge = pd.merge(raw, crosswalk, on='full_agency', how='left')
raw_merge.head()
msas_parents.head()
parents.head()
parents.msa.str.endswith('0')
parents.msa.str.endswith('0').sum()
parents.shape
raw_merge = pd.merge(raw, crosswalk, on='full_agency', how='left')
raw_merge.head()
raw_merge.shape
raw_merge.fips.count()
raw_merge.msa.count()
parents.head()
pd.merge(raw_merge, parents, left_on='fips', right_on='short_geoid')
raw_merge
raw_merge.columns
get_ipython().magic(u'history ')
crosswalk['fips'] = crosswalk['FSTATE'].astype(str) + crosswalk['FPLACE'].astype(str)
raw_merge = pd.merge(raw, crosswalk, on='full_agency', how='left')
raw_merge.head()
pd.merge(raw_merge, parents, left_on='fips', right_on='short_geoid')
raw_merge.fips.count()
raw_merge.fips
raw_merge[320
]
raw_merge.ix[320,:]
raw_merge.ix[320,['FCOUNTY', 'FPLACE']]
raw_merge.ix[320,['FCOUNTY', 'FPLACE', 'fips']]
import requests
r = requests.get('https://www.youtube.com/watch?v=yXEuEUQIP3Q')
js = r.json()
r
r.text
r = requests.get('http://api.censusreporter.org/1.0/geo/tiger2013/16000US3774440/parents')
js = r.json()
js['parents']
get_ipython().magic(u'edit')
get_ipython().magic(u'edit')
raw_merge.fips
get_msa('3684000')
get_msa('2599027')
get_ipython().magic(u'edit')
get_msa('2599027')
get_msa('3684000')
get_ipython().magic(u'paste')
get_ipython().magic(u'edit')
raw_merge.head()
raw_merge['msa_geoid'] = raw_merge['fips'].apply(get_msa)
raw_merge
raw_merge.msa_geoid
raw_merge.msa_geoid.count()
raw_merge.msa_geoid.str.len() > 0
(raw_merge.msa_geoid.str.len() > 0).sum()
raw_merge.msa.count()
raw_merge.head()
raw_merge.msa.dtype
raw_merge['msa'] = raw_merge.msa.astype('object')
raw_merge['msa'] = raw_merge.msa.str.rjust(4, '0')
raw_merge['msa']
raw_merge['msa']
msa_geoids = raw_merge.msa_geoid
msa_geoids
raw.head()
crosswalk.head()
raw_merge = pd.merge(raw, crosswalk, on='full_agency')
raw_merge['msa_parent'] = msa_geoids
raw_merge.head()
raw_merge.tail()
raw_merge.columns
final = raw_merge[['city', 'state', 'msa', 'rape_2010', 'rape_2011', 'rape_2012', 'violent_2010', 'violent_2011', 'violent_2012', 'property_2010', 'property_2011', 'property_2012', 'fips', 'msa_parent']]
final
final.head()
final.tail()
final['msa_parent_short'] = final.msa_parent.apply(lambda x: x.split('US')[1])
final['msa_parent_short'] = final.msa_parent.apply(lambda x: x.split('US').get(1, ''))
final['msa_parent_short'] = final.msa_parent.apply(lambda x: x.split('US'))
final.msa_parent_short
final['msa_parent_short'] = final.msa_parent_short.apply(lambda x: x[1] if len(x) > 0)
final['msa_parent_short'] = final.msa_parent_short.apply(lambda x: x[1] if len(x) > 0 else '')
final.drop('msa_parent_short', inplace=True)
final.drop('msa_parent_short', 1, inplace=True)
final
final.drop('fips', axis=1, inplace=True)
final.to_csv('ucr_msas.csv')
final.to_csv('ucr_msas.csv', index=False)
final.tail()
final.tail(10)
final.tail(20)
raw_merge.tail(15)
raw_merge.tail(15)['FPLACE']
raw_merge.tail(15)[['FSTATE', 'FCOUNTY', 'FPLACE']]
raw_merge.tail(15)[['full_agency', 'FSTATE', 'FCOUNTY', 'FPLACE']]
raw_merge.tail(15)[['full_agency', 'FSTATE', 'FCOUNTY', 'FPLACE', 'fips']]
raw_merge.tail(15)[['full_agency', 'FSTATE', 'FCOUNTY', 'FPLACE', 'fips', 'msa_parents']]
raw_merge.tail(15)[['full_agency', 'FSTATE', 'FCOUNTY', 'FPLACE', 'fips', 'msa_parent']]
get_msa('3775000')
raw_merge_nodupes = raw_merge.drop_duplicates('full_agency')
raw_merge_nodupes.shape
msas2 = raw_merge_nodupes.fips.apply(get_msa)
msas2
get_msa('3775000')
raw_merge_nodupes['msa_parent'] = msas2
final = raw_merge_nodupes[['city', 'state', 'rape_2010', 'rape_2011', 'rape_2012', 'violent_2010', 'violent_2011', 'violent_2012', 'property_2010', 'property_2011', 'property_2012', 'msa_parent']]
final.tail()
final.msa_parent.count()
final.shape
(final.msa_parent.str.len() > 0).sum()
final.to_csv('ucr_msas.csv', index=False)
msas2 = raw_merge.fips.apply(get_msa)
msas2.tail()
raw_merge['msa_parents'] = msas2
raw_merge.columns
raw_merge.msa_parent == raw_merge.msa_parents
(raw_merge.msa_parent.str.len() > 0).sum()
(raw_merge.msa_parents.str.len() > 0).sum()
(raw_merge.msa_parent.str.len() > 0) & (raw_merge.msa_parent.str.len() == 0)
((raw_merge.msa_parent.str.len() > 0) & (raw_merge.msa_parent.str.len() == 0)).sum()
raw_merge.drop('msa_parent', axis=1, inplace=True)
raw_merge.head(20)
get_msa('4899015')
raw_merge.FPLACE.dtype
raw_merge['FPLACE'] = raw_merge.FPLACE.astype(str)
raw_merge['FPLACE']
raw_merge['FPLACE'].str.rjust(5, '0')
raw_merge['FPLACE'] = raw_merge['FPLACE'].str.rjust(5, '0')
raw_merge['fips'] = raw_merge['FSTATE'] + raw_merge['FPLACE']
raw_merge['fips'] = raw_merge['FSTATE'].astype(str) + raw_merge['FPLACE']
raw_merge
msas2 = raw_merge.fips.apply(get_msa)
msas2
msas2.head()
(msas2.str.len() > 0).sum()
raw_merge['msa_parents'] = msas2
raw_merge
raw_merge['FSTATE'] = raw_merge['FSTATE'].astype(str)
raw_merge['FSTATE']
raw_merge['FSTATE'].rjust(2, '0
raw_merge['FSTATE'].rjust(2, '0')
raw_merge['FSTATE'].str.rjust(2, '0')
raw_merge['FSTATE'] = raw_merge['FSTATE'].str.rjust(2, '0')
raw_merge['fips'] = raw_merge['FSTATE'].astype(str) + raw_merge['FPLACE']
msas2 = raw_merge.fips.apply(get_msa)
(msas2.str.len() > 0).sum()
raw_merge.shape
raw_merge['msa_parents'] = msas2
raw_merge.head()
raw_merge[raw_merge.msa_parents.str.len() == 0]
get_ipython().magic(u'pinfo pd.DataFrame.drop_duplicates')
raw_merge.groupby('city').ngroups
get_ipython().set_next_input(u"raw_merge.groupby('city').take");get_ipython().magic(u'pinfo take')
raw_merge.groupby('city').msa_parents.max()
raw_merge.groupby('full_agency').msa_parents.max()
msas = raw_merge.groupby('full_agency').msa_parents.max()
msas
msas.full_agency
raw_merge.groupby('full_agency').first()
df_dedup = raw_merge.groupby('full_agency').first()
df_dedup['msa_parents'] = msas
df_dedup.shape
(df_dedup.msas.str.len() > 0).sum()
(df_dedup.msa_parentss.str.len() > 0).sum()
(df_dedup.msa_parents.str.len() > 0).sum()
df_dedup
df_dedup.columns
df_dedup.ZIPCODE
df_dedup['ZIPCODE'] = df_dedup.ZIPCODE.astype(str)
df_dedup['ZIPCODE'] = df_dedup.ZIPCODE.str.rjust(5, '0')
df_dedup['ZIPCODE']
df_dedup['ZIPCODE'] = df_dedup.ZIPCODE.str.rstrip('.0')
df_dedup['ZIPCODE']
df_dedup['ZIPCODE'] = df_dedup.ZIPCODE.str.rjust(5, '0')
df_dedup['ZIPCODE']
final = df_dedup[['city', 'state', 'rape_2010', 'rape_2011', 'rape_2012', 'violent_2010', 'violent_2011', 'violent_2012', 'property_2010', 'property_2011', 'property_2012', 'msa_parent']]
final = df_dedup[['city', 'state', 'rape_2010', 'rape_2011', 'rape_2012', 'violent_2010', 'violent_2011', 'violent_2012', 'property_2010', 'property_2011', 'property_2012', 'msa_parents']]
final
final.to_csv('ucr_msas.csv', index=False)
df_dedup['ZIPCODE'] = raw_merge.groupby('full_agency').ZIPCODE.first()
df_dedup['ZIPCODE']
df_dedup['ZIPCODE'].astype(int).astype(str)
df_dedup['ZIPCODE'].fillna(0)
df_dedup['ZIPCODE'] = df_dedup['ZIPCODE'].fillna(0)
df_dedup['ZIPCODE'].astype(int).astype(str)
df_dedup['ZIPCODE'] = df_dedup['ZIPCODE'].astype(int).astype(str)
df_dedup['ZIPCODE'].rjust(5, '0')
df_dedup['ZIPCODE'].str.rjust(5, '0')
df_dedup['ZIPCODE'] = df_dedup['ZIPCODE'].str.rjust(5, '0')
raw_merge.ZIPRANGE
df_dedup['ZIPRANGE'] = raw_merge.groupby('full_agency').ZIPRANGE.max()
final = df_dedup[['city', 'state', 'rape_2010', 'rape_2011', 'rape_2012', 'violent_2010', 'violent_2011', 'violent_2012', 'property_2010', 'property_2011', 'property_2012', 'msa_parents', 'ZIPCODE', 'ZIPRANGE']]
final.to_csv('ucr_msas.csv', index=False)
final.msa_parents.str[-5:]
final['msa_short'] = final.msa_parents.str[-5:]
final.to_csv('ucr_msas.csv', index=False)
