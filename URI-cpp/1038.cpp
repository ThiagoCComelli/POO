#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main()
{ 
    int code,amount;

    cin >> code >> amount;

    cout << fixed << setprecision(2);

    if (code == 1)
    {
        cout << "Total: R$ " << 4.0*amount << endl;
    }
    else if (code == 2)
    {
        cout << "Total: R$ " << 4.5*amount << endl;
    }
    else if (code == 3)
    {
        cout << "Total: R$ " << 5.0*amount << endl;
    }
    else if (code == 4)
    {
        cout << "Total: R$ " << 2.0*amount << endl;
    }
    else
    {
        cout << "Total: R$ " << 1.5*amount << endl;
    }
    return 0;
}