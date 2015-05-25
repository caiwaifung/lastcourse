#pragma once
#include <string>
#include <vector>
#include <cstdio>
#include <cassert>

struct Feature {
    float a[FEATURE_DIM];
    int id;
    double dis(const Feature &f) const {
        double ans = 0;
        for (int i = 0; i < FEATURE_DIM; ++i)
            ans += double(a[i] - f.a[i]) * double(a[i] - f.a[i]);
        return ans;
    }
};

class FeatureList {
public:
    static std::vector<Feature> load(std::string filename) {
        FILE *f = fopen(filename.c_str(), "r");
        if (f == nullptr)
            throw std::string("FeatureList.load: cannot open file");
        //printf("successfully opened file.\n"); fflush(stdout);
        std::vector<Feature> a;
        int n, m; 
        fscanf(f, "%d%d", &n, &m);
        //printf("n=%d m=%d\n", n, m); fflush(stdout);
        assert(m == FEATURE_DIM);
        for (int i = 0; i < n; ++i) {
            //printf("reading line %d/%d\n", i+1, n); fflush(stdout);
            Feature cur;
            cur.id = i;
            for (int j = 0; j < m; ++j) {
                fscanf(f, "%f", &cur.a[j]);
            }
            a.push_back(cur);
        }
        return a;
    }
    /*
    static void save(const std::vector<Feature> &feature, std::string filename) {
        assert(false);
    }
    */
};
