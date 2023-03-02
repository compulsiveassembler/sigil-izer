#loop through replace_string_at_index when finding substring surrounded by
#vowels - - - - - - - > xvavx - - - - - > pass index of a into replace func
#and loop through all indexs - - - - > store indexes into list






def vowel_checker():

    

    return 

def replace_string_at_index(first_string, index, new_substring):

    if int(index) < len(first_string):
        subbed_string = first_string[0:int(index)] + new_substring +  first_string[int(index) + 1: ]
        return subbed_string
    else:    
        return "Index exceeds string length, error"


def substitute_letters():
    print("Please enter what you would like to be SIGIL'd: ")
    string1 = input()
    string1 = string1.lower()   
    string1 = string1.replace("a", "")
    string1 = string1.replace("e", "")
    string1 = string1.replace("i", "")
    string1 = string1.replace("o", "0")
    string1 = string1.replace("u","")

    print(string1)

    return


print("Enter string to be replaced: ")

string2 = input()

print("Enter index to be replaced")

index_num = input()

print("Enter character you would like to be used instead")

new_char = input()
    
print(replace_string_at_index(string2, index_num, new_char))


 