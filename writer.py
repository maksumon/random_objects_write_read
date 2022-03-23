import random
import string
import os
import json

MAX_FILE_SIZE = 2097152

# let's define a function for creating a string of random alphanumerical characters
def random_alphanumerics():
    length = random.randint(5, 15) # define the length of the alphanumeric string randomly between a range
    output = ''
    for i in range(length):
        output += random.choice(string.ascii_lowercase + string.digits) # create our alphanumeric string
    return output

# let's define a function for creating a string of random alphabetical characters
def random_string():
    length = random.randint(5, 15) # define the length of the alphabetical string randomly between a range
    output = ''.join(random.choice(string.ascii_lowercase) for x in range(length)) # we are using ascii lowercase so that encoding doesn't cause our file size to be unpredictable
    return output

# let's define a function for creating a random integers and converting them to a string
def random_int():
    output = random.randint(0, 10000)
    intToStr = '{}'.format(output)
    return intToStr

# let's define a function for creating random floats and converting them to a string
def random_float():
    length = random.randint(1, 10) # let's make sure the float is between a randomly chosen decimal place
    output = round(random.uniform(0.0, 10000.0), length)
    floatToStr = '{}'.format(output)
    return floatToStr

# let's define a function for generating random objects
def generate_objects():
    # let's define our file name first
    fileName = 'random_objects.txt'
    open(fileName, 'w')

    # let's check the initial size of the file which should be 0
    fileSize = os.stat(fileName).st_size

    # alright let's open the file and append data to it
    with open(fileName, 'a') as myFile:
        while fileSize < MAX_FILE_SIZE: # run the loop until fileSize is MAX_FILE_SIZE
            function_list = [
                random_alphanumerics,
                random_string,
                random_int,
                random_float
            ] # put our functions into a list
            dataType = random.choice(function_list) # randomly choose a function to run
            output = dataType()
            myFile.write(output + ',')
            fileSize = os.stat(fileName).st_size
            print(fileSize)
        # once loop is done, print final file size and close file
        print('Final file size:', fileSize / 1000000, 'MB')
        myFile.close()
    # Create Dictionary
    dictionary = {
        "fileName": fileName
    }
    # Return JSON Object
    return json.dumps(dictionary)