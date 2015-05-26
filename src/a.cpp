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

#include "RTree.h"
#include "comm.h"
#include <cstdlib>
#include <cstring>
#include <string>
#include <random>

Result cur_result;
Feature cur_query;

bool my_callback(void *obj, void *) {
    Feature *fea = (Feature *)obj;
    int id = fea->id;
    double d = cur_query.dis(*fea);
    cur_result.a.push_back(std::make_pair(d, id));
    return true;
}

template<class TreeType> 
void query(TreeType &tree, const Feature &feature) {
    static Real lbound[FEATURE_DIM], rbound[FEATURE_DIM];
    memmove(lbound, feature.a, sizeof(lbound));
    memmove(rbound, feature.a, sizeof(rbound));

    cur_result.a.clear();
    Real delta = 0.0001f; 
    for (; ; delta *= 1.5f) {
        RTreeNodeAccessNum = 0;
        tree.Search(lbound, rbound, my_callback, nullptr);
        if (cur_result.a.size() >= 5)
            break;
        cur_result.a.clear();
        for (int i = 0; i < FEATURE_DIM; ++i) {
            lbound[i] -= delta;
            rbound[i] += delta;
        }
    }
    sort(cur_result.a.begin(), cur_result.a.end());
    if (cur_result.a.size() > 5)
        cur_result.a.resize(5);
    cur_result.access_num = RTreeNodeAccessNum;
}

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
    RTree<void*, Real, FEATURE_DIM> tree;
    for (auto &x: data) {
        //static int ind = 0;
        //printf("  -> inserting #%d..\n", ++ind); fflush(stdout);
        tree.Insert(x.a, x.a, &x);
    }

    printf("answering queries..\n"); fflush(stdout);
    std::vector<Feature> queries = IO::load_data(f_queries);
    std::vector<Result> ans;
    for (auto &q: queries) {
        cur_query = q;
        query(tree, q);
        ans.push_back(cur_result);
    }

    printf("saving results..\n"); fflush(stdout);
    IO::save_result(f_out, ans);
    return 0;
}
