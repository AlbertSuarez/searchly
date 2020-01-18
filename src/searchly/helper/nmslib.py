import nmslib


class Nmslib:
    """
    Custom class for an NMSLIB index with custom functions for interacting with the index.
    """

    def __init__(self, metric='l2', method='hnsw'):
        """
        Initialize the NMSLIB index.
        :param metric: Metric.
        :param method: Method.
        """
        self._metric = metric
        self._method = method
        self._index = None

    def fit(self, x):
        """
        Insert feature vector to the class index.
        :param x: Numpy array with the feature vectors.
        :return: Feature vectors fitted into the index.
        """
        self._index = nmslib.init(space=self._metric, method=self._method)
        self._index.addDataPointBatch(x)
        self._index.createIndex(index_params={'efConstruction': 500}, print_progress=True)
        self._index.setQueryTimeParams(params={'efSearch': 500})

    def query(self, v, n):
        """
        Query to the index given a single features vector.
        :param v: Features vector.
        :param n: Amount of nearest neighbours to return by the index.
        :return: Query results.
        """
        return self._index.knnQuery(v, k=n)

    def batch_query(self, x, n):
        """
        Query to the index given a an array of features vector.
        :param x: Array of features vector.
        :param n: Amount of nearest neighbours to return by the index.
        :return: Query results.
        """
        return self._index.knnQueryBatch(x, k=n)

    def save(self, fn):
        """
        Save the class index to a file given its path.
        :param fn: File path where to save the index.
        :return: Index saved.
        """
        self._index.saveIndex(fn)

    def load(self, fn):
        """
        Load an index to the class given a file path.
        :param fn: File path where to load the index.
        :return: Index loaded.
        """
        self._index = nmslib.init(space=self._metric, method=self._method)
        self._index.loadIndex(fn)
        self._index.setQueryTimeParams(params={'efSearch': 500})

    def __str__(self):
        """
        Format the NMSLIB index to string.
        :return: String formatted version of the index.
        """
        return f'Nmslib(metric={self._metric}, method={self._method})'
