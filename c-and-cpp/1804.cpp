#include <iostream>
#include <vector>

using namespace std;

void update_bit(vector<int> &bit, int idx, int delta) {
  while (idx < bit.size()) {
    bit[idx] += delta;
    idx += idx & (-idx);
  }
}

int get_sum_bit(const vector<int> &bit, int i) {
  int s = 0;
  while (i > 0) {
    s += bit[i];
    i -= i & (-i);
  }
  return s;
}

int main() {
  int buggies;
  cin >> buggies;

  vector<int> list_buggies(buggies, 0);
  for (int i = 0; i < buggies; ++i) {
    cin >> list_buggies[i];
  }

  vector<int> bit(buggies + 1, 0);
  for (int idx = 0; idx < buggies; ++idx) {
    update_bit(bit, idx + 1, list_buggies[idx]);
  }

  string line;
  char a;
  int idx;

  while (scanf("%c %d", &a, &idx) != EOF) {
    if (a == '?') {
      int s = get_sum_bit(bit, idx - 1);
      cout << s << endl;
    } else if (a == 'a') {
      int p = list_buggies[idx - 1];
      update_bit(bit, idx, -p);
    }
  }

  return 0;
}
