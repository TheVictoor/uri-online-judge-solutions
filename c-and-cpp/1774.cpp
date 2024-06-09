
#include <iostream>
#include <vector>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <algorithm>

using namespace std;

int main() {
    int r, c;
    cin >> r >> c;

    unordered_map<int, vector<pair<int, int>>> dag;

    for (int ci = 0; ci < c; ++ci) {
        int a, b, p;
        cin >> a >> b >> p;
        dag[a].emplace_back(b, p);
        dag[b].emplace_back(a, p);
    }

    unordered_set<int> visited;
    visited.insert(1);

    set<pair<int, int>> nexts;
    for (const auto& i : dag[1]) {
        nexts.insert(i);
    }

    int sum = 0;

    while (visited.size() != dag.size()) {
        auto next = *min_element(nexts.begin(), nexts.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.second < b.second;
        });

        nexts.erase(next);

        if (visited.count(next.first)) {
            continue;
        }

        for (const auto& i : dag[next.first]) {
            nexts.insert(i);
        }

        sum += next.second;
        visited.insert(next.first);
    }

    cout << sum << endl;

    return 0;
}
