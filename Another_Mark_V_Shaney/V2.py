#This function will load file with provided file name and return contents inside.
def load_file(filename):
    filevar = open(filename)
    sentences_ori = '. ' + filevar.read()
    filevar.close()
    return sentences_ori

#This function will take the original sentences and proceed it into a list of words.
def convert_list(sentences):
    sentences = sentences.lower()
    for punctuation in [',','?','*','(',')','"',';',':','-','@','\n','#']:
        sentences = sentences.replace(punctuation, " # ")
    sentences = sentences.replace('.', ' *')
    while '  ' in sentences:
        sentences = sentences.replace('  ', ' ')
    return sentences.split(' ')

#This function will take a word list and output a list of words that suiltable for starting a sentence.
def valid_start(word_list):
    valid_words = []
    for num in range(len(word_list)-1):
        if word_list[num] == '*' and word_list[num+1] != '#':
            if not word_list[num+1] in valid_words:
                valid_words.append(word_list[num+1])
    return valid_words

#This function will build a dictionary using the word list.
def build_dict(word_list):
    dictionary = {}
    for num in range(len(word_list)-2):
        searching, times = True, 0
        while searching:
            if (word_list[num], word_list[num+1], times) in dictionary:
                times += 1
            else:
                dictionary[word_list[num], word_list[num+1], times] = word_list[num+2]
                searching = False
    return dictionary

#This function will return a sentence by using the provided available starting words and dictionary.
def build_sentence(valid_s, dictionary):
    import random
    sentence = ['*', valid_s[random.randint(0,len(valid_s)-1)]]
    quit = False
    while not quit:
        running, num = True, 1
        while running:
            if not (sentence[len(sentence)-2], sentence[len(sentence)-1], num) in dictionary :
                current_word = dictionary[sentence[len(sentence)-2], sentence[len(sentence)-1], random.randint(0, num-1)]
                if current_word == '*':
                    quit = True
                sentence.append(current_word)
                running = False
            else:
                num += 1
    result = sentence[1][0].upper() + sentence[1][1:]
    for word in sentence[2:]:
        if word == '#':
            result += ','
        elif word == '*':
            result += '.' + ' '
        elif word == 'i':
            result += ' ' + 'I'
        else:
            result += ' ' + word
    return result

#This function will print the word out by each character at a time.
def slow_print(sentence):
    from time import sleep
    for letter in sentence:
        print(letter, end='', flush=True)
        sleep(0.05)

#main function
def main():
    import random
    #Preparing part
    ori_sen = load_file('synthtext-biblical-data.dat')
    word_lis = convert_list(ori_sen)
    word_lis = word_lis[:len(word_lis)-3]
    st = valid_start(word_lis)
    dic = build_dict(word_lis)
    #Infinity print
    while True:
        for times in range(random.randint(5,12)):
            sentence = build_sentence(st, dic)
            slow_print(sentence)
        print('換行')
        print('')

#Call main function
main()
