from __future__ import division, print_function
from pyspark import SparkContext

sc = SparkContext(appName='Processing PLINK frequencies')
plink_freqs = sc.wholeTextFiles('tsi-*-*.frq')

freqs = plink_freqs.mapValues(lambda content:
                              [float([tok for tok in l.split(' ')
                                      if tok != ''][-2])
                               for l in content.split('\n')[1:-1]])


first = freqs.first()
print(first)
flat = freqs.flatMapValues(lambda my_freqs: my_freqs)
def bla(e, acc):
    return (acc[0] + e[1],  acc[1] + 1)
my_sum, cnt = flat.fold((0.0, 0), bla)
#my_sum, cnt = flat.fold((0.0, 0), lambda e, acc: (acc[0] + e[1], acc[1] + 1))
print(my_sum, cnt, my_sum / cnt)
