#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    double val, tot1 = 0; int tot = 0;
    for (int i = 0; i < 6; i++)
    {
        cin >> val;

        if (val > 0)
        {
            tot++;
            tot1 += val;
        }
    }
    
    cout << setprecision(1) << fixed;
    cout << tot << " valores positivos" << endl;
    cout << tot1/tot << endl;

    return 0;
}