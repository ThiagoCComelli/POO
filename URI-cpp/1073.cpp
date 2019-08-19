#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main()
{
    int n,val;
    cin >> n;
    for (int i = 2; i <= n; i += 2)
    {
        val = pow(i,2);
        cout << i << "^2 = " << val << endl;
    }
    
    return 0;
}