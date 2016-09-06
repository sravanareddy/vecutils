"""Find nearest (most similar) word
"""
from scipy.spatial.distance import cdist
import numpy
import sys
from load_vectors import WordVectors

def search(wv, word):
    if word not in wv.labidxmap:
        print word, 'not in vocabulary'

    cd = cdist(wv.vecs[wv.labidxmap[word]][numpy.newaxis, :], wv.vecs, 'cosine')

    winner = [None, 2]
    for i, d in enumerate(cd[0]):
        if i==wv.labidxmap[word]:
            continue
        if d < winner[1]:
            winner = [wv.labels[i], d]
    return winner[0]

def mainloop(filename):
    maxwords = 100000
    wv = WordVectors(filename, maxwords)
    print 'Loaded'
    while True:
        word = raw_input('Enter word: ')
        winner = search(wv, word)
        if winner:
            print winner

if __name__=='__main__':
    mainloop(sys.argv[1])
