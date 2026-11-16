
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
RESET = '\033[0m'


def handleEdgeCase(letter):   

    match letter:    

        case "ا": return 'b'
        case "أ": return 'G'
        case "إ": return 'T'
        case "آ": return 'B'
        case _: return letter   

def toِArabic(sentence):

    EN_to_AR: dict[str, str] = {
        
        "q": "ض", "w": "ص", "e": "ث", "r": "ق",
        "t": "ف", "y": "غ", "u": "ع", "\\": "\\",
        "i": "ه", "o": "خ", "p": "ح", "[": "ج", "]": "د",
        "a": "ش", "s": "س", "d": "ي", "f": "ب", "g": "ل",
        "h": "ا", "j": "ت", "k": "ن", "l": "م", ";": "ك", "'": "ط",
        "`": "ذ", "z": "ئ", "x": "ء", "c": "ؤ", "v": "ر",
        "b": "لا", "n": "ى", "m": "ة", ",": "و", ".": "ز", "/": "ظ",
    
        "Q": "َ", "W": "ً", "E": "ُ", "R": "ٌ", "T": "لإ",
        "Y": "إ", "U": "‘", "I": "÷", "O": "×", "P": "؛",
        "{": "<", "}": ">",
    
        "A": "ِ", "S": "ٍ", "D": "]", "F": "[", "G": "لأ",
        "H": "أ", "J": "ـ", "K": "،", "L": "/",
        ":": ":", "\"": "\"",
    
        "Z": "~", "X": "ْ", "C": "}", "V": "{", "B": "لآ",
        "N": "آ", "M": "’", "<": ",", ">": ".",

        "!": "!", "@": "@", "$": "$", "%": "%",
        "^": "^", "&": "&", "*": "*", "(": "(",
        ")": ")", "-": "-", "_": "_", "=": "=", "+": "+"
        
    }
    
    mashed = " "
    isSuccessful = True
    
    for i in range(len(sentence)):

        if (sentence[i].isspace()):
            mashed += ' '
            continue

        if(str(sentence[i]).isnumeric()):
            mashed += sentence[i]
            continue

        try:    
            mashed += EN_to_AR[sentence[i]]
                
        except KeyError: 
                print(f"\n{RED}Invalid English Letter '{sentence[i]}'{RESET}")
                isSuccessful = False
                break

    return mashed, isSuccessful

def toEnglish(letter):

        Ar_to_En: dict[str, str] = {
            
    "ض": "q", "ص": "w", "ث": "e", "ق": "r",
    "ف": "t", "غ": "y", "ع": "u", "\\": "\\",
    "ه": "i", "خ": "o", "ح": "p", "ج": "[", "د": "]",
    "ش": "a", "س": "s", "ي": "d", "ب": "f", "ل": "g",
    "ا": "h", "ت": "j", "ن": "k", "م": "l", "ك": ";", "ط": "'",
    "ذ": "`", "ئ": "z", "ء": "x", "ؤ": "c", "ر": "v",
    "لا": "b", "ى": "n", "ة": "m", "و": ",", "ز": ".", "ظ": "/",

    "َ": "Q", "ً": "W", "ُ": "E", "ٌ": "R", "لإ": "T",
    "إ": "Y", "‘": "U", "÷": "I", "×": "O", "؛": "P",
    "<": "{", ">": "}",

    "ِ": "A", "ٍ": "S", "]": "D", "[": "F", "لأ": "G",
    "أ": "H", "ـ": "J", "،": "K", "/": "L", ":": ":",
    "\"": "\"",

    "~": "Z", "ْ": "X", "}": "C", "{": "V", "لآ": "B",
    "آ": "N", "’": "M", ",": "<", ".": ">",

    "ّ": "~", "!": "!", "@": "@", "$": "$", 
    "%": "%", "^": "^", "&": "&", "*": "*",
    
    "(": "(", ")": ")", "-": "-", "_": "_",
    "=": "=", "+": "+" 
    
}
        mashed = " "
        
        isValid = True
        skip = False
        isSuccessful = True

        for i in range(len(sentence)):

            if (skip):
                
                skip = False
                continue

            if (i == len(sentence)-1): isValid = False

                
            if (sentence[i].isspace()):
                
                mashed += ' '
                continue
            
            if(str(sentence[i]).isnumeric()):

                mashed+= sentence[i]
                continue


            if(sentence[i] == 'ل' and isValid): 
               
                letter = handleEdgeCase(sentence[i+1])

                if (letter != sentence[i+1]): 

                    mashed += letter
                    skip = True
                    continue 
                
            try: 
                mashed += Ar_to_En[sentence[i]]
                      
            except KeyError: 
                      print(f"\n{RED}Invalid Arabic Letter '{sentence[i]}'{RESET}")
                      isSuccessful = False
                      break

        return mashed , isSuccessful


while(True):
    
    print("\n[1] Mash to Arabic.\n[2] Mash to English.\n[Q] Quit.")
    
    mode = input(f"\nChoose a Mode: {RED}▸{RESET} ").strip().capitalize()
    mashed = ''
    
    
    if mode == '1':

        sentence = input("\nEnter a Sentence to Mash it to Arabic: ").strip()
        mashed, isSuccessful = toِArabic(sentence) 

        if (isSuccessful): 
            print(f"\n{GREEN}{mashed}{RESET}")

    elif mode == '2':

        sentence = input("\nEnter a Sentence to Mash it to English: ").strip()
        mashed, isSuccessful = toEnglish(sentence) 

        if (isSuccessful): 
            print(f"\n{GREEN}{mashed}{RESET}")


    elif mode == 'Q':

        print(f"\n {BLUE}Good Bye{RESET} ^_^")
        break

    else:

        print(f"\n{RED}Invalid input{RESET}")
        continue

    with open("DeMash_output.txt", "w", encoding="utf-8") as file:

        file.writelines(mashed)
        file.writelines('\n')
        file.close()
