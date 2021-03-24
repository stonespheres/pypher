#Loads a text file and outputs a list

#Requires
import sys

def loadFile(file):
    #Open a file and return lowercase list of strings
    try:
        with open(file) as in_file:
            #Remove whitespace
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as error:
        print("{}Error opening {}. Terminating program.".format(error, file), file=sys.stderr)
        sys.exit(1)