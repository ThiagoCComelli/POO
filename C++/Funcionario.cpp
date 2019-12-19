#include "Funcionario.hpp"
#include <vector>
#include <string>

using namespace std;

int main(){
    vector<Funcionario>lista;

    Funcionario bob("Bob",23,3900);
    Funcionario tom("Tom",27,1200);
    Funcionario tonim("Tonim",27,10000);

    bob.setCargo("vendedor");
    tom.setCargo("vendedor");
    tonim.setCargo("gerente");

    bob.setVendas(1000);
    tom.setVendas(5000);
    tonim.setVendas(1500);

    bob.darAumento(10);
    tom.darAumento(5);

    lista.push_back(bob);
    lista.push_back(tom);
    lista.push_back(tonim);

    for(auto & value:lista){
        printf("Nome: %s\nIdade: %d\nCargo: %s\nVendas: %.2f\nSalario base: %.2f\nComissao: %.2f\nImposto: %.2f\nSalario final: %.2f\n\n",
                value.getNome().c_str(),value.getIdade(),value.getCargo().c_str(),value.getVendas(),value.getSalarioBase(),value.calcComissao(),value.calcImposto(),value.getSalario());
    }
    return 0;
};
