#include "Forno.hpp"
#include <vector>

int main(){
    vector<Forno>lista;

    Forno tabajara("Tabajara",100);
    Forno orange("Orange",350);

    tabajara.ligar();
    printf("%d\n",tabajara.getTemp());
    tabajara.mudarTemperatura(25);
    printf("%d\n",tabajara.getTemp());
    tabajara.mudarTemperatura(30);
    printf("%d\n",tabajara.getTemp());
    tabajara.mudarTemperatura(-15);
    printf("%d\n",tabajara.getTemp());
    tabajara.mudarTemperatura(-75);

    orange.ligar();
    printf("%d\n",orange.getTemp());
    orange.mudarTemperatura(300);
    printf("%d\n",orange.getTemp());
    orange.mudarTemperatura(-20);
    printf("%d\n",orange.getTemp());
    orange.mudarTemperatura(30);
    printf("%d\n",orange.getTemp());
    printf("%d\n",orange.getStatus());
    printf("%d\n",tabajara.getStatus());

    tabajara.desligar();
    orange.desligar();

    printf("%d\n",orange.getStatus());
    printf("%d\n",tabajara.getStatus());

    lista.push_back(tabajara);
    lista.push_back(orange);

    for (auto & value:lista){
        printf("Marca: %s\nTemperatura: %d\n",value.getMarca().c_str(),value.getTemp());
    }






    return 0;
}