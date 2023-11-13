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
    plt.legend([]) # panaikinam legenda
    plt.savefig("pagal_savivaldybes_2022.png")
    plt.tight_layout()
    plt.show()

pagal_savivaldybes()

