import os
from bs4 import BeautifulSoup
if os.path.exists("./testfile_drug_prescription.html"):
    os.remove("./testfile_drug_prescription.html")
if os.path.exists("../processed/drug_prescription.txt"):
    os.remove("../processed/drug_prescription.txt")


with open("../htmlFile/index.html", "r") as html:
    file = open("testfile_drug_prescription.html", "a")
    for line in html:
        if "Applied date:" in line:
            file.write('<div class="applieddate">' +
                       line.strip() + "</div>\n")


with open("testfile_drug_prescription.html", "r") as html:
    file = open("../processed/drug_prescription.txt", "a")
    for line in html:
        t = line.rindex("<br><br>", 0, len(line) - 10)
        file.write(line[t:].replace("<br>", "").replace("</div>", ""))
