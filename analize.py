import pandas as pd
import seaborn as sns
from duomenys import get_data
import matplotlib.pyplot as plt
from scipy.stats import linregress

Asmuo = get_data()
Asmuo = pd.DataFrame(Asmuo)

#Profesinių ligų pasiskirstymas pagal savivaldybes 2022 metais
def pagal_savivaldybes(year):
    year = year

    pagal_regiona=Asmuo[Asmuo['year'] == year].groupby('savivaldybe')['year'].count()
    pagal_regiona_sorted = pagal_regiona.sort_values(ascending=False)
    pagal_regiona = pagal_regiona_sorted[pagal_regiona_sorted> 5]
    plt.figure(figsize=(14,10))
    pagal_regiona.plot(kind='bar', color='green')
    plt.title('Profesinių ligų pasiskirstymas pagal savivaldybes 2022 metais')
    plt.ylabel('Atvejų_skaičius')
    plt.xticks(rotation=25,ha='right')
    plt.legend([])
    plt.savefig("Pictures\pagal_savivaldybes_2022.png")
    plt.tight_layout()
    plt.show()

#Profesinės ligos ir jų dažnis

def profesiniu_lig_daz(year):
    year = year
    prof_lig_dazn_per_pas_met = Asmuo[Asmuo['year'] == year].groupby('priezasties_pav')['savivaldybe'].count()
    prof_lig_dazn_per_pas_met = prof_lig_dazn_per_pas_met[prof_lig_dazn_per_pas_met > 1]
    colors = ["lightskyblue", "lightcoral", "darkgreen", "pink", "lightgreen", "purple", "orange"]
    plt.pie(prof_lig_dazn_per_pas_met, labels=prof_lig_dazn_per_pas_met.index, autopct='%1.1f%%', startangle=90,
            colors=colors,textprops={'fontsize': 6})
    plt.title(f'{year} metų\n' "Profesinės ligos pagal priežastis ")
    plt.savefig("Pictures\profesines_lig_pagal_dazni.png")
    plt.show()

#Profesinių ligų pasiskirstymas pagal lytį
def lytis(year_start,year_end):
    year_start=year_start
    year_end=year_end
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
    plt.savefig("Pictures\lytis_linijinis.png")
    plt.show()

#Profesinių ligų skaičiaus kitimas savivaldybėse pasirinktų metų intervale
def kitimas_metais(year_start, year_end):
    year_start = year_start
    year_end = year_end
    filtruoti_duomenys = Asmuo[Asmuo['year'].between(year_start, year_end)]
    rezultatas = filtruoti_duomenys.groupby(['savivaldybe', 'year']).size().unstack(fill_value=0)
    rezultatas = rezultatas[rezultatas >= 1]
    rezultatas = rezultatas.dropna()

    rezultato_ilgis = rezultatas.reset_index().melt(id_vars='savivaldybe', var_name='year', value_name='count')
    palette = sns.color_palette("Paired", n_colors=len(rezultato_ilgis['savivaldybe'].unique()))
    # sns.set_theme(style="darkgrid")
    plt.figure(figsize=(15, 7))
    sns.lineplot(data=rezultato_ilgis, x='year', y='count', hue='savivaldybe', marker='o', palette=palette)
    # sns.color_palette("dark:#5A9_r", as_cmap=True)
    plt.title(f'Profesinių ligų skaičiaus kitimas savivaldybėse {year_start}-{year_end} metais')
    plt.xlabel('Metai')
    plt.ylabel('Ligų skaičius')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Savivaldybe', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig("Pictures\pokytis.png")
    plt.show()

def regresija(year_start,year_end):
    year_start = year_start
    year_end = year_end
    filtruoti_duomenys = Asmuo[Asmuo['year'].between(year_start, year_end)]

    rezultatas = filtruoti_duomenys.groupby(['savivaldybe', 'year']).size().unstack(fill_value=0)

    rezultatas_per_metus_savivaldybe = rezultatas.sum(axis=1)

    filtruota_savivaldybes = rezultatas_per_metus_savivaldybe[rezultatas_per_metus_savivaldybe > 0].index

    filtruoti_rezultatas = rezultatas.loc[filtruota_savivaldybes]

    filtruoti_rezultatas_ilgis = filtruoti_rezultatas.reset_index().melt(id_vars='savivaldybe', var_name='year',
                                                                         value_name='count')
    filtruoti_rezultatas_ilgis['year'] = pd.to_numeric(filtruoti_rezultatas_ilgis['year'], errors='coerce')

    filtruoti_rezultatas_ilgis = filtruoti_rezultatas_ilgis.dropna(subset=['year'])

    filtruoti_rezultatas_ilgis['year'] = filtruoti_rezultatas_ilgis['year'].astype(int)

    plt.figure(figsize=(15, 7))
    plt.title('Tendencijų linijos pagal Savivaldybe ir metus')

    plt.xticks(rotation=45, ha='right')

    slopes = {}

    for name, group in filtruoti_rezultatas_ilgis.groupby('savivaldybe'):
        slope, intercept, r_value, p_value, std_err = linregress(x=group['year'], y=group['count'])
        slopes[name] = slope
    for name, group in filtruoti_rezultatas_ilgis.groupby('savivaldybe'):
        if slopes[name] > 0:
            sns.regplot(
                x='year', y='count', data=group,
                label=name, scatter_kws={'s': 50},
                line_kws={'linewidth': 2}, ci=None
            )
    plt.legend(title='Savivaldybe', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.xlabel('Metai')
    plt.ylabel('Skaičius')
    plt.savefig("Pictures\ regresija.png")
    plt.show()



pagal_savivaldybes(2022)
profesiniu_lig_daz(2019)
lytis(2013,2023)
kitimas_metais(2005,2023)
regresija(2013,2023)