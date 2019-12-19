#include "ZakGalou.hpp"
#include <vector>

using namespace std;

bool colide(Personagem a, Personagem b){
    if ((a.getPosX() == b.getPosX()) && (a.getPosY() == b.getPosY())){
        return true;
    } else {
        return false;
    }
}

int distancia(Personagem a, Personagem b){
    return abs(a.getPosX() - b.getPosX()) + abs(a.getPosY() - b.getPosY());
}

int main(){
    vector<Personagem>lista;

    Personagem zak("Zak",125,10,2,27);
    Personagem galou("Galou",100,7,29,6);
    Personagem tonim("Tonim",155,4,20,8);

    zak.mover('l',7);
    zak.mover('l',10);
    zak.mover('l',10);
    zak.mover('s',5);
    zak.mover('n',20);

    galou.mover('n',2);
    galou.mover('n',0);
    galou.mover('n',7);
    galou.mover('n',7);

    tonim.mover('o',3);

    lista.push_back(zak);
    lista.push_back(galou);
    lista.push_back(tonim);

    for (auto & value:lista){
        printf("Nome: %s\nVelocidade Maxima: %d\nVida: %d\nVida Maxima: %d\nPosicao: %d %d\n\n",
                value.getNome().c_str(),value.getVelMax(),value.getVidaAtual(),value.getVidaMax(),value.getPosX(),value.getPosY());
    }

    printf("Colidem[%s e %s]: %s\n\n",zak.getNome().c_str(),tonim.getNome().c_str(),colide(zak,tonim) ? "true":"false");
    printf("Distancia entre %s e %s: %d\n",tonim.getNome().c_str(),galou.getNome().c_str(),distancia(tonim,galou));
    printf("Distancia entre %s e %s: %d\n",zak.getNome().c_str(),tonim.getNome().c_str(),distancia(zak,tonim));

}