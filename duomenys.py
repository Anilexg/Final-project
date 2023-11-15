import pandas as pd
# from web_scrap import scrape_table
#
# # Kreipiamės į funkciją iš web_scrap.py, kad gautime duomenis iš interneto puslapio lentelės
# asmuo = scrape_table()
#
# # Gauti duomenys keičiami į Pandas DataFrame su nurodytomis stulpelių pavadinimais
# asmuo = pd.DataFrame(asmuo,columns=['id','m_id','pagr_tlk_kodas._id','pagr_tlk_pav._id','papild_tlk_kodas._id',
#                                     'papild_tlk_pav._id','ligos_eiga','itarta_pav','itarta_kodas','priezasties_kodas',
#                                     'priezasties_pav','lyties_kodas','lyties_pavadinimas','savivaldybe','year','quarter'])
#
# # Išsaugome duomenis į CSV failą, nurodytu pavadinimu ir nurodytoje vietoje
# asmuo.to_csv("CSV file\ asmenys.csv", index=False)
# # Atsispausdiname
# print(asmuo)

# Kadangi interneto svetaineje yra apribojimas iki 100 eilučių, mūsų pasirinktas variantas netenkina, todėl tenka kreiptis į
# duomenu bazeje pateiktus csv failus, kad analizė būtų vaizdingesnė ir pilnesnė.

# Duomenų gavimas iš internetinio šaltinio
def get_data():

    # Nurodme interneto puslapio URL, iš kurio imsime duomenis
    url = "https://get.data.gov.lt/datasets/gov/hi/profesines/Asmuo/:format/csv"

    # Perkeliame duomenis iš CSV formato internetinio šaltinio į Pandas DataFrame.
    Asmuo = pd.read_csv(url)

    # Iš DataFrame pašaliname mums nereikalingus stulpelius
    Asmuo = Asmuo.drop(
        ['_type', '_id', '_revision', 'm_id', 'pagr_tlk_kodas._id', 'pagr_tlk_pav._id', 'papild_tlk_kodas._id',
         'papild_tlk_pav._id', 'ligos_eiga', 'itarta_pav', 'itarta_kodas', 'priezasties_kodas', 'quarter'], axis=1)

    # Grąžina duomenis
    return Asmuo

# Išsaugome duomenis į CSV failą, nurodytu pavadinimu ir nurodytoje vietoje
# get_data().to_csv("CSV file\ Asmuo_new.csv", index=False)

