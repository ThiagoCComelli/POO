#include <iostream>
#include <iomanip>
#include <math.h>
#include <vector>
#include <bits/stdc++.h>
#include <cstring>

using namespace std;

int main() 
{
    float sal,tax,rem;
    
    cin >> sal;

    cout << fixed << setprecision(2);
    if (sal >= 0 && sal <= 2000)
    {
        cout << "Isento" << endl;
    }
    else if (sal > 2000 && sal <= 3000)
    {
        sal -= 2000;
        tax = sal*.08;
        cout << "R$ " << tax << endl;
    }
    else if (sal > 3000 && sal < 4500)
    {
        sal -= 3000;
        tax = (1000*.08)+(sal*.18);
        cout << "R$ " << tax << endl;
    }
    else
    {
        sal -= 4500;
        tax = (1000*.08)+(1500*.18)+(sal*.28);
        cout << "R$ " << tax << endl;
    }
    return 0;
}