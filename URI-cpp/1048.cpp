#include <iostream>
#include <iomanip>
#include <math.h>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main() 
{
    float  sal,newsal,gain;
    int percent;

    cin >> sal;

    if (sal <= 400 && sal >= 0)
    {
        newsal = sal*1.15;
        gain = sal*.15;
        percent = 15;
    }
    else if (sal > 400 && sal <= 800)
    {
        newsal = sal*1.12;
        gain = sal*.12;
        percent = 12; 
    }
    else if (sal > 800 && sal <= 1200)
    {
        newsal = sal*1.10;
        gain = sal*.10;
        percent = 10; 
    }
    else if (sal > 1200 && sal <= 2000)
    {
        newsal = sal*1.07;
        gain = sal*.07;
        percent = 7; 
    }
    else if (sal > 2000)
    {
        newsal = sal*1.04;
        gain = sal*.04;
        percent = 4; 
    }

    cout << fixed << setprecision(2);
    cout << "Novo salario: " << newsal << endl;
    cout << "Reajuste ganho: " << gain << endl;
    cout << "Em percentual: " << percent << " %" << endl;
  
    return 0;
}