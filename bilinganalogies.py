"""Find "solutions" to a-b+c in two languages (animal-frog+rana)
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

def mainloop(sourcefilename, targetfilename):
    maxwords = None
    swv = WordVectors(sourcefilename, maxwords)
    twv = WordVectors(targetfilename, maxwords)
    print 'Loaded'
    while True:
        sa = raw_input('Enter source word a (e.g. animal): ')
        sb = raw_input('Enter source word b (e.g. frog): ')
        tb = raw_input('Enter target word b (e.g. rana): ')
        winner = search(twv, [sa, sb, tb])
        if winner:
            print sa, '-', sb, '+', tb, '=', winner

if __name__=='__main__':
    mainloop(sys.argv[1], sys.argv[2])
