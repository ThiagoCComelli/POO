#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main()
{
    int distance;
    double gas, total;

    cin >> distance >> gas;

    total = distance/gas;

    cout << fixed << setprecision(3);
    cout << total << " km/l" << endl;

    return 0;
}