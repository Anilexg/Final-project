
# **OCCUPATIONAL** DISEASES ANALYSIS

### _Details_

Created by: Lina Gegužienė and Renata Šimkevičienė

This is the end project in Vilnius Coding School

Project theme:  Health data analysis and visualisation

The main goal of the project is to find out the number of cases per year, the geographical distribution and which sexes are most affected by Occupational Diseases. The analysis period is from 2005 to 2023.

In this project we used to work with Python language, CSV files and Database (Postgres).
  

### _Applied knowledge:_

Used libraries: Pandas, Numpy, MatplotLib, SeaBorn, sklearn.linear_model ????

##### _postgres_.py

Used database adapter: psycopg2

Steps:????

1. Creating of postgres connection settings (def db_con():)
2. Writing function to create table into vcs_final_project database (def create_table():)
3. Creating connection to database for data analysis (def work_with_database():)

##### _web_scrap_.py

Used imports: psycopg2, BeautifulSoup, requests, time, postgres.py ???/

Steps:

1. Finding data from URL ("https://get.data.gov.lt/datasets/gov/hi/profesines/Asmuo").
2. Getting needed data from url as table using Beautiful soup and indicate analysis method (html.parser).
3. Using "if" and "for" received data inserted into table in Postgres

##### final_project.py

This is the main project file where all analysis were made.

Steps:

1. 

2. All visuals are controlled by functions (def), which helps to separate all graphs in the code.

For example, if you call def "pagal_savivaldybes():" you will receive this view:

![pagal_savivaldybes_2022.png](Pictures%2Fpagal_savivaldybes_2022.png)

For example if you call def "profesiniu_lig_daz(year):" you will receive this view:

![profesines_lig_pagal_priez.png](Pictures%2Fprofesines_lig_pagal_priez.png)

For example if you call def "lytis():" you will receive this view:

![lytis_linijinis.png](Pictures%2Flytis_linijinis.png)

For example if you call def "kitimas_metais():" you will receive this view:

![pokytis.png](Pictures%2Fpokytis.png)

For example if you call def "regresija():" you will receive this view:

![ regresija.png](Pictures%2F%20regresija.png)

### _Conclution_


