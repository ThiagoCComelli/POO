#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int x,y,tot=0;
    cin >> x >> y;
    if (x>y)
    {
        for (++y; y < x; y++)
        {
            if (y%2!=0)
            {
                tot += y;
            }
        }
    }
    else if (x<y)
    {
        for (++x; x < y; x++)
        {
            if (x%2!=0)
            {
                tot += x;
            }
        }
    }
    
    cout << tot << endl;

    return 0;
}