#include <string>

using namespace std;

class Personagem{
private:
    int pos_x,pos_y,vidamax,vidaatual,velmax;
    string nome;
public:
    Personagem(string _nome,int _vidamax,int _velocidade,int _posx,int _posy){
        nome = _nome;
        vidaatual = _vidamax;
        vidamax = _vidamax;
        velmax = _velocidade;
        pos_x = _posx;
        pos_y = _posy;
    }
    int getPosX(){
        return pos_x;
    }
    int getPosY(){
        return pos_y;
    }
    int getVidaMax(){
        return vidamax;
    }
    int getVidaAtual(){
        return vidaatual;
    }
    int getVelMax(){
        return velmax;
    }
    string getNome(){
        return nome;
    }

    bool mover(char direcao,int velocidade){
        if (velocidade <= velmax && velocidade >= 0){
            if (direcao == 's'){
                pos_y -= velocidade;
                return true;
            } else if (direcao == 'n'){
                pos_y += velocidade;
                return true;
            } else if (direcao == 'l'){
                pos_x += velocidade;
                return true;
            } else if (direcao == 'o'){
                pos_x -= velocidade;
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    }
};