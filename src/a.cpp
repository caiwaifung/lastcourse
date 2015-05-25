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

int found;
int hit_id;

struct Result {
    int id;
    float delta;
    int found;
};

bool my_callback(void *obj, void *) {
    hit_id = ((Feature *)obj)->id;
    ++found;
    //printf("Hit data rect %d\n", ((Feature *)obj)->id);
    return true;
}

template<class TreeType> 
Result query(TreeType &tree, const Feature &feature) {
    static float lbound[FEATURE_DIM], rbound[FEATURE_DIM];
    memmove(lbound, feature.a, sizeof(lbound));
    memmove(rbound, feature.a, sizeof(rbound));

    found = 0;
    float delta = 0.0001f; 
    for (; ; delta *= 1.5f) {
        tree.Search(lbound, rbound, my_callback, nullptr);
        if (found > 0)
            break;
        for (int i = 0; i < FEATURE_DIM; ++i) {
            lbound[i] -= delta;
            rbound[i] += delta;
        }
    }
    Result ret;
    ret.id = hit_id;
    ret.delta = delta;
    ret.found = found;
    return ret;
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
    std::vector<Feature> data = FeatureList::load(f_data);

    printf("inserting data to tree..\n"); fflush(stdout);
    RTree<void*, float, FEATURE_DIM> tree;
    for (auto &x: data) {
        tree.Insert(x.a, x.a, &x);
    }

    printf("answering queries..\n"); fflush(stdout);
    std::vector<Feature> queries = FeatureList::load(f_queries);
    std::vector<Result> ans;
    for (auto &q: queries) {
        int i = 0; double d = 1e50;
        for (auto &x: data) {
            double tmp = q.dis(x);
            if (tmp < d) {
                d = tmp;
                i = x.id;
            }
        }
        Result r;
        r.delta = (float)d; r.found = 0;
        r.id = i;
        ans.push_back(r);
        /*
        auto cur = query(tree, q);
        ans.push_back(cur);
        */
    }

    printf("saving results..\n"); fflush(stdout);
    FILE *f = fopen(f_out.c_str(), "w");
    for (auto &x: ans) {
        fprintf(f, "%d %.4f \t%d\n", x.id, x.delta, x.found);
    }
    fclose(f);
    return 0;
}
