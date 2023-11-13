import pandas as pd
# from web_scrap import scrape_table
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import psycopg2
# asmuo=scrape_table("https://get.data.gov.lt/datasets/gov/hi/profesines/Asmuo")
# asmuo = pd.DataFrame(asmuo,columns=['id','m_id','pagr_tlk_kodas._id','pagr_tlk_pav._id','papild_tlk_kodas._id',
#                                     'papild_tlk_pav._id','ligos_eiga','itarta_pav','itarta_kodas','priezasties_kodas',
#                                     'priezasties_pav','lyties_kodas','lyties_pavadinimas','savivaldybe','year','quarter'])
#
# asmuo.to_csv("asmenys.csv", index=False)
#
#
# darbo_stazas=scrape_table("https://get.data.gov.lt/datasets/gov/hi/profesines/DarboStazas")
# darbo_stazas = pd.DataFrame(darbo_stazas, columns=['id','atvejis_id','pagr_tlk_kodas._id','pagr_tlk_pav._id',
#                                                    'lpk','evrk','stazas','year','quarter'])
#
# darbo_stazas.to_csv("darbo_stazas.csv", index=False)

# Kadangi interneto svetaineje yra apribojimas iki 100 eilučių, mūsų pasirinktas variantas netenkina, todėl tenka kreiptis į
# duomenu bazeje pateiktus csv failus, kad analizė būtų vaizdingesnė ir pilnesnė.

url = "https://get.data.gov.lt/datasets/gov/hi/profesines/Asmuo/:format/csv"
Asmuo = pd.read_csv(url)
Asmuo = Asmuo.drop(['_type', '_id', '_revision','m_id','pagr_tlk_kodas._id','pagr_tlk_pav._id','papild_tlk_kodas._id',
                    'papild_tlk_pav._id'], axis=1)
Asmuo.to_csv("Asmuo_new.csv", index=False)
