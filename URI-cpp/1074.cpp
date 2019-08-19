#include <iostream>
#include <iomanip>
#include <math.h>
#include <string>

using namespace std;

int main()
{
    int n,val;
    string name;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> val;
        if (val==0)
        {
            name += "NULL";
        }
        else if (val%2==0)
        {
            name += "EVEN ";
        }
        else if (val%2!=0)
        {
            name += "ODD ";
        }
        if (val>0)
        {
            name += "POSITIVE";
        }
        else if (val<0)
        {
            name += "NEGATIVE";
        }
        cout << name << endl;
        name = "";
    }

    return 0;
}