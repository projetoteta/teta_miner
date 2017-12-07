import PyPDF2
import requests
import io
import re

pdf_content = io.BytesIO(requests.get("http://www.alep.pr.gov.br/transparencia/wp-content/uploads/2017/11/56_10_2017_Fornecedores.pdf").content)
pdf_reader = PyPDF2.PdfFileReader(pdf_content)

for i in range(0,pdf_reader.numPages):
    page = pdf_reader.getPage(i)
    arrStr = page.extractText().split("\n")
    strW = page.extractText().replace('\n','')
    
    for j in range(0,len(arrStr)):
        if arrStr[j] == 'Gabinete do Deputado :':
            print("DEPUTADO:",arrStr[j+1])
        elif arrStr[j] == 'Período de Apuração :':
            print("Período:",arrStr[j+1])
    
    m = re.finditer(r"[A-Z\b[A-Z][a-z][A-z\u00C0-\u017F\(\)\,\. \$\n]+\b", strW, re.MULTILINE)
    list_match = [match for match in m]
    
    for k in range(0,len(list_match)):
        if 'R$' in list_match[k].group(0):
            desp = strW[list_match[k].start()+len(list_match[k].group(0)) : list_match[k+1].start()]
            desp_split = re.sub( r"([A-Z])", r" \1", desp).split()
            if len(desp_split) > 1:
                print(list_match[k].group(0)[:-3])
                contador = 0
                for y in range(0,len(desp_split)):
                    r = re.search(r"(\d{2}.\d{3}.\d{3}/\d{4}-\d{2})", desp_split[y])
                    if r:
                        print(r.group(0),desp_split[y+1])
                        print(re.findall(r'[A-Z\u00C0-\u017F\.\- ]{2,}',desp)[contador])
                        contador += 1
                        
                print("-----------")

