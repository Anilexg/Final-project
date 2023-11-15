
# **OCCUPATIONAL** DISEASES ANALYSIS

### _Details_

Created by: Lina Gegužienė and Renata Šimkevičienė

This is the end project of Data analysis course at Vilnius Coding School.

Project theme:  Occupational Diseases data analysis and visualization

The main goal of the project is to find out the number of cases per year, the geographical distribution and which sexes are most affected by Occupational Diseases. The analysis period is from 2005 to 2023.

In this project we used Python, CSV files, and a PostgreSQL database showcasing our practical coding skills acquired at Vilnius Coding School.
  

### _Applied knowledge:_

Used libraries: Pandas, Numpy, MatplotLib, SeaBorn, Selenium,SciPy

##### _postgres_.py

Used database adapter: psycopg2

##### _web_scrap_.py

Getting data from URL ("https://get.data.gov.lt/datasets/gov/hi/profesines/Asmuo").

##### analize.py

This is the main project file where all analysis were made. All visuals are controlled by functions, which helps to separate all graphs in the code.

For example, if you call "pagal_savivaldybes()" you will receive this view:

![pagal_savivaldybes.png](Pictures%2Fpagal_savivaldybes.png)

For example if you call "profesiniu_lig_dazni()" you will receive this view:

![profesines_lig_pagal_dazni.png](Pictures%2Fprofesines_lig_pagal_dazni.png)

For example if you call "lytis()" you will receive this view:

![lytis_linijinis.png](Pictures%2Flytis_linijinis.png)

For example if you call "kitimas_metais()" you will receive this view:

![pokytis.png](Pictures%2Fpokytis.png)

For example if you call "regresija()" you will receive this view:

![ regresija.png](Pictures%2F%20regresija.png)

### _Conclution_

n analysis of the Occupational Diseases List shows that since 2013 to 2023 in the municipality of Mažeikiai has the highest number of cases. Since 2005, the most frequent diagnosis has been Mechanical vibrations. In terms of occupational diseases by gender, males are the leading group in the period from 2014 to 2022. The graph showing the evolution of occupational diseases in the municipalities clearly shows a decrease in the number of cases. This is likely to be influenced by the rapid development of technology and occupational safety requirements. The last graph shows a selection of municipalities where the number of occupational diseases is increasing in a linear regression, i.e. there is an upward trend in the number of cases over the period shown in the graph.

