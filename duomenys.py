import pandas as pd
# from web_scrap import scrape_table
#
#
# asmuo = scrape_table()
# asmuo = pd.DataFrame(asmuo,columns=['id','m_id','pagr_tlk_kodas._id','pagr_tlk_pav._id','papild_tlk_kodas._id',
#                                     'papild_tlk_pav._id','ligos_eiga','itarta_pav','itarta_kodas','priezasties_kodas',
#                                     'priezasties_pav','lyties_kodas','lyties_pavadinimas','savivaldybe','year','quarter'])
#
# asmuo.to_csv("CSV file\ asmenys.csv", index=False)
#
# Kadangi interneto svetaineje yra apribojimas iki 100 eilučių, mūsų pasirinktas variantas netenkina, todėl tenka kreiptis į
# duomenu bazeje pateiktus csv failus, kad analizė būtų vaizdingesnė ir pilnesnė.
def get_data():
    url = "https://get.data.gov.lt/datasets/gov/hi/profesines/Asmuo/:format/csv"
    Asmuo = pd.read_csv(url)
    Asmuo = Asmuo.drop(
        ['_type', '_id', '_revision', 'm_id', 'pagr_tlk_kodas._id', 'pagr_tlk_pav._id', 'papild_tlk_kodas._id',
         'papild_tlk_pav._id', 'ligos_eiga', 'itarta_pav', 'itarta_kodas', 'priezasties_kodas', 'quarter'], axis=1)

    return Asmuo


# get_data().to_csv("CSV file\ Asmuo_new.csv", index=False)
#
# print(get_data().dtypes)
