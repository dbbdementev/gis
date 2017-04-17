import time
from gis import main


class test_time(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))


if __name__ == '__main__':
    with test_time() as p:
        main('testdata-small.csv', 'result.csv')
