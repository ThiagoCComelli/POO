#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int n,val=0;
    cin >> n;
    do
    {
        if ((n%2)!=0)
        {
            cout << n << endl;
            val++;
        }
        n++;
    } while (val<6);
        
    return 0;
}