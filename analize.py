import pandas as pd
import seaborn as sns
from duomenys import get_data
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Įkeliame duomenis iš funkcijos
Asmuo = get_data()
# Gautus duomenis paverčiame į DataFrame
Asmuo = pd.DataFrame(Asmuo)

# Profesinių ligų pasiskirstymas pagal savivaldybes pasirinktų metų intervale
def pagal_savivaldybes(year_start,year_end):
    year_start = year_start
    year_end = year_end
    # Išrenkame duomenis iš Asmuo, tarp nurodytų metų intervalo
    filtruoti_duomenys = Asmuo[Asmuo['year'].between(year_start, year_end)]

    # Suskaičiuojame kiekvienoje savivaldybėje kiekvienais metais esančių atvejų kiekį
    rezultatas = filtruoti_duomenys.groupby(['savivaldybe', 'year']).size().reset_index(name='count')

    # Gautus rezultatus paverčiame į sveikus skaičius
    rezultatas['count'] = rezultatas['count'].astype(int)

    # Atvejų skaičius renkame tik tuos kurie yra didesni už 5
    rezultatas = rezultatas[rezultatas['count'] > 5]

    # Kuriame grafiką, nusakome jo dydį, koordinačių ašių pavadinimus ir kt.
    plt.figure(figsize=(14,10))

    # Naudojant Seaborn biblioteką nubraižomas stulpelinis grafikas.
    sns.barplot(x='count',y='savivaldybe',  data=rezultatas, hue='savivaldybe', palette='Set2', dodge=False)
    plt.title(f'Profesinių ligų pasiskirstymas pagal savivaldybes nuo {year_start}  iki  {year_end} metų')
    plt.ylabel('Savivaldybės')
    plt.xlabel('Atvejų_skaičius')
    plt.legend([])
    plt.savefig("Pictures\pagal_savivaldybes.png")
    plt.tight_layout()
    plt.show()

# Profesinių ligų pasiskirstymas pagal priežastis nurodytu laikotarpiu

def profesiniu_lig_daz(year):
    year = year
    # Filtruojame duomenis pagal metus ir grupuojame pagal priežastis, skaičiuojame kiekvienos priežasties atvejį tam tikruose metuose
    prof_lig_dazn_per_pas_met = Asmuo[Asmuo['year'] == year].groupby('priezasties_pav')['savivaldybe'].count()

    # Imame duomenis atitinkančius sąlygą, kad ligos atvejis buvo daugiau nei vienas kartas
    prof_lig_dazn_per_pas_met = prof_lig_dazn_per_pas_met[prof_lig_dazn_per_pas_met > 1]

    # Renkame grafikui spalvas
    colors = ["lightskyblue", "lightcoral", "darkgreen", "pink", "lightgreen", "purple", "orange"]

    # Sukuriame skritulinę diagramą
    plt.pie(prof_lig_dazn_per_pas_met, labels=prof_lig_dazn_per_pas_met.index, autopct='%1.1f%%', startangle=90,
            colors=colors,textprops={'fontsize': 6})
    plt.title(f'{year} metų\n' "Profesinės ligos pagal priežastis ")
    plt.savefig("Pictures\profesines_lig_pagal_dazni.png")
    plt.show()

# Profesinių ligų pasiskirstymas pagal lytį ir metų intervalą
def lytis(year_start,year_end):
    year_start=year_start
    year_end=year_end

    # Filtruojame duomenis pagal metų intervalą
    lyties_df = Asmuo[Asmuo['year'].between(year_start, year_end)]

    # Grupuojame pagal metus ir lytį atsižvelgiant į ligų skaičių
    rezultatas = lyties_df.groupby(['year', 'lyties_pavadinimas'])['priezasties_pav'].count().unstack(fill_value=0)

    # kuriame linijinę diagramą
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

# Profesinių ligų skaičiaus kitimas savivaldybėse pasirinktų metų intervale
def kitimas_metais(year_start, year_end):
    year_start = year_start
    year_end = year_end

    # Filtruojame duomenis pagal metų intervalą
    filtruoti_duomenys = Asmuo[Asmuo['year'].between(year_start, year_end)]

    # Grupuojame duomenis pagal savivaldybes ir metus, skaičiuojame profesinių ligų atvejų skaičių kiekvienai
    # savivaldybei nurodytų metų intervale
    rezultatas = filtruoti_duomenys.groupby(['savivaldybe', 'year']).size().unstack(fill_value=0)

    # Išrenkame duomenis, kurie didesni arba = 1
    rezultatas = rezultatas[rezultatas >= 1]

    # Pašaliname eilutes, kuriose reikšmė NAN
    rezultatas = rezultatas.dropna()

    # Transformuojame duomenis iš stulpelio į eilutę, kad galėtume pasinaudoti Seaborn biblioteka
    rezultato_ilgis = rezultatas.reset_index().melt(id_vars='savivaldybe', var_name='year', value_name='count')

    # Pasirenkame spalvas grafiko vizualizavimui
    palette = sns.color_palette("Paired", n_colors=len(rezultato_ilgis['savivaldybe'].unique()))
    plt.figure(figsize=(15, 7))

    # Kuriame linijinę diagramą naudodami Seaborn biblioteka
    sns.lineplot(data=rezultato_ilgis, x='year', y='count', hue='savivaldybe', marker='o', palette=palette)
    plt.title(f'Profesinių ligų skaičiaus kitimas savivaldybėse {year_start}-{year_end} metais')
    plt.xlabel('Metai')
    plt.ylabel('Ligų skaičius')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Savivaldybe', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig("Pictures\pokytis.png")
    plt.show()

# Tiriame profesinių ligų atvejų skaičiaus kitimą naudodami linijinę regresiją
def regresija(year_start,year_end):
    year_start = year_start
    year_end = year_end

    # Filtruojame duomenis pagal metų intervalą
    filtruoti_duomenys = Asmuo[Asmuo['year'].between(year_start, year_end)]

    # Grupuojame duomenis pagal savivaldybes ir metus, skaičiuojame profesinių ligų atvejų skaičių kiekvienai
    # savivaldybei nurodytų metų intervale
    rezultatas = filtruoti_duomenys.groupby(['savivaldybe', 'year']).size().unstack(fill_value=0)

    # Sumuojame ligų atvejų skaičių
    rezultatas_per_metus_savivaldybe = rezultatas.sum(axis=1)

    # Išrenkame tik tas savivaldybes, kurios turi bent vieną ligos atvejį
    filtruota_savivaldybes = rezultatas_per_metus_savivaldybe[rezultatas_per_metus_savivaldybe > 0].index

    # Rezultatas apie savivaldybes kuriose yra bent vienas atvejis
    filtruoti_rezultatas = rezultatas.loc[filtruota_savivaldybes]

    # Pertvarkome duomenis, kad būtų paprasčiau juos atvaizduoti linijinės regresijos analizėje
    filtruoti_rezultatas_ilgis = filtruoti_rezultatas.reset_index().melt(id_vars='savivaldybe', var_name='year',
                                                                         value_name='count')
    # Konvertuojame metų stulpelį į skaičių
    filtruoti_rezultatas_ilgis['year'] = pd.to_numeric(filtruoti_rezultatas_ilgis['year'], errors='coerce')

    # Pašaliname eilutes kuriose trūksta duomenų
    filtruoti_rezultatas_ilgis = filtruoti_rezultatas_ilgis.dropna(subset=['year'])

    # Konvertuojame metų stulpelį į sveikus skaičius
    filtruoti_rezultatas_ilgis['year'] = filtruoti_rezultatas_ilgis['year'].astype(int)

    # Kuriame grafiką
    plt.figure(figsize=(15, 7))
    plt.title('Linijinė regresija pagal savivaldybes ir metus')
    plt.xticks(rotation=45, ha='right')

    # Sukuriame tuščią žodyną
    slopes = {}

    # Pradedame ciklą, grupuojame duomenis pagal savivaldybes
    for name, group in filtruoti_rezultatas_ilgis.groupby('savivaldybe'):

        # Skaičiuojame linijinės regresijos tendenciją kiekvienai savivaldybei
        slope, intercept, r_value, p_value, std_err = linregress(x=group['year'], y=group['count'])

        # Įrašome į žodyną
        slopes[name] = slope

    # Pradedame ciklą, grupuojame duomenis pagal savivaldybes
    for name, group in filtruoti_rezultatas_ilgis.groupby('savivaldybe'):

        # Tikriname ar žodyno elementas teigiamas
        if slopes[name] > 0:
            # jei > 0, sukuria regresijos grafiką su atitinkama savivaldybe
            sns.regplot(
                x='year', y='count', data=group,
                label=name, scatter_kws={'s': 50},
                line_kws={'linewidth': 2}, ci=None
            )

    # Grafiko parametrai
    plt.legend(title='Savivaldybe', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.xlabel('Metai')
    plt.ylabel('Skaičius')
    plt.savefig("Pictures\ regresija.png")
    plt.show()



# pagal_savivaldybes(2013,2023)
# profesiniu_lig_daz(2019)
# lytis(2013,2023)
# kitimas_metais(2005,2023)
regresija(2013,2023)