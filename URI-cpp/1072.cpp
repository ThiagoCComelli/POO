#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int n,in=0,out=0,tot;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> tot;
        if (tot >= 10 && tot <= 20)
        {
            in++;
        }
        else
        {
            out++;
        }
    }
    cout << in << " in" << endl;
    cout << out << " out" << endl;
    
    return 0;
}