#include <iostream>
#include <iomanip>
#include <math.h>
#include <string>

using namespace std;

int main()
{
    int n;
    double a,b,c,out;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> a >> b >> c;
        out = (a*2+b*3+c*5)/10;
        cout << fixed << setprecision(1) << out << endl;
    }
    
    return 0;
}