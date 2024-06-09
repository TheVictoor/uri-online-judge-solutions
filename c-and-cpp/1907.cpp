#include <iostream>
#include <vector>
#include <queue>

using namespace std;

void paint_blank_sequence(vector<vector<char>>& image, int r, int c, pair<int, int> start) {
    int rows = image.size();
    int cols = image[0].size();
    queue<pair<int, int>> q;
    q.push(start);

    while (!q.empty()) {
        auto current = q.front();
        q.pop();
        int row = current.first;
        int col = current.second;

        if (image[row][col] == '.') {
            image[row][col] = 'o';

            if (col + 1 < cols && image[row][col + 1] == '.') {
                q.push({row, col + 1});
            }
            if (col - 1 >= 0 && image[row][col - 1] == '.') {
                q.push({row, col - 1});
            }
            if (row + 1 < rows && image[row + 1][col] == '.') {
                q.push({row + 1, col});
            }
            if (row - 1 >= 0 && image[row - 1][col] == '.') {
                q.push({row - 1, col});
            }
        }
    }
}

int main() {
    int r, c;
    cin >> r >> c;

    vector<vector<char>> image(r, vector<char>(c));
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            cin >> image[i][j];
        }
    }

    int paint_count = 0;

    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            if (image[i][j] == '.') {
                paint_blank_sequence(image, r, c, {i, j});
                ++paint_count;
            }
        }
    }

    cout << paint_count << endl;

    return 0;
}
