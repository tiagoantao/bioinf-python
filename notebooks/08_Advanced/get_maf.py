from __future__ import print_function

import pickle
import sys


def gather_MAFs(chrom, start_pos):
    mafs = []
    try:
        f = open('tsi-%d-%d.frq' % (chrom, start_pos))
        f.readline()
        for cnt, l in enumerate(f):
            toks = [tok for tok in l.rstrip().split(' ') if tok != '']
            maf = float(toks[-2])
            mafs.append(maf)
        f.close()
    except:
        # might be empty if there are no SNPs
        pass
    w = open('MAF-%d-%d' % (chrom, start_pos), 'w')
    pickle.dump(mafs, w)
    w.close()

chrom = int(sys.argv[1])
start_pos = int(sys.argv[2])
gather_MAFs(chrom, start_pos)
