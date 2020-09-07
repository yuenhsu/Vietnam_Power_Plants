# Import PDP & Merge with WRI/Market
pdp = pd.read_csv('https://github.com/yuenhsu/Vietnam_Power_Plants/blob/master/data/eng_pdp.csv').drop(columns='base_name')
wri_market = pd.read_csv('https://github.com/yuenhsu/Vietnam_Power_Plants/blob/master/data/eng_wri.csv')

all = pdp.merge(
    wri_market.drop(columns='_merge'),
    left_on = 'std_name',
    right_on = 'base_name',
    how = 'outer',
    sort = True,
    indicator = True
)


# Filter out plants that are in both dataset
both = all[all['_merge']=='both']['std_name'].unique().tolist()

# Give brand new units/plants a "New" tag in the name
for i in pdp.index:
    if (pdp.at[i,'std_name'] in both) & (int(pdp.at[i,'planned_year'])>2019):
        name = pdp.at[i,'std_name']
        new_name = name + ' New'
        pdp.at[i,'std_name'] = new_name

# Merge again
all2 = pdp.merge(
    wri_market.drop(columns=['_merge','name']),
    left_on = 'std_name',
    right_on = 'base_name',
    how = 'outer',
    sort = True,
    indicator = True
)

# Filter out brand new units/plants
new_plant = all2[all2['_merge']=='left_only'][['std_name','std_fuel','capacity_mw_x','planned_year']].rename(columns={'capacity_mw_x':'capacity_mw'})
new_plant['capacity_mw'] = new_plant['capacity_mw'].astype(int)
new_plant['planned_year'] = new_plant['planned_year'].astype(int)
new_plant_grouped = new_plant.groupby(by=['std_name','std_fuel']).agg({'capacity_mw':'sum','planned_year':'mean'}).reset_index()
new_plant_grouped['planned_year'] = new_plant_grouped['planned_year'].round()
new_plant_grouped['planned_year'] = new_plant_grouped['planned_year'].astype(int)