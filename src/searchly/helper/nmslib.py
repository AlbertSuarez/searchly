import nmslib


class Nmslib:

    def __init__(self, metric='l2', method='hnsw'):
        self._metric = metric
        self._method = method
        self._index = None

    def fit(self, x):
        self._index = nmslib.init(space=self._metric, method=self._method)
        self._index.addDataPointBatch(x)
        self._index.createIndex(index_params={'efConstruction': 500}, print_progress=True)
        self._index.setQueryTimeParams(params={'efSearch': 500})

    def query(self, v, n):
        return self._index.knnQuery(v, k=n)

    def batch_query(self, x, n):
        return self._index.knnQueryBatch(x, k=n)

    def save(self, fn):
        self._index.saveIndex(fn)

    def load(self, fn):
        self._index = nmslib.init(space=self._metric, method=self._method)
        self._index.loadIndex(fn)
        self._index.setQueryTimeParams(params={'efSearch': 500})

    def __str__(self):
        return f'Nmslib(metric={self._metric}, method={self._method})'
