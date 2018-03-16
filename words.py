import codecs
from tkinter.filedialog import askopenfilename


def word_count(str): #Pass String. Return words and num of appearances
    counts = dict()
    words = str.split()
    for word in words:
        word = word.capitalize()
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def fileToString():#opens files and converts it into a string. Prints it
    filename = askopenfilename()
    file = codecs.open(filename,'r', encoding='utf-8')
    listOfLines = file.readlines() #turns file into list of strings
    sizeOfList = len(listOfLines) 
    stringFromList = ""
    for x in range(sizeOfList): #converts list into one big string
        listOfLines[x] = listOfLines[x].replace("\n", " ")
        listOfLines[x] = listOfLines[x].replace("\t", "")
        listOfLines[x] = listOfLines[x].replace(".", "")
        listOfLines[x] = listOfLines[x].replace("'s", "")
        listOfLines[x] = listOfLines[x].replace(",", "")
        listOfLines[x] = listOfLines[x].replace(":", "")
        listOfLines[x] = listOfLines[x].replace("?", "")
        listOfLines[x] = listOfLines[x].replace("!", "")
        stringFromList = stringFromList + listOfLines[x] #One big string
    print(narrowedDownWords(word_count(stringFromList)))

def narrowedDownWords(counts):
    for w in sorted(counts, key=counts.get, reverse=True): #sorts dict
            if(counts[w] > 0):
                print (w, counts[w])
    
    
        
def main():
    fileToString()
    

if __name__ == "__main__":
    main()
