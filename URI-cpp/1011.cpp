#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main()
{
    int r;
    double pi = 3.14159,volume;

    cin >> r;

    volume = (4.0/3)*pi*pow(r,3);

    cout << "VOLUME = " << fixed << setprecision(3) << volume << endl;

    return 0;
}