#include "Computador.hpp"
#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

int main(){
    vector<Computador>lista;

    Computador pc0(2000);
    pc0.setNeon();
    pc0.setWindows();

    Computador pc1(2500);
    pc1.setLinux();

    Computador pc2(1500);

    lista.push_back(pc0);
    lista.push_back(pc1);
    lista.push_back(pc2);

    for(auto & value:lista){
        printf("%.2f %s\n",value.getTot(),value.componentes().c_str());
    }
}

