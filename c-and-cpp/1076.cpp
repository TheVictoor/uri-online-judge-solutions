
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <string>

using namespace std;

int bfs(const string& parent, unordered_set<string>& visited, const string& current, const string& start, int total, unordered_map<string, unordered_set<string>>& dag) {
    visited.insert(current);
    if (current == start && visited.size() == total) {
        return 0;
    }

    int c = parent.empty() ? 0 : 2;
    for (const string& n : dag[current]) {
        if (n != parent) {
            c += bfs(current, visited, n, start, total, dag);
        }
    }

    return c;
}

int main() {
    int n_tests;
    cin >> n_tests;

    for (int test = 0; test < n_tests; ++test) {
        string start;
        cin >> start;
        int v, a;
        cin >> v >> a;

        unordered_map<string, unordered_set<string>> dag;

        for (int ia = 0; ia < a; ++ia) {
            string a, b;
            cin >> a >> b;
            dag[a].insert(b);
            dag[b].insert(a);
        }

        unordered_set<string> visited;
        int c = bfs("", visited, start, start, dag.size(), dag);

        cout << c << endl;
    }

    return 0;
}
