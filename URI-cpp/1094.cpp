#include <iostream>
#include <iomanip>
#include <math.h>
#include <string>

using namespace std;

int main()
{
    int n,c=0,r=0,s=0,tot;
    int res;
    string name;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> tot >> name;
        res += tot;
        if (name == "C")
        {
            c += tot;
        }
        else if (name == "R")
        {
            r += tot;
        }
        else if (name == "S")
        {
            s += tot;
        }
    }
    res = c+r+s;
    cout << "Total: " << c+r+s << " cobaias" << endl;
    cout << "Total de coelhos: " << c << endl;
    cout << "Total de ratos: " << r << endl;
    cout << "Total de sapos: " << s << endl;
    cout << fixed << setprecision(2);
    cout << "Percentual de coelhos: " << (100.0*c)/res << " %" << endl;
    cout << "Percentual de ratos: " << (100.0*r)/res << " %" << endl;
    cout << "Percentual de sapos: " << (100.0*s)/res << " %" << endl;
    return 0;
}