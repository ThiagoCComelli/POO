#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int num, horas;
    double valor, salario;

    cin >> num >> horas >> valor;

    cout << "NUMBER = " << num << fixed << setprecision(2) << "\nSALARY = U$ " << horas*valor << endl;

    return 0;
}