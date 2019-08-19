#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main()
{ 
    int sub, cem = 0, cinquenta = 0, vinte = 0, dez = 0, cinco = 0, dois = 0, um = 0, total;

    cin >> total;

    cout << total << endl;
    cout << total/100 << " nota(s) de R$ 100,00" << endl;
    sub = total%100;
    cout << sub/50 << " nota(s) de R$ 50,00" << endl;
    sub = sub%50;
    cout << sub/20 << " nota(s) de R$ 20,00" << endl;
    sub = sub%20;
    cout << sub/10 << " nota(s) de R$ 10,00" << endl;
    sub = sub%10;
    cout << sub/5 << " nota(s) de R$ 5,00" << endl;
    sub = sub%5;
    cout << sub/2 << " nota(s) de R$ 2,00" << endl;
    sub = sub%2;
    cout << sub/1 << " nota(s) de R$ 1,00" << endl;

    return 0;
}