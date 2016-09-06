"""Find "solutions" to a-b+c (king-man+woman = queen)
"""
from scipy.spatial.distance import cdist
import numpy
import sys
from load_vectors import WordVectors

def search(wv, threewords):
    for word in threewords:
        if word not in wv.labidxmap:
            print word, 'not in vocabulary'
            return

    threewords_ids = [wv.labidxmap[word] for word in threewords]
    target = wv.vecs[threewords_ids[0]] - wv.vecs[threewords_ids[1]] + wv.vecs[threewords_ids[2]]
    cd = cdist(target[numpy.newaxis, :], wv.vecs, 'cosine')

    winner = [None, 2]
    for i, d in enumerate(cd[0]):
        if i in threewords_ids:
            continue
        if d < winner[1]:
            winner = [wv.labels[i], d]
    return winner[0]

def mainloop(filename):
    maxwords = 100000
    wv = WordVectors(filename, maxwords)
    print 'Loaded'
    while True:
        a = raw_input('Enter word a (e.g. king): ')
        b = raw_input('Enter word b (e.g. man): ')
        c = raw_input('Enter word c (e.g. woman): ')
        winner = search(wv, [a, b, c])
        if winner:
            print a, '-', b, '+', c, '=', winner

if __name__=='__main__':
    mainloop(sys.argv[1])
