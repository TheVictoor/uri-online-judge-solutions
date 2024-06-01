
#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

char getCurrent(vector<vector<char>>& grid, pair<int, int>& curr) {
    return grid[curr.first][curr.second];
}

int main() {
    int c, r;
    cin >> c >> r;

    vector<vector<char>> grid(r, vector<char>(c));
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            cin >> grid[i][j];
        }
    }

    unordered_map<string, bool> visited;
    string direction = "";
    pair<int, int> current = {0, 0};

    auto currentKey = [](pair<int, int>& p) {
        return to_string(p.first) + "," + to_string(p.second);
    };

    while (!visited[currentKey(current)] && getCurrent(grid, current) != '*') {
        visited[currentKey(current)] = true;
        char currCell = getCurrent(grid, current);
        if (currCell == '>' || currCell == '<' || currCell == 'v' || currCell == '^') {
            direction = currCell;
        }

        if (direction == ">") {
            if (current.second + 1 >= c) break;
            current.second++;
        } else if (direction == "<") {
            if (current.second - 1 < 0) break;
            current.second--;
        } else if (direction == "v") {
            if (current.first + 1 >= r) break;
            current.first++;
        } else if (direction == "^") {
            if (current.first - 1 < 0) break;
            current.first--;
        }
    }

    if (getCurrent(grid, current) != '*') {
        cout << "!" << endl;
    } else {
        cout << "*" << endl;
    }

    return 0;
}
