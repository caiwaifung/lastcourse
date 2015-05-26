#pragma once
#include <cmath>
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
        ans = sqrt(ans);
        return ans;
    }
};

typedef std::pair<double, int> PairDI;

struct Result {
    std::vector<PairDI> a;
    int access_num;
};

class IO {
public:
    static std::vector<Feature> load_data(std::string filename) {
        FILE *f = fopen(filename.c_str(), "r");
        if (f == nullptr)
            throw std::string("IO.load_data: cannot open file");
        std::vector<Feature> a;
        int n, m; 
        fscanf(f, "%d%d", &n, &m);
        assert(m == FEATURE_DIM);
        for (int i = 0; i < n; ++i) {
            Feature cur;
            cur.id = i;
            for (int j = 0; j < m; ++j) {
                fscanf(f, "%f", &cur.a[j]);
            }
            a.push_back(cur);
        }
        return a;
    }
    static void save_result(std::string filename, const std::vector<Result> &result) {
        FILE *f = fopen(filename.c_str(), "w");
        if (f == nullptr)
            throw std::string("IO.save_result: cannot open file");
        for (auto &r: result) {
            fprintf(f, "%d", r.access_num);
            for (auto &p: r.a)
                fprintf(f, " %d %.6f", p.second, p.first);
            fprintf(f, "\n");
        }
        fclose(f);
    }
    /*
    static void save(const std::vector<Feature> &feature, std::string filename) {
        assert(false);
    }
    */
};