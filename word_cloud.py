# Python 3

# Please use the included copy of 98-0.txt, the text of
# of A Tale of Two Cities, by Charles Dickens

import collections

# open the 98-0.txt input file
input_file=open('98-0.txt', encoding="utf8")
stopword_file=open('stopwords.txt', encoding="utf8")

# number of words to print is 10
num_words = 10

# Part 1: setup the SET of stop words to do this:
# 1. create a set (already done for you)
stopwords=set()

# 2. for each word in the stopword file, add the word to the list.
# Hints: you may wish to read in each line, then use line.split() to get each word
#        when adding each word, you'll want to use word.strip() to remove whitespace
for line in stopword_file:
    line = line.strip()
    line=line.split()           #  as each line contains only a single word
    stopwords.add(line[0])      #  adding that single word

# For debugging, you can print your set here:
#print(stopwords)
#print(len(stopwords))

# Part 2: Instantiate a dictionary, and for every word in the file, add to 
# the dictionary if it doesn't exist. If the word is already present, increase the count.


# 1. create your data structure here - you'll want to use a dictionary like below:
wordcount={'':0}

# 2. For each word in the input file:
#    a. use .lower() to make lower case and .strip() to remove whitespace
#    b. use .replace(<from>,<to>) to replace each ".", ",", "\"" <-- the \" allows
#       you to remove a quotation mark.  For example:
#word="banana".replace("a","0")
#print(word)
#    c. check to make sure the word isn't in the list of stopwords.  If it isn't:
#    d. if the word isn't already in your dictionary, add it with the count of 1.
#       if the word is in the dictionary, add 1 to the present count

#   Following symbols are to be removed from words....
symbols = [',','.','!','?','(',')','\"',':',';','[',']','#','--']


for line in input_file:
    words=line.split()      # 'words' contains list of the words i.e. strings
    for a_word in words:
        word=a_word.lower()         # converting the word into lowercase
        for s in symbols:           # removing symbols and stripping whitespaces
            word=word.replace(s,'')
            word=word.strip()
        if(word not in stopwords):          # word should not be in 'stopwords'
            #       print(word)   :       debugging
            temp=1
            str='newly added'
            for key,value in wordcount.items():
                if(word == key):        # if word already exists ,
                    temp=value+1        # increase its value by 1
                    str='Increment in'
                    break
            wordcount[word]=temp
            #       print(str,' ',word)   :    debugging


####################        print(wordcount)        :  debugging     ######################



# Part 3, we want to print the top n most frequent words
# An easy way to sort your dictionary is to use collections.Counter.
# If you want, collections.Counter may be useful.  For example:
d = collections.Counter(wordcount)
########################   print(d)     : debugging     ###################
# Lastly, you'll want to iterate through the 10 most common elements
# in the collection, e.g., using d.most_common(10) which returns a list of tuples
# and print the word and its count
common_words=d.most_common(num_words)       # list of tuples e.g. [('said':444),('mr':555)]
for common_word in common_words:            # remember 'common_word' is a tuple
    print(common_word[0],' : ',common_word[1])
