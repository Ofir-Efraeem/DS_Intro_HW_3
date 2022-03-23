
#A
def read_line(n,file):
    try:
        file=open(file)
        if(type(n)== int):
            counter=1
            for line in file:
                if n == counter:
                    return line
                counter=counter+1
            return "line " + str(n) + " doesn't exist"
        else:
            return "invalid input detected"
    except:
        return "file doesn't exist"

#B
def longest_words(file):
    try:
        file = open(file)

        lst = ["a","a","a","a","a"]
        for line in file:
            line = line.replace('.', ' ')
            line=line.split()
            for word in line:
                word = word.replace('-','')
                word = word.replace(',','')
                if len(word) > len(lst[4]):
                    lst[4] = word
                    lst.sort(key=len, reverse=True)
        return lst
    except:
        return "file doesn't exist"

print(longest_words('ex3_text.txt'))






