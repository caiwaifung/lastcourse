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
int split_num;

bool my_callback(void *obj, void *) {
    Feature *fea = (Feature *)obj;
    int id = fea->id;
    double d = cur_query.dis(*fea);
    cur_result.a.push_back(std::make_pair(d, id));
    if (cur_result.a.size() > (size_t)NUM_ANSWER * 2)
        return false;
    return true;
}

template<class TreeType> 
void query(TreeType &tree, const Feature &feature) {
    Real le = 0., ri = 10000; 
    for (int tmp = 0; tmp < 20; ++tmp) {
        Real radius = (le + ri) / 2.;
        if (tmp == 19) radius = ri;
        static Real lbound[FEATURE_DIM], rbound[FEATURE_DIM];
        for (int i = 0; i < FEATURE_DIM; ++i) {
            lbound[i] = feature.a[i] - radius;
            rbound[i] = feature.a[i] + radius;
        }
        cur_result.a.clear();
        rtree_stat.clear();
        tree.Search(lbound, rbound, my_callback, nullptr);
        if (cur_result.a.size() >= NUM_ANSWER * 2)
            ri = radius;
        else
            le = radius;
    }
    sort(cur_result.a.begin(), cur_result.a.end());
    if (cur_result.a.size() > NUM_ANSWER)
        cur_result.a.resize(NUM_ANSWER);
    cur_result.access_num = rtree_stat.access_num;
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

    //for (size_t i = 0; i < data.size(); ++i) {
        //memset(data[i].a, 0, sizeof(data[i].a));
        //data[i].a[0] = (Real)i;
    //}
    std::sort(data.begin(), data.end());

    printf("inserting data to tree..\n"); fflush(stdout);
    RTree<void*, Real, FEATURE_DIM> tree;
    rtree_stat.clear();
    for (auto &x: data) {
        //static int ind = 0;
        //printf("  -> inserting #%d..\n", ++ind); fflush(stdout);
        tree.Insert(x.a, x.a, &x);
    }
    split_num = rtree_stat.split_num;

    printf("answering queries..\n"); fflush(stdout);
    std::vector<Feature> queries = IO::load_data(f_queries);
    std::vector<Result> ans;
    for (auto &q: queries) {
        cur_query = q;
        query(tree, q);
        cur_result.split_num = split_num;
        ans.push_back(cur_result);
    }

    printf("saving results..\n"); fflush(stdout);
    IO::save_result(f_out, ans);
    return 0;
}
