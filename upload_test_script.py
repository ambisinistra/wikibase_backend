from my_config import *
from wikidataintegrator import wdi_core, wdi_login

import pandas as pd
import tqdm

wdi_core.config = config_config

logincreds = wdi_login.WDLogin(user=config_login, pwd=config_pass, mediawiki_api_url=f"{config_wb_url}/w/api.php")

class Wikibase_Loader:

    def __init__(self):
        pass


    def load_from_tsv(self, names=[]):

        counter = 0

        for number, name in enumerate(names):
            print ("loading table {} from {}".format(number + 1, len(names)))
            df = pd.read_csv(name, sep='\t')
            df = df[df["Kind#string"] == "Tag"]

            entities = list(set(df["Name#string"]))
            
            for entity in entities:
                item_to_load = wdi_core.WDItemEngine()
                item_to_load.set_label(entity)
                try:
                    item_to_load.write(logincreds)
                    counter += 1
                except NonUniqueLabelDescriptionPairError:
                    print ("entity creation with name {} failed. It already exist".format(entity))
        
        print ("totally entities loaded", counter)

my_loader = Wikibase_Loader()

files_to_load = ['Metadata Overview (Археология).tsv', \
    'Metadata Overview (Виды человеческой деятельности).tsv', \
    'Metadata Overview (временные периоды).tsv', \
    'Metadata Overview (Локализации).tsv', \
    'Metadata Overview (Люди).tsv', \
    'Metadata Overview (результаты человеческой деятельности).tsv']

my_loader.load_from_tsv(files_to_load)