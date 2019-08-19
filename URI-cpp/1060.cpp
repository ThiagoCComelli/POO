#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    double val; int tot = 0;
    for (int i = 0; i < 6; i++)
    {
        cin >> val;

        if (val > 0)
        {
            tot++;
        }
    }
    
    cout << tot << " valores positivos" << endl;

    return 0;
}