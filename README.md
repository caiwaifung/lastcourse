Experiment Project: Indexing Images for Content Based Retrieval
=============

FORMATS:

- feature file
    N, M, following by N lines of M-dim features (floats)

- ans files
    #queries blocks; each block 2 lines.
    first line: A, S
        A (int): number of node access
        S (int): number of node splitting during insertion
    second line: several pairs of (i_k, d_k)
        i_k (int): index of k-th closest image
        d_k (float): distance of k-th closest image
