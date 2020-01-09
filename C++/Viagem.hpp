#include <string>

using namespace std;

class Viagem {
private:
    string destino,data;
    float passagem,seguro,estadia,tot,ind;
    int viajantes;
    bool febre;
public:
    Viagem(string x, string y){
        destino = x;
        data = y;
    }
    string getDestino(){
        return destino;
    }
    string getData(){
        return data;
    }
    float getPassagem(){
        return passagem;
    }
    float getSeguro(){
        return seguro;
    }
    float getEstadia(){
        return estadia;
    }
    int getViajantes(){
        return viajantes;
    }
    bool getFebre(){
        return febre;
    }
    float getTotal(){
        tot = viajantes*(passagem+estadia+seguro);
        return tot;
    }
    float getInd(){
        ind = passagem+estadia+seguro;
        return ind;
    }

    void setPassagem(float x){
        passagem = x;
    }
    void setSeguro(float x){
        seguro = x;
    }
    void setEstadia(float x){
        estadia = x;
    }
    void setViajantes(int x){
        viajantes = x;
    }
    void setFebre(bool x){
        febre = x;
    }

};