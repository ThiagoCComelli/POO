#include <vector>
#include <string>

using namespace std;

class Computador{
private:
    double basic,tot = 0;
    bool windows=0,linux=0,neon=0;
public:
    Computador(int x){
        basic = x;
        tot += x;
    }
    double getBasic(){
        return basic;
    }
    double getTot(){
        return tot;
    }
    bool getWindows(){
        return windows;
    }
    bool getLinux(){
        return linux;
    }
    bool getNeon(){
        return neon;
    }
    void setWindows(){
        tot += 500;
        windows = true;
    }
    void setLinux(){
        tot += 2;
        linux = true;
    }
    void setNeon(){
        tot += 100;
        neon = true;
    }

    double calcularPreco(){
        return tot;
    }
    string componentes(){
        string comp = "| ";
        if (windows== true){
            comp += "Windows | ";
        } if (linux== true){
            comp += "Linux | ";
        } if (neon== true){
            comp += "Neon |";
        }
        return comp;
    }

};
