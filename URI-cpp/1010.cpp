#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int a, b, d, e;
    double c, f, valor;

    cin >> a >> b >> c;
    cin >> d >> e >> f;

    valor = b*c+e*f;

    cout << "VALOR A PAGAR: R$ " << fixed << setprecision(2) << valor << endl;

    return 0;
}