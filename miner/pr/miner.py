#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 20:04:38 2017

@author: projeto_teta
"""
import requests
from bs4 import BeautifulSoup

pagina_principal = requests.get("http://www.alep.pr.gov.br/transparencia/fiscalize/verbas-de-ressarcimento/")
soup = BeautifulSoup(pagina_principal.content, 'html.parser')

meses = soup.find(id="select-date")

"""
for mes in meses.find_all('option'):
    pagina_mes = requests.get("http://www.alep.pr.gov.br/transparencia/ajax/?ID="+mes['value'])
    soup_mes = BeautifulSoup(pagina_mes.content,'html.parser')
    
    docs = soup.find("a")
    print(docs)
"""

pagina_mes = requests.get("http://www.alep.pr.gov.br/transparencia/ajax/?ID=34654")
soup_mes = BeautifulSoup(pagina_mes.content,'html.parser')
docs = soup.find_all("a")

for doc in docs:
    link_doc = doc.get('href')
    if link_doc.endswith('pdf'):
        print(link_doc)