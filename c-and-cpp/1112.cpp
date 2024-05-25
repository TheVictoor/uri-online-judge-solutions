
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void updateBIT(vector<vector<int>> &bit, int x, int yy, int val, int X, int Y) {
  while (x <= X) {
    int y = yy;
    while (y <= Y) {
      bit[x][y] += val;
      y += (y & -y);
    }
    x += (x & -x);
  }
}

int getSum(vector<vector<int>> &bit, int x, int yy) {
  int sum = 0;
  while (x > 0) {
    int y = yy;
    while (y > 0) {
      sum += bit[x][y];
      y -= (y & -y);
    }
    x -= (x & -x);
  }
  return sum;
}

int answerQueries(int x1, int y1, int x2, int y2, vector<vector<int>> &bit) {
  int v1 = getSum(bit, x2, y2);
  int v2 = getSum(bit, x2, y1 - 1);
  int v3 = getSum(bit, x1 - 1, y2);
  int v4 = getSum(bit, x1 - 1, y1 - 1);

  return v1 - v2 - v3 + v4;
}

int main() {
  while (true) {
    int x, y, p, q;
    cin >> x >> y >> p;

    if (x == 0 && y == 0 && p == 0) {
      break;
    }

    cin >> q;

    vector<vector<int>> bit(x + 1, vector<int>(y + 1, 0));

    for (int i = 0; i < q; i++) {
      string a;
      cin >> a;

      if (a == "A") {
        int an, ax, ay;
        cin >> an >> ax >> ay;

        updateBIT(bit, ax + 1, ay + 1, an, x, y);
      } else if (a == "P") {

        int fx, fy, ux, uy;
        cin >> fx >> fy >> ux >> uy;

        int x1 = ux, x2 = fx;
        if (x2 < x1) {
          swap(x1, x2);
        }

        int y1 = uy, y2 = fy;
        if (y2 < y1) {
          swap(y1, y2);
        }

        int ans = answerQueries(x1 + 1, y1 + 1, x2 + 1, y2 + 1, bit);

        cout << ans * p << endl;
      }
    }
    cout << endl;
  }

  return 0;
}
