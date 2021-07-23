from sys import argv as ag

def palindrome ( string ):
    a = ""

    validate = "".join ( string.lower().split(""))
    if validate [::-1] = validate:
        return True
    else: 
        return False
    ##string = string.lower()
    ##stringList = string.split ("")
    ##string = "".join (stringList)
    ##print(stringList)
    ##print (string)


if __name__ == "__main__":
    print (palindrome ( "AMor A Roma"))