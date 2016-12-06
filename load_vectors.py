import pandas
import numpy

class WordVectors:
    def __init__(self, filename, maxrows=None):
        """
        filename should be a file with 1 vector per line, represented as label dim1 dim2...
        """
        data = pandas.read_csv(filename, sep=' ', nrows=maxrows, header=None)
        self.labels = map(str, list(data.iloc[:, 0]))
        self.labidxmap = dict([(w, i) for (i, w) in enumerate(self.labels)])
        self.vecs = data.iloc[:, 1:].as_matrix()

    def merge(self, other, this_suffix, other_suffix):
        """merge in another word vector space, transforming labels with suffixes"""
        oldsize = len(self.labels)

        self.labels = [label+this_suffix for label in self.labels]
        self.labels.extend([label+other_suffix for label in other.labels])

        self.labidxmap = {w+this_suffix: i for w, i in self.labidxmap.items()}
        self.labidxmap.update({w+other_suffix: i+oldsize for w, i in other.labidxmap.items()})

        self.vecs = numpy.vstack((self.vecs, other.vecs))
