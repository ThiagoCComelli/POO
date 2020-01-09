#include <string>

using namespace std;

class Forno{
private:
   string marca;
   int tempmax, temp;
   bool status= 0;
public:
    Forno(string _marca,int _tempmax){
        marca = _marca;
        tempmax = _tempmax;
    }
    string getMarca(){
        return marca;
    }
    int getTempMax(){
        return tempmax;
    }
    int getTemp(){
        return temp;
    }
    bool getStatus() {
        return status;
    }
    void ligar(){
        status = 1;
        temp = 50;
    }
    void desligar(){
        status = 0;
        temp = 50;
    }
    bool mudarTemperatura(int graus){
        if (getStatus() == 1){
            if (tempmax == temp){
                return false;
            } else {
                if ((temp+graus) >= tempmax || (temp+graus) <= 50){
                    return false;
                } else {
                    temp += graus;
                    return true;
                }
            }
        } else {
            return false;
        }
    }
};
