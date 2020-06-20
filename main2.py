import pandas as pd
from html5print import HTMLBeautifier
import html2text
import pprint
h = html2text.HTML2Text()
h.ignore_links = True
pp = pprint.PrettyPrinter(indent=4)

drugs = []
chk = False
chk2 = False
with open('index.html', 'r') as file:
    stringHTML = file.read()
    s = HTMLBeautifier.beautify(stringHTML, 4)
    drug = {}
    strParsed = h.handle(s)
    strParsed += "##"
    tarr = []
    tarrr = []
    # print(strParsed)
    for line in strParsed.splitlines():

        if line.find("##") != -1:
            drugs.append(drug)
            drug = {}
            drug['name'] = line[3:]
        if line.find("Dosage form:") != -1:
            drug['dosage_form'] = line[line.find(":") + 1:]
        if line.find("Strength:") != -1:
            drug['strength'] = line[line.find(":") + 1:]
        if line.find("Manufacturer:") != -1:
            drug['manufacturer'] = line[line.find(":") + 1:]
        if line.find("Agent:") != -1:
            drug['agent'] = line[line.find(":") + 1:]
        if line.find("MAH:") != -1:
            drug['mah'] = line[line.find(":") + 1:]
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
            drug['ATC-code'] = line[line.find(":") + 1:]
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
            drug['old_tradenames'] = "Datum:"+line[line.find(":") + 1:]

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

    # print(drugs)

df = pd.DataFrame(drugs)
with open("tableView.txt", 'a') as f:
    f.write(df.to_string(header=True, index=True))
pp.pprint(drugs)
