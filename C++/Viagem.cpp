#include <stdio.h>
#include <vector>
#include "Viagem.hpp"

using namespace std;

int main(){
    vector<Viagem>lista;
    float minTot = 0;
    float minInd = 0;

    Viagem roma("Roma","10/03/2019 - 12/05/2019");
    roma.setViajantes(3);
    roma.setFebre(false);
    roma.setPassagem(2000);
    roma.setEstadia(1000);
    roma.setSeguro(120);

    Viagem istanbul("Istanbul","14/06/2019 - 12/07/2019");
    istanbul.setViajantes(2);
    istanbul.setFebre(true);
    istanbul.setPassagem(2500);
    istanbul.setEstadia(1200);
    istanbul.setSeguro(150);

    lista.push_back(roma);
    lista.push_back(istanbul);

    for (int i = 0; i < lista.size(); ++i) {
        printf("Destino: %s\nData: %s\nVacina: %d\nPassagens: %.2f\nEstadia: %.2f\nSeguro: %.2f\nViajantes: %d\nTotal: %.2f\n\n",
                lista[i].getDestino().c_str(),lista[i].getData().c_str(),lista[i].getFebre(),lista[i].getPassagem(),lista[i].getEstadia(),lista[i].getSeguro(),lista[i].getViajantes(),lista[i].getTotal());
    }
    Viagem a("","");
    Viagem b("","");
    for (int i = 0; i < lista.size(); ++i) {
        if(i==0){
            minTot = lista[i].getTotal();
            minInd = lista[i].getInd();
            a = b = lista[i];
        } else {
            if (lista[i].getTotal() < minTot) {
                minTot = lista[i].getTotal();
                a = lista[i];
            }
            if(lista[i].getInd() < minInd){
                minInd = lista[i].getInd();
                b = lista[i];
            }
        }
    }
    printf("Viagem mais barata no total: %s\n",a.getDestino().c_str());
    printf("Viagem mais barata no individual: %s\n",b.getDestino().c_str());

    return 0;
}
