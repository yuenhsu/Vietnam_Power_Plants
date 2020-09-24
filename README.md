# Vietnam_Power_Plants
 A list of power plants in Vietnam

## Project
The repository is created for my research project that examines the current electricity supply distribution in Vietnam and proposes a more sustainable path forward. Initially, we planned to utilise existing power plant database and visualise the distribution emphasising on the policy recommendation. However, we soon realised that there are currently no complete database for power plants in Vietnam available. Therefore, the project shifted towards building a repository providing future researchers with a complete list of power plants in Vietnam as of August 2020.

## Data Source
* [WRI Global Power Plant Database](https://github.com/wri/global-power-plant-database): The database provides existing data from [Clean Development Mechanism](https://cdm.unfccc.int/Projects/projsearch.html), [Global Energy Observatory](https://github.com/hariharshankar/pygeo), and other energy databases. For more information, please see the [repository](https://github.com/wri/global-power-plant-database). WRI database is the skeleton of our project providing power plants information, including energy source, capacity, coordinates, and commissioning year, for those existed before 2016. In this repository, we refer data from this database as **WRI**.
* [Vietnam Market Report](https://drive.google.com/file/d/1nGuxqdS9x0xMEjo0YRlC8sMHg7DhSeTa/view): The 2018 market report lists all plants liscensed to operate on the market by the end of 2018 with capacities produced in the year. This list allows us to update the information in WRI database and add some plants that are not available in WRI. In this repository, we refer data from this database as **Market**.
* [Vietnam PDP Plan](https://drive.google.com/file/d/1nGuxqdS9x0xMEjo0YRlC8sMHg7DhSeTa/view?usp=sharing): PDP 7 outlines a master plan for power source development. That is, a list of power plants to be constructed between 2016 to 2030. The revised PDP7 document from June 2020 includes infromation on current and future power plant projects, forecasted year of construction completion and construction status. This list allows us to verify some of the information in the previous two sources and builds up a road map for Vietnam power sector up to 2030. In this repository, we refer data from this database as **PDP**.

## Processes & File Directory
All raw and processed data are stored in [`data`](https://github.com/yuenhsu/Vietnam_Power_Plants/tree/master/data) folder and the scripts are stored in the root folder.

* Raw data: 
    * `raw_wri.csv`: Data from WRI database after cleaning with `1_data_collection.py` to remove duplicates.
    * `raw_market.csv` & `raw_pdp.csv`: Manually input from official PDF documents.

* Translation & standardisation: `translation.csv` for a list of plant and fuel names in Vietnamese and English, using `2_translation.py`.

* Cleaning: Changes are documented in `edit.csv` and the script for merging three datasets are available in `3_clean_merge.py`. We made many judgement calls in this step and operated under these premises:
    * Official documents take priority. That is, if WRI data are different from Market or PDP, we will drop WRI entry.
    * If WRI data are significantly different from official data, we will verify with second resources, either from Vietnamese power plant website, press releases or academic papers, and make decision on how to proceed.
    * Any power plants that are available in WRI only, that is, without official record, we must verify with at least one local Vietnam source to consider this power plant operational.

* Final output: `Vietnam_Power_Plants.csv`, includes a list of existing power plants and planned power plants up to 2030 with capacity, fuel source, coordinates, and commissioning year. Please note that:
    * Power plants with commissioning year after 2020 do not have coordinates since they are not built.
    * For bundled power plant projects, that is the one consisting of a set of power plants, we tool coordinates of the first power plant mentioned in the official name
    * For power plants with coordinates for both pwoer house and dem, we took coordinates of the power house. 
    * For power plants with coordinates for main building and extension, we took coordinates of the main building.

Here is a snapshot of the final output:
std_name | capacity_mw | latitude | longitude | std_fuel | commissioning_year 
--- | --- | --- | --- | --- | ---
A Luoi | 170 | 16.2839 | 107.3589 | Hydro | 2012


## Analysis
After obtaining the final list, we began the analysis and research. The project goal is to provide recommendations on improving sustainability of Vietnam’s electricity grid. We first assessed the current and planned electricity grid of Vietnam​ and identified the areas for improvement. 

### Assessing the current and planned electricity grid
![](https://github.com/yuenhsu/Vietnam_Power_Plants/blob/master/image_output/01_generation_ind.png?raw=true)

The graph shows the distribution of electricity generation by fuel type from 1990 to 2030 in Vietnam, assuming all existing power plants will continue operating without retiring before 2030. Electricity generated by coal plants increases significantly from 2010 to early 2020s. While the slope decreases after 2022, under current government proposal, more and more coal plants are planned to be constructed every year. 

![](https://github.com/yuenhsu/Vietnam_Power_Plants/blob/master/image_output/02_generation_yr_sum.png?raw=true)

This graph shows the distribution of electricity generation by fuel source. Current and future power generation rely heavily on plants powered by coal, gas and oil respectively. The stacked bar chart also shows the total power generation for each year. Under the assumption that no plant will retire, generation from all types of source increases. Either building more power plants or increasing the capacity for existing plants will result in changes in generation. As the graph provides aggregated data, it is difficult to tell whether Vietnam is building a few plants with large capacity or multiple small ones. Hence, the next graph.

![](https://github.com/yuenhsu/Vietnam_Power_Plants/blob/master/image_output/03_capacity.png?raw=true)

The bubble chart shows the **capacity** and commissioning year for each plant in the list. Majority of the power plants have a capacity lower than 1000 MW. Plants with larger capacity use coal, hydro, or nuclear as the energy source. The renewable category is excluded in the previous statement because Linh and I treat it as a placeholder. We believe that Vietnamese officals have not determined what renewable energy will fuel a number of plants nor decided on their place of construction, hence those lack plant name in PDP document, but have fixed term to be built.

To sum, electricity supply in Vietnam has been increasing since 2000 and will continue to grow. While various energy sources are utilised to increase generation, coal plants along with other fossil fuels are expected to be powering the grid. 

So, back to the research, does the current and planned grid seem to be heading to a more sustainable future? Yes and no. Yes - because many plants powered by renewable energy are expected to be built within the next decade. No - because more coal plants will be constructed as well. This brings to the next step: what recommendations can we provide to make the energy sector slightly more sustainable? 

### Visualising distribution for recommendation
![](https://github.com/yuenhsu/Vietnam_Power_Plants/blob/master/image_output/04_plants.png?raw=true)

Firstly, we mapped all power plants with coordinates. 

![](https://github.com/yuenhsu/Vietnam_Power_Plants/blob/master/image_output/05_buffer_fossil.png?raw=true)

Secondly, we draw a buffer around all fossil plants with a diameter of 36 kilometers to demonstrate the area of pollution generated by the plants. The map shows that the fossil plants are concerntrated in the north and south. We then calculated the proportion of polluted area and multiplied the percentage with the province population, assuming the population is distributed equally across the province. 

![](https://github.com/yuenhsu/Vietnam_Power_Plants/blob/master/image_output/06_affected_pop.png?raw=true)

This is the final result. The red colour on the map shows the affected population in each province. Three provinces with the most population affected by the pollution are:
1. Ho Chih Minh City: 62.27% of the province falls within the pollution buffer area with an estimated 5.3 million residents.
2. Ha Noi: 29.70% with 2.2 million residents.
3. Dong Nai: 24.75% with 763,691 residents affected.

### Recommendation
![](https://github.com/yuenhsu/Vietnam_Power_Plants/blob/master/image_output/07_plants.png?raw=true)

Lastly, we analysed the top three plants with the most affected population. All three of which are located in Ho Chih Minh City and use fossil fuel as the primary energy source. Vietnamese officials should consider replacing these three power plants with renewable energy source to reduce the population affected by the pollution.

## Contributor
* Yu En Hsu, Master of Public Administration Candidate at Maxwell School at Syracuse University - *Author and Researcher* - [Portfolio](https://yuenhsu.website/)
* Linh Nguyen Phan Bao, Master of Public Administration Candidate at Maxwell School at Syracuse University - *Author and Researcher* - [Github](https://github.com/lnguyenp)
* Pete Wilcoxen, Professor, Public Administration and International Affairs at Maxwell School at Syracuse University - *Instructor and Advisor* - [Portfolio](https://wilcoxen.maxwell.insightworks.com/pages/44.html)
