#include <iostream>
#include <iomanip>
#include <math.h>
#include <string>

using namespace std;

int main()
{
    int n, maior = 0, pos = 0;
    for (int i = 0; i < 100; i++)
    {
        cin >> n;
        if (n > maior)
        {
            maior = n;
            pos = i;
        }
    }
    cout << maior << endl;
    cout << ++pos << endl;
    return 0;
}