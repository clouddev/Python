def ShortenName(name):
    shortenedName = ""
    if 10 <= len(name) <= 60:
        
        spltName = name.split()
        
            if len(spltName) >= 3:
            middleName = spltName[-1]
            middleInitial = middleName[0] + "."
            newList = []
            for i in range(0, len(spltName) -1 ):
                newList.append(spltName[i])
            newList.append(middleInitial)
            shortenedName = " ".join(newList)
            return shortenedName
        else:
            return name
    else:
        return "Error"
