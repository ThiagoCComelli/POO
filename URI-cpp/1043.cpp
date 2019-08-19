#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main() 
{
    float a,b,c,tri,per;
    
    cin >> a >> b >> c;

    tri = (b-c);
    per = (a+b+c);

    cout << fixed << setprecision(1);

    if (tri < a && a < (b+c))
    {
        cout << "Perimetro = " << per << endl;
    }
    else
    {
        tri = ((a+b)*c)/2.0;
        cout << "Area = " << tri << endl;
    }
    
    return 0;
}