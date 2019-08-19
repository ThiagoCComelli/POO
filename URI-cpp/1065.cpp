#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int val = 0,n;

    for (int i = 0; i < 5; i++)
    {
        cin >> n;

        if ((n%2)==0)
        {
            val++;
        }
    }
    
    cout << val << " valores pares" << endl;

    return 0;
}