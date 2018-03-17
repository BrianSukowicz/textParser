import codecs
import sys
from tkinter.filedialog import askopenfilename

def getFilePath(): #open dialog and get filepath
    filename = askopenfilename()
    if (not filename):
        sys.exit()
    file = codecs.open(filename,'r', encoding='utf-8')
    return file

def fileToListOfLines(myFile): #converts text in file into list of lines
    listOfLines = myFile.readlines() #turns file into list of strings
    myFile.close()
    return listOfLines

def listToString(myList): #converts list to a big string
    stringFromList = ""
    for x in range(len(myList)):
        myList[x] = myList[x].replace("\n", " ") #removes new line
        myList[x] = myList[x].replace("\t", "") #removes tab
        stringFromList = stringFromList + myList[x] 
    return stringFromList

def stringToListOfWords(myStr): #converts a string into list of words
    words = myStr.split()
    return words

def editListOfWords(words):
    for x in range(len(words)):
        words[x] = words[x].capitalize()
        words[x] = words[x].replace('.', "")
        words[x] = words[x].replace(",", "")
        words[x] = words[x].replace("?", "")
        words[x] = words[x].replace("!", "")
        words[x] = words[x].replace(";", "")
        words[x] = words[x].replace(":", "")
        words[x] = words[x].replace("(", "")
        words[x] = words[x].replace(")", "")
        words[x] = words[x].replace("{", "")
        words[x] = words[x].replace("}", "")
        words[x] = words[x].replace("/", "")
        words[x] = words[x].replace("[", "")
        words[x] = words[x].replace("]", "")
        words[x] = words[x].replace("'", "")
        words[x] = words[x].replace("'s", "")
        words[x] = words[x].replace('"', "")
    return words

def getWordCount(words):
    counts = dict()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def printWordCounts(counts):
    for w in sorted(counts, key=counts.get, reverse=True): #sorts dict
            if(counts[w] > 0):
                print (w, ":", counts[w])
    
 
    
def main():
    printWordCounts(getWordCount(editListOfWords(stringToListOfWords(listToString(fileToListOfLines(getFilePath()))))))
    

if __name__ == "__main__":
    main()
    
    
    
