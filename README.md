# Vietnam_Power_Plants
 A list of power plants in Vietnam

# Project
## Contributor
* Yu En Hsu, Master of Public Administration Candidate at Maxwell School at Syracuse University - *Author and Researcher* - [Portfolio](https://yuenhsu.website/)
* Linh Nguyen Phan Bao, Master of Public Administration Candidate at Maxwell School at Syracuse University - *Author and Researcher* - [Github](https://github.com/lnguyenp)
* Pete Wilcoxen, Professor, Public Administration and International Affairs at Maxwell School at Syracuse University - *Instructor and Advisor* - [Portfolio](https://wilcoxen.maxwell.insightworks.com/pages/44.html)

## Purpose
The repository is created for my research project that examines the current electricity supply distribution in Vietnam and proposes a more sustainable path forward. Initially, we planned to utilise existing power plant database and visualise the distribution emphasising on the policy recommendation. However, we soon realised that there are currently no complete database for power plants in Vietnam available. Therefore, the project shifted towards building a repository providing future researchers with a complete list of power plants in Vietnam as of August 2020.

## Data Source
* [WRI Global Power Plant Database](https://github.com/wri/global-power-plant-database): The database provides existing data from [Clean Development Mechanism](https://cdm.unfccc.int/Projects/projsearch.html), [Global Energy Observatory](https://github.com/hariharshankar/pygeo), and other energy databases. For more information, please see the [repository](https://github.com/wri/global-power-plant-database). WRI database is the skeleton of our project providing power plants information, including energy source, capacity, coordinates, and commissioning year, for those existed before 2016. In this repository, we refer data from this database as **WRI**.
* [Vietnam Market Report](https://drive.google.com/file/d/1nGuxqdS9x0xMEjo0YRlC8sMHg7DhSeTa/view): The 2018 market report lists all plants operating on the market by the end of 2018 with capacity in the year. This list allows us to update the information in WRI database and adds some plants that are not available in WRI. In this repository, we refer data from this database as **Market**.
* [Vietnam PDP Plan](https://drive.google.com/file/d/1nGuxqdS9x0xMEjo0YRlC8sMHg7DhSeTa/view?usp=sharing): PDP 7 outlines a master plan for power source development. That is, a list of power plants to be constructed between 2016 to 2030. This list allows us to verify some of the information in the previous two sources and builds up a road map for Vietnam power sector up to 2030. In this repository, we refer data from this database as **PDP**.

# Processes
TL;DR: Final product is [Vietnam_Power_Plants.csv](https://github.com/yuenhsu/Vietnam_Power_Plants/blob/master/Vietnam_Power_Plants.csv), which includes a list of existing power plants and planned power plants up to 2030 with capacity, fuel source, coordinates, and commissioning year. Have fun!

1. Data Collection
    1. Pull data from WRI and [clean](https://github.com/yuenhsu/Vietnam_Power_Plants/blob/master/1_data_collection.py) the content. As WRI itself consists of multiple sources, we resolve duplicates in this step. The output is available in [raw_wri.csv](https://github.com/yuenhsu/Vietnam_Power_Plants/tree/master/data) file.
    2. Manually convert Market and PDP data as both sources are available in PDF formats only. The output are [raw_market.csv](https://github.com/yuenhsu/Vietnam_Power_Plants/tree/master/data) and [raw_pdp.csv](https://github.com/yuenhsu/Vietnam_Power_Plants/tree/master/data).

2. Translation & Standardisation: As both Market and PDP are in Vietnamese, we needed to translate the power plant names and province names to English. 
    1. We noticed that Market and WRI are **plant-based** data and PDP is **unit-base** data. For example, Market and WRI have **Formosa Ha Tinh** and PDP has **Formosa Ha Tinh Unit 1**. For the purpose of the research, we decided to build plant-level data.
    2. We translated and standardised fuel name as well. For example, hydro can be Thủy điện or TĐ in Vietnamese, and we converted them into the English. The conversion between English and Vietnamese is documented in the [translation.csv](https://github.com/yuenhsu/Vietnam_Power_Plants/tree/master/data) file. The script for the step is available in the [2_translation.py](https://github.com/yuenhsu/Vietnam_Power_Plants/blob/master/2_translation.py).

3. Manual Cleaning & Merging: Given three data sources are from different point of time, here we made a lot of judgement call to continue the process. We operated under these premises:
    1. Official documents take priority. That is, if WRI data are different from Market or PDP, we will drop WRI entry.
    2. If WRI data are significantly different from official data, we will verify with second resources, either from Vietnamese press release or academic research, and make decision on how to proceed.
    3. Any power plants that are available in WRI only, that is, without official record, we must be able to verify with at least one local Vietnam source to consider the power plant.
    4. All the changes are documented in [edit.csv](https://github.com/yuenhsu/Vietnam_Power_Plants/tree/master/data) file.
    5. Lastly, we merged three data. The script is available in [3_clean_merge.py](https://github.com/yuenhsu/Vietnam_Power_Plants/blob/master/3_clean_merge.py)

4. Output: [Vietnam_Power_Plants.csv](https://github.com/yuenhsu/Vietnam_Power_Plants/blob/master/Vietnam_Power_Plants.csv) is the final product. A preview of the file is provided below. Please note that:
    1. Power plants with commissioning year after 2019 do not have coordinates. They are from the PDP master plan that are scheduled to build in the future.
    2. Coordinates are not entirely accurate. Some are for the power plants and others are for the dem. Priority is given to the plant itself.
    3. Smaller plants with lower than 30 mw capacity may not have coordinates. We prioritise power plants with significant capacity. We may continue the project and finish the coordinates for small plants in the future.
    4. Alternative energy source, as shown in PDP, do not have physical plants location. Considering the PDP was drafted in 2016, these alternative sources are likely to be placeholder that were waiting to be planned in the future.

std_name | capacity_mw | latitude | longitude | std_fuel | commissioning_year 
--- | --- | --- | --- | --- | ---
A Luoi | 170 | 16.2839 | 107.3589 | Hydro | 2012


