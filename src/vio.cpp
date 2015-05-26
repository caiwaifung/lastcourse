//
// Usage:
//     <me> data_file query_file out_file
// where:
//     <data_file>, <query_file> are feature files (see ../data/feature-*/*.feature)
//     <out_file> contain K lines (K: number of queries); each line:
//         visit_times i1 i2 .... ip,  i stands for a nearest neighbor
//
// Must define FEATURE_DIM before compiling
//

#ifndef FEATURE_DIM
#error
#define FEATURE_DIM 10
#endif

#include "comm.h"
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <string>
#include <random>
#include <vector>

int main(int argc, char *argv[]) {
    if (argc != 4) {
        fprintf(stderr, "Usage:\n  <me> data_file query_file out_file\n");
        exit(1);
    }
    std::string f_data(argv[1]);
    std::string f_queries(argv[2]);
    std::string f_out(argv[3]);

    printf("reading data..\n"); fflush(stdout);
    std::vector<Feature> data = IO::load_data(f_data);

    printf("inserting data to tree..\n"); fflush(stdout);

    printf("answering queries..\n"); fflush(stdout);
    std::vector<Feature> queries = IO::load_data(f_queries);
    std::vector<Result> ans;
    for (auto &q: queries) {
        std::vector<PairDI> c;
        for (auto &x: data) {
            double tmp = q.dis(x);
            c.push_back(std::make_pair(tmp, x.id));
        }
        std::sort(c.begin(), c.end());
        if (c.size() > NUM_ANSWER)
            c.resize(NUM_ANSWER);
        Result r;
        r.a = c;
        r.access_num = 0;
        ans.push_back(r);
    }

    printf("saving results..\n"); fflush(stdout);
    IO::save_result(f_out, ans);
    return 0;
}
