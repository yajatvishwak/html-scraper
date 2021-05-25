checkNextLine = False
counter = 0
with open("../htmlFile/index.html") as html:
    file = open("../sanitizedhtml/sanitized_agent.html", "a")
    for line in html:
        counter = counter+1
        if checkNextLine and counter == 3:
            if "Agent" not in line:
                print(line.split())
                file.write('''<br> Agent: null \n''')
                file.write(line)
                checkNextLine = False
            else:
                file.write(line)
                checkNextLine = False
        else:
            file.write(line)
        if "Manufacturer:" in line:
            checkNextLine = True
            counter = 0
