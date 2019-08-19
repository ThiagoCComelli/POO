#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main()
{ 
    double gas,time,speed,averagegas = 12.0;

    cin >> time >> speed;

    gas = (time*speed)/averagegas;

    cout << fixed << setprecision(3);
    cout << gas << endl;

    return 0;
}