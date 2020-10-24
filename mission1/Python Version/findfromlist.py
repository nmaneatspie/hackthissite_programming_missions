
#Norman Thien
#Date created: 23/10/2020
#Last Modified: 24/10/2020

#Code used to complete mission 1 of the programming challenge on hackthissite.com
#Essentially recieves input strings in file and tries to unjumble them to one of the words
#in the included dictionary file. Code assumes the jumbled word has unjumbled solution
#in the file.

#sys.exit code 1 should log error to file
#sys.exit code 2 has issues logging error

#Library imports
import sys
import datetime

#Variables
debug = True #just for testing/debugging in visual studio

dictionary_file = "dictionary.txt"
jumbled_file = "jumbled.txt"
results_file = "results.txt"
dictionary_words = []
jumbled_words = []

#Functions
#File loading function
def load_file(filename, err_num):
    try:
        if debug == True:
            from os.path import dirname, join
            current_dir = dirname(__file__)
            file_path = join(current_dir, filename)
            file = open(file_path)
            return file
        else:
            file = open(filename)
            return file
    except:
        try:
            error_log(err_num, filename)
        except:
            sys.exit([2])
        sys.exit([1])

#File writing function
def write_file(filename, err_num):
    try:
        if debug == True:
            from os.path import dirname, join
            current_dir = dirname(__file__)
            file_path = join(current_dir, "Error_log.txt")
            file = open(file_path, 'a')
            return file
        else:
            file = open("Error_log.txt", 'a')
            return file
    except:
        error_log(err_num, filename)
    sys.exit([2])

#Error logging code: file related
def error_log(err_num, filename = ""):
    if err_num == -1: #Prevent looping when writing error to log
        sys.exit([2])
    err_msg = {
        1: "Error opening file {}".format(filename),
        2: "Error with reading from {}".format(dictionary_file),
        3: "Error with closing dictionary file {}".format(dictionary_file),
        4: "Error reading from {}".format(jumbled_file),
        5: "Error with closing dictionary file {}".format(jumbled_file),
        }
    try:
        file = write_file(filename, -1)
        file.write("{} ".format(datetime.datetime.now()))
        file.write("{}\n".format(err_msg.get(err_num)))
        file.close()
    except:
        sys.exit([2])
    sys.exit([1])

#Main code:

#Load dictionary words into array from file.
file = load_file(dictionary_file, 1)

try:
    for x in file: #Dictionary file has each word on it's own line
        dictionary_words.append(x)
except:
    error_log(2)

try:
    file.close()
except:
    error_log(3)

#Load jumbled words from file
file = load_file(jumbled_file, 1)

try:
    for x in file:
        jumbled_words.append(x)
except:
    error_log(4)

try:
    file.close
except:
    error_log(5)