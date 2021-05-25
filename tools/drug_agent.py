import os
from bs4 import BeautifulSoup
if os.path.exists("./testfile_drug_agent.txt"):
    os.remove("./testfile_drug_agent.txt")
if os.path.exists("../processed/drug_agent.txt"):
    os.remove("../processed/drug_agent.txt")

with open("../sanitizedhtml/sanitized_agent.html", "r") as html:
    file = open("testfile_drug_agent.txt", "w")
    soup = BeautifulSoup(html, 'html.parser')

    for div in soup.findAll(text=lambda t: "Agent:" in t):
        if "null" in div:
            file.write(div.strip() + "\n")
        else:
            file.write("Agent: " + div.find_next("a").text.strip() + "\n")


with open("testfile_drug_agent.txt", "r") as name:
    file = open("../processed/drug_agent.txt", "a")
    for line in name:
        file.write(line.strip() + "\n")
