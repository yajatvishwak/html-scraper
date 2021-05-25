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
with open("../htmlFile/index.html", "r") as html:
    file = open("testfile.txt", "a")
    soup = BeautifulSoup(html, 'html.parser')

    for div in soup.find_all("h2",
                             # attrs={
                             #   'cellspacing': '0',
                             #   'cellpadding': '0',
                             #   'width': '798',
                             #  "border": "0"}
                             ):
        file.write(div.text)


with open("testfile.txt", "r") as name:
    file = open("../processed/drug_name.txt", "a")
    for line in name:
        if ":" in line and "-" in line:
            file.write(line)
