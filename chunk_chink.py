import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

text=state_union.raw('2006- GWBush.txt')
custom_tnzr=PunktSentenceTokenizer(text)# this is synonimous to training the tokenizer using the corpus provided
tokenized=custom_tnzr.tokenize(text)

def process_content():

    try:
        for i in tokenized:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            print(tagged)
            #the angle bracket is to introduce parts of speech abbreviations
            chunkGram='''  Chunk:{<RB.?>*<VB.?>*<NNP><NN>?}'''# regex pattern to define the required parts of speech
            chunkParser=nltk.RegexpParser
            chunked=chunkParser.parse(tagged)
            print(chunked)
            chunked.draw()# visual representation

    except Exception as e:
        print(str(e))

process_content()
# chunking- Grouping things
#chinking- Removing some things from a chunk

#CHINKING

def process2_content():

    try:
        for i in tokenized:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            print(tagged)
            #the angle bracket is to introduce parts of speech abbreviations
            chunkGram='''  Chunk:{<.*>+}
                            }< VB.?|IN|DT>+ {  '''# chinking part, specify what you dont want
            # regex pattern to define the required parts of speech
            chunkParser=nltk.RegexpParser
            chunked=chunkParser.parse(tagged)
            print(chunked)
            chunked.draw()# visual representation

    except Exception as e:
        print(str(e))

process2_content()