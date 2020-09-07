# Import
plant_name = pd.read_csv('https://github.com/yuenhsu/Vietnam_Power_Plants/blob/master/data/translation.csv')

# Fuel
fuel_translation = plant_name[plant_name['type']=='Fuel'][['std_name','name']]
fuel_translation = fuel_translation.rename(
    columns={
        'std_name':'std_fuel',
        'name':'fuel'
    })

# Plant
plant_translation = plant_name[plant_name['type']=='Plant'][['std_name','name']]


# Market
market = pd.read_csv('https://github.com/yuenhsu/Vietnam_Power_Plants/blob/master/data/raw_market.csv')

# Translate plant name
market = market.merge(
    plant_translation,
    how = 'left',
    on = 'name',
    sort = True
)

# Translate fuel
market = market.merge(
    fuel_translation,
    how = 'left',
    on = 'fuel',
)

# Keep standardised names and export
market = market[['std_name','std_fuel','capacity_mw',]]
market.to_csv('market.csv',index=False)


# PDP
pdp = pd.read_csv('https://github.com/yuenhsu/Vietnam_Power_Plants/blob/master/data/raw_pdp.csv')

# Translate plant name
pdp = pdp.merge(
    plant_translation,
    how = 'left',
    left_on = 'base_name',
    right_on = 'name',
    sort = True
)

# Translate fuel
pdp = pdp.merge(
    fuel_translation,
    how = 'left',
    on = 'fuel',
)

pdp['std_fuel'].fillna('Renewable', inplace=True)

# Keep standardised columns
pdp = pdp[['std_name','base_name','std_fuel','capacity_mw','planned_year']]

# Clean capacity
for i in pdp.index:
    if 'x' in pdp.at[i,'capacity_mw']:
        unit, cap = pdp.at[i,'capacity_mw'].split('x')
        new_cap = int(unit) * int(cap)
        pdp.at[i,'capacity_mw'] = new_cap

pdp.to_csv('pdp.csv',index=False)