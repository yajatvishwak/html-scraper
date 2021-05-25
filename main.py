from bs4 import BeautifulSoup
import re

html = """
<table cellspacing="0">
            <td bgcolor="#555555">
               <table cellspacing="0" cellpadding="0" border="0" width="798">
                  <td bgcolor="#DDE2D7">
                     <h2>Abilify - Aspnr: 020038 </h2>
                  </td>
               </table>
            </td>
         </table>

"""
with open("index.html", "r") as html:
    file = open("testfile.txt", "a")
    soup = BeautifulSoup(html, 'html.parser')

    for div in soup.findAll(text=lambda t: "Dosage form:" in t):
        file.write(div)

    # for div in soup.find_all("table", attrs={
    #     # 'cellspacing': '0',
    #     # 'cellpadding': '0',
    #     'width': '795',lllll
    #         "border": "0"}):
    # file.write(div.td.text)


with open("testfile.txt", "r") as name:
    file = open("drug_dosage_form.txt", "a")
    for line in name:
        if line.strip().isalnum:
            file.write(line.strip() + "\n")
