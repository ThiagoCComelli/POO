#include "Pescador.hpp"
#include <vector>

using namespace std;

int main(){
    vector<Pescador>lista;
    Pescador melhor("",0);
    Pescador pior("",0);

    Pescador bob("Bob",20);
    bob.pescou();

    Pescador ted("Ted",22);
    ted.pescou();
    ted.pescou();
    bob.pescou();

    Pescador tom("Tom",43);
    tom.pescou();
    ted.pescou();

    lista.push_back(bob);
    lista.push_back(ted);
    lista.push_back(tom);

    for(auto & value:lista){
        printf("Nome: %s\nIdade: %d\nPeixes: %d\n\n",value.getNome().c_str(),value.getIdade(),value.getPeixes());
        if (value.getPeixes() > melhor.getPeixes()){
            melhor = value;
        } if (pior.getNome() == "") {
            pior = value;
        } else {
            if(pior.getPeixes() > value.getPeixes()){
                pior = value;
            }
        }
    }

    printf("Melhor: %s\nPeixes: %d\n\n",melhor.getNome().c_str(),melhor.getPeixes());
    printf("Pior: %s\nPeixes: %d\n\n",pior.getNome().c_str(),pior.getPeixes());


    return 0;
}
