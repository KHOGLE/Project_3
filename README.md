### Project_3

# Starting a Business in LA
**Collaborators**: Katharyn Hogle, Jacob Bayer, Jose Varrera, and Naomi Martin

## Summary
How can we determine where success is more likely to occur within Los Angeles without access to the revenue produced by each company?

We decided that location data, start date, and the total amount of businesses for each industry within those locations is the strongest implication of success. 

The most common business consists of mini-warehousing and self-storage in the Los Angeles Area 
Los Angeles has roughly 14 times more businesses than any sub-city with Van Nuys, California being the most active of those cities.
In the year 2018, over 38 thousand businesses began operating. 
Recent years have seen a large spike in businesses opened despite COVID-19.

### Data Sources
#### Original CSV Source
- **Data.gov** : https://catalog.data.gov/dataset/listing-of-active-businesses
#### NAICS Codes 
- **Economic Census: NAICS Codes & Understanding Industry Classification Systems** : https://www.census.gov/programs-surveys/economic-census/year/2022/guidance/understanding-naics.html

## Visuals 

Created using Plotly and Jupiter Notebook
Multi-figured plot using buttons to select between sample options.
Compares geographical, historic, and industry-based data, respectively. 


## Relevance
All of this data is designed to determine what a successful business might look like.
Industry v. StartDate determines current and outdated business trends. 
Industry v. Location determines what districts need what types of businesses.
Location v. StartDate determines which districts may be up and coming.
The number of businesses per location may determine what districts are home to more consumers or which districts may need to find more businesses to attract.
ALL OF THIS DATA IS A GREAT START TO DETERMINING WHERE A BUSINESS COULD PROSPER.

## Problems Encountered
Data Modeling struggles: We managed to create a sqlite.db to run the flask app with, however, it kept crashing as it tried to load making it impossible to connect further on.
Data Visualization struggles: We tried to change our csv files into Json files to run JavaScript D3 but no matter which form of Json conversion was attempted, the file refused to write correctly and therefor was useless.  
Plotly in Python brought with it its own variety of issues


### Code Building Sources
- **W3schools**:  Jumbotron, CSS options, Font styles, Well, and Panels
- **getbootstrap.com** : Grid system
- **Stack OverFlow https://stackoverflow.com/questions/31394998/using-sqlalchemy-to-load-csv-file-into-a-database and 
https://stackoverflow.com/questions/43453420/import-csv-to-database-using-sqlalchemy**: SQL database formation
- **https://github.com/sqlitebrowser/sqlitebrowser/wiki** : SQLite Browser Documentation
- **https://stackoverflow.com/questions/51119308/how-to-extract-the-first-2-digits-of-all-numbers-in-a-column-of-a-dataframe**: Separating out the first two digits of NAICS in data-cleaning process
- **https://plotly.com/python/basic-charts/**: Jupyter Notebook graphs
