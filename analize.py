import pandas as pd
from duomenys import get_data
import matplotlib.pyplot as plt
import requests
import psycopg2
import psycopg2
from scipy.stats import linregress

Asmuo = get_data()
Asmuo = pd.DataFrame(Asmuo)

#Profesinių ligų pasiskirstymas pagal savivaldybes 2022 metais
def pagal_savivaldybes():

    year = 2022

    pagal_regiona=Asmuo[Asmuo['year'] == year].groupby('savivaldybe')['year'].count()
    pagal_regiona = pagal_regiona[pagal_regiona> 5]
    plt.figure(figsize=(14,10))
    pagal_regiona.plot(kind='bar', color='green')
    plt.title('Profesinių ligų pasiskirstymas pagal savivaldybes 2022 metais')
    plt.ylabel('Atvejų_skaičius')
    plt.xticks(rotation=25,ha='right')
    plt.legend([])
    plt.savefig("pagal_savivaldybes_2022.png")
    plt.tight_layout()
    plt.show()

#Profesinės ligos ir jų dažnis

def profesiniu_lig_daz(year):
    year = year
    prof_lig_dazn_per_pas_met = Asmuo[Asmuo['year'] == year].groupby('priezasties_pav')['savivaldybe'].count()
    prof_lig_dazn_per_pas_met = prof_lig_dazn_per_pas_met[prof_lig_dazn_per_pas_met > 10]
    colors = ["lightskyblue", "lightcoral", "yellowgreen", "pink", "lightgreen", "purple"]
    plt.pie(prof_lig_dazn_per_pas_met, labels=prof_lig_dazn_per_pas_met.index, autopct='%1.1f%%', startangle=90,
            colors=colors,textprops={'fontsize': 6})
    plt.title(f'{year} metų\n' "Profesinės ligos pagal priežastis ")
    plt.savefig("profesines_lig_pagal_priez.png")
    plt.show()

#Profesinių ligų pasiskirstymas pagal lytį
def lytis():
    year_start = 2013
    year_end = 2023
    lyties_df = Asmuo[Asmuo['year'].between(year_start, year_end)]
    rezultatas = lyties_df.groupby(['year', 'lyties_pavadinimas'])['priezasties_pav'].count().unstack(fill_value=0)
    plt.figure(figsize=(10, 6))
    rezultatas.plot(kind='line', marker='o')
    plt.title('Profesinių ligų pasiskirstymas pagal lytį ir metus')
    plt.xlabel('Metai')
    plt.ylabel('Atvejų skaičius')
    plt.xticks(rotation=25, ha='right')
    plt.legend(title='Lytis', loc='upper right')
    plt.tight_layout()
    plt.savefig("lytis_linijinis.png")
    plt.show()






# pagal_savivaldybes()
# profesiniu_lig_daz(2020)
# lytis()