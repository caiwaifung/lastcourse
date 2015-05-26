Experiment Project: Indexing Images for Content Based Retrieval
=============

FORMATS:

- feature file
    N, M, following by N lines of M-dim features (floats)

- ans files
    #queries lines, while each line:
    C, following by several pairs of (i_k, d_k)
        C (int): number of node access
        i_k (int): index of k-th closest image
        d_k (float): distance of k-th closest image
