#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main()
{ 
    double value;
    
    cin >> value;

    if (value <= 25 && value >= 0)
    {
        cout << "Intervalo [0,25]" << endl;
    }
    else if (value > 25 && value <= 50)
    {
        cout << "Intervalo (25,50]" << endl;
    }
    else if (value > 50 && value <= 75)
    {
        cout << "Intervalo (50,75]" << endl;
    }
    else if (value > 75 && value <= 100)
    {
        cout << "Intervalo (75,100]" << endl;
    }
    else
    {
        cout << "Fora de intervalo" << endl;
    }
    return 0;
}