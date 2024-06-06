#include <iostream>
#include <cmath>
#include <iomanip>

int main() {
    int a, b, c;
    std::cin >> a >> b >> c;
    double p = (a + b + c) / 2.0;
    double area = std::sqrt(p * (p - a) * (p - b) * (p - c));
    std::cout << std::fixed << std::setprecision(3) << area << " m2" << std::endl;
    return 0;
}
