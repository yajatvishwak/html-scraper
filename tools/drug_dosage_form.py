from bs4 import BeautifulSoup
with open("../htmlFile/index.html", "r") as html:
    file = open("testfile_drug_dosage.txt", "a")
    soup = BeautifulSoup(html, 'html.parser')

    for div in soup.findAll(text=lambda t: "Dosage form:" in t):
        file.write(div)

with open("testfile_drug_dosage.txt", "r") as name:
    file = open("../processed/drug_dosage_form.txt", "a")
    for line in name:
        if line.strip().isalnum:
            file.write(line.strip() + "\n")
