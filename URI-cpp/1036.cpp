#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main()
{ 
    double a,b,c,x,x1,x2;

    cin >> a >> b >> c;

    x = pow(b,2)-(4*a*c);

    if (x>0)
    {
        if (a>0)
        {
            x = sqrt(x);
            x1 = (-b + x)/(2*a);
            x2 = (-b - x)/(2*a);
            
            cout << fixed << setprecision(5);
            cout << "R1 = " << x1 << endl;
            cout << "R2 = " << x2 << endl;
        }
        else
        {
            cout << "Impossivel calcular" << endl;
        }  
    }
    else if (x<0)
    {
        cout << "Impossivel calcular" << endl;
    }
    else
    {
        x1 = (-b + x)/(2*a);
        x2 = (-b - x)/(2*a);
        
        cout << fixed << setprecision(5);
        cout << "R1 = " << x1 << endl;
        cout << "R2 = " << x2 << endl;
    }
    
    return 0;
}