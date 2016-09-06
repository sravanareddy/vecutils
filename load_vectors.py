import pandas

class WordVectors:
    def __init__(self, filename, maxrows=None):
        """
        filename should be a file with 1 vector per line, represented as label dim1 dim2...
        """
        self.maxrows = maxrows
        data = pandas.read_csv(filename, sep=' ', nrows=maxrows, header=None)
        self.labels = list(data.iloc[:, 0])
        self.labidxmap = dict([(w, i) for (i, w) in enumerate(self.labels)])
        self.vecs = data.iloc[:, 1:].as_matrix()
