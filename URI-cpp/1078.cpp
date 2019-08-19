#include <iostream>
#include <iomanip>
#include <math.h>
#include <string>

using namespace std;

int main()
{
    int n,m;
    cin >> n;
    for (int i = 1; i < 11; i++)
    {
        m = n*i;
        cout << i << " x " << n << " = " << m << endl;
    }
    
    return 0;
}