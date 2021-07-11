from my_config import *
from wikidataintegrator import wdi_core, wdi_login

wdi_core.config = config_config

logincreds = wdi_login.WDLogin(user=config_login, pwd=config_pass, mediawiki_api_url=f"{config_wb_url}/w/api.php")

#create some WDItemEngine here