#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main()
{
    double a,b,c,pi = 3.14159,tri,cir,tra,qua,ret;

    cin >> a >> b >> c;

    tri = (a*c)/2;
    cir = pi*pow(c,2);
    tra = ((a+b)*c)/2;
    qua = pow(b,2);
    ret = a*b;

    cout << "TRIANGULO: " << fixed << setprecision(3) << tri << endl;
    cout << "CIRCULO: " << fixed << setprecision(3) << cir << endl;
    cout << "TRAPEZIO: " << fixed << setprecision(3) << tra << endl;
    cout << "QUADRADO: " << fixed << setprecision(3) << qua << endl;
    cout << "RETANGULO: " << fixed << setprecision(3) << ret << endl;

    return 0;
}