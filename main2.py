import pandas as pd
import re
from html5print import HTMLBeautifier
import html2text
import pprint
h = html2text.HTML2Text()
h.ignore_links = True
pp = pprint.PrettyPrinter(indent=4)

drugs = []
chk = False
chk2 = False
chk3 = False
with open('index.html', 'r') as file:
    stringHTML = file.read()
    s = HTMLBeautifier.beautify(stringHTML, 4)
    drug = {}
    drug['PE'] = "no"
    drug['NN'] = "no"
    drug['CA'] = "no"
    strParsed = h.handle(s)
    strParsed += "##"
    tarr = []
    tarrr = []
    # print(strParsed)
    for line in strParsed.splitlines():

        if line.find("##") != -1:
            drugs.append(drug)
            drug = {}
            drug['PE'] = "no"
            drug['NN'] = "no"
            drug['CA'] = "no"
            drug['name'] = line[3:line.find("-")].strip()
        if line.find("Dosage form:") != -1:
            drug['dosage_form'] = line[line.find(":") + 1:].strip()
        if line.find("Aspnr:") != -1:
            drug['Asprn'] = line[line.find(":")+1:].strip()
        if line.find("Strength:") != -1:
            drug['strength'] = line[line.find(":") + 1:].strip()
        if line.find("Manufacturer:") != -1:
            drug['manufacturer'] = line[line.find(":") + 1:].strip()
        if line.find("Agent:") != -1:
            drug['agent'] = line[line.find(":") + 1:].strip()
        if line.find("MAH:") != -1:
            drug['MAH'] = line[line.find(":") + 1:].strip()
        if line.find("Prescription only") != -1:
            drug['PE'] = "yes"

        if line.find("Not classified as a narcotic") != -1:
            drug['NN'] = "yes"

        if line.find("Centrally approved e") != -1:
            drug['CA'] = "yes"

        if line.find("Applied date:") != -1:
            arr = line.split()
            try:
                drug['applied_date'] = arr[2]
            except:
                drug['applied_date'] = "NA"
            try:
                drug['reg_number'] = arr[5] if len(arr[5]) != 0 else "NA"
            except:
                drug['reg_number'] = "NA"
            try:
                drug['appr_date'] = arr[8]
            except:
                drug['appr_date'] = "NA"

        if line.find("Expiry date:") != -1:
            drug['expiry_date'] = line[line.find(":") + 1:]
        if line.find("ATC-code:") != -1:
            drug['ATC-code'] = line[line.find(":") + 1:].strip()
            chk = True
        if chk == True and line.find("|") == -1:
            tarr.append(line)
        if chk == True and line.find("|") != -1:
            comments = ""
            for e in tarr:
                if e.find("ATC") != -1 or len(e.strip()) == 0:
                    continue
                else:
                    comments += e
            drug['comments'] = comments
            tarr = []
            chk = False
        if line.find("Old tradenames") != -1:
            chk3 = True
        if chk3 and line.find("Datum") != -1:
            drug['old_name'] = line[line.find(":")+1:].strip()
            chk3 = False

            # drugs.append(drug)
        if line.find("Ingredients") != -1:
            chk2 = True
            tarrr.append(line[line.find("Active"):])
            continue
        if chk2 and len(line.strip()) != 0:
            tarrr.append(line)
        if chk2 and len(line.strip()) == 0:
            drug['ingredients'] = tarrr
            tarrr = []
            chk2 = False

# --- ingredients ---
    drugsWithIngredients = []

    for drug in drugs:
        d = {}
        d['active_ingredient'] = []
        d['active_corresponding_to'] = []
        d['antimicrobial_preservative'] = []
        d['aroma'] = []
        d['colourant'] = []
        d['other_constituent'] = []
        d['other_substance_corresponding_to'] = []
        try:
            # print(drug['ingredients'][2:])
            for i in drug['ingredients'][2:]:
                if i.find("Active ingredient") != -1:
                    d['active_ingredient'].append(
                        "".join(i.split('Active ingredient')).strip())
                if i.find("Active corresponding to") != -1:
                    d['active_corresponding_to'].append(
                        "".join(i.split('Active corresponding to')).strip())
                if i.find("Antimicrobial preservative") != -1:
                    d['antimicrobial_preservative'].append(
                        "".join(i.split('Antimicrobial preservative')).strip())
                if i.find("Aroma") != -1:
                    d['aroma'].append(
                        "".join(i.split('Aroma')).strip())
                if i.find("Colourant") != -1:
                    d['colourant'].append(
                        "".join(i.split('Colourant')).strip())
                    # Other constituent
                # print(i)
                if i.find("Other constitutent ") != -1:
                    d['other_constituent'].append(
                        "".join(i.split('Other constitutent ')).strip())
                # Other substance corresponding to
                if i.find("Other substance corresponding to") != -1:
                    d['other_substance_corresponding_to'].append(
                        "".join(i.split('Other substance corresponding to')).strip())
            drug['ingredients'] = d
            drugsWithIngredients.append(drug)
        except:
            print("NA")
            #df = pd.DataFrame(drugs)
            # with open("tableView.txt", 'a') as f:
            #    f.write(df.to_string(header=True, index=True))
            # pp.pprint(drugs)
pp.pprint(drugsWithIngredients)
