import re
import json

def generate_report():
    # let's define our file name first
    fileName = 'random_objects.txt'
    
    # alright let's open the file in read mode
    with open(fileName, 'r') as myFile:
        string = myFile.read()
        listAlphabaticObjects = re.findall(r"[a-z]+", string)
        listAlphanumericObjects = re.findall(r"\w+", string)
        listIntegerObjects = re.findall(r"d+", string)
        listRealObjects = re.findall(r"\d+.d+", string)
        print('Alphabetics: {}'.format(len(listAlphabaticObjects)))
        print('Alphanumerics: {}'.format(len(listAlphanumericObjects)))
        print('Integers: {}'.format(len(listIntegerObjects)))
        print('Reals: {}'.format(len(listRealObjects)))
        myFile.close()
        # Create Dictionary
        dictionary = {
            "alphabetics": len(listAlphabaticObjects),
            "alphanumerics": len(listAlphanumericObjects),
            "integers": len(listIntegerObjects),
            "reals": len(listRealObjects)
        }
        # Return JSON Object
        return json.dumps(dictionary)