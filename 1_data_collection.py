# Read CDM file from WRI Repository
cdm = pd.read_csv('https://raw.githubusercontent.com/wri/global-power-plant-database/master/source_databases_csv/database_CDMDB.csv', dtype=object)
cdm = cdm[cdm['country_long']=='Vietnam'].reset_index().drop(columns=['index', 'country','country_long']).dropna(axis=1, how='all').rename(columns={'fuel1':'primary_fuel'})

# Clean Plant Name with Hydro or Wind 
cdm.loc[cdm['name'].str.lower().str.contains('hydro'),'base_name'] = cdm['name'].str.lower().str.extract('(.*)\shydro', expand=False)
cdm.loc[cdm['name'].str.lower().str.contains('wind'),'base_name'] = cdm['name'].str.lower().str.extract('(.*)\swind', expand=False)

# Manual Clean
cdm.at[0,'base_name'] = 'Eatul 4'
cdm.at[212,'base_name'] = 'Binh Thuan'
cdm['base_name'] = cdm['base_name'].str.replace(' province','')

# Combing two Nam Cat (5 & 3.2) into one record
cdm.at[106,'capacity_mw'] = '8.2'
cdm.drop(index=107, inplace=True)
cdm = cdm[cdm['base_name'].notnull()]
cdm['base_name'] = cdm['base_name'].str.title()

# Read WRI file
wri = pd.read_csv('https://raw.githubusercontent.com/wri/global-power-plant-database/master/source_databases_csv/database_WRI.csv', dtype=object)
wri = wri[wri['country_long']=='Vietnam'].drop(columns=['country','country_long']).dropna(axis=1, how='all').reset_index()
wri['base_name'] = wri['name'].str.title()

# Combind two Nam Cat (5 & 3.2) into one record & two Thac Ba (120 & 0.3)
wri.at[154, 'capacity_mw'] = '8.2'
wri.at[241, 'capacity_mw'] = '120.3'
wri.at[11,'base_name'] = 'Bac Lieu'
wri.drop(index=[155, 242], columns=['index'], inplace=True)
wri.set_index('base_name',inplace=True)

# Merge
data = wri.merge(cdm, how='outer',on='base_name',indicator=True, sort=True)

# Manual Resolve naming differences. CDM takes priority.
data.at[205,'base_name'] = 'Muong Hum'
data.drop(index=[
    93, # Dak Ro Sa 2 > Dakrosa2
    91, # Dak R'Tih > Dakrtih
    112, # Dam'Bri > Da M'Bri
    203, # Change CDM from Muong Hum 32 Mw to Muong Hum and keep CDM
    330, # Sre Pok 4a > SrePok 4A
    264, 265, # Ngoi Xan 1 & Ngoi Xan 2 > Ngoi Xan
    385, # Yan-Tann-Sien > Yan Tann Sien
    388 # Zahung > Za Hung
], inplace=True)

# Extract Base Names
master = pd.DataFrame(data['base_name'])
master = master.merge(cdm, how='left').set_index('base_name')
master['commissioning_year'] = np.nan
master.update(wri, overwrite=False)
master.to_csv('master.csv')