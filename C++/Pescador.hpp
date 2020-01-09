#include <string>

using namespace std;

class Pescador{
private:
    string nome;
    int idade,peixes=0;
public:
    Pescador(string _nome,int _idade){
        nome = _nome;
        idade = _idade;
    }
    string getNome(){
        return nome;
    }
    int getIdade(){
        return idade;
    }
    int  getPeixes(){
        return peixes;
    }
    void pescou(){
        peixes++;
    }
};