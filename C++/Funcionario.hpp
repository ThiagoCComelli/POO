#include <string>

using namespace std;

class Funcionario{
private:
    int idade;
    string nome,cargo;
    double salario,vendas;
public:
    Funcionario(string _nome,int _idade,double _salario){
        nome = _nome;
        idade = _idade;
        salario = _salario;
    };

    void setCargo(string _cargo){
        cargo = _cargo;
    }
    void darAumento(double perc){
        salario *= perc/100;
    }
    void setVendas(int _vendas){
        vendas = _vendas;
    }
    double getSalarioBase(){
        return salario;
    }
    double getSalario(){
        return salario+calcComissao()-calcImposto();
    }
    double calcComissao(){
        return vendas*0.04;
    }
    string getNome(){
        return nome;
    }
    int getIdade(){
        return idade;
    }
    string getCargo(){
        return cargo;
    }
    double getVendas(){
        return vendas;
    }
    double calcImposto(){
        if(0 <= salario+calcComissao() && salario+calcComissao() <= 1000){
            return (salario+calcComissao()) * 0.05;
        } else if (1000 < salario+calcComissao() && salario+calcComissao() <= 5000){
            return (salario+calcComissao()) * 0.08;
        } else if (5000 < salario+calcComissao() && salario+calcComissao() <= 10000){
            return (salario+calcComissao()) * 0.12;
        } else if (salario+calcComissao() > 10000){
            return (salario+calcComissao()) * 0.20;}
        return 0;
    }

};
