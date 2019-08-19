#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main()
{ 
    float a,b,c,d,average,grade,finalgrade;
    
    cin >> a >> b >> c >> d;
    cout << fixed << setprecision(1);

    average = (a*2+b*3+c*4+d*1)/10.0;
    if (average >= 7)
    {
        cout << "Media: " << average << endl;
        cout << "Aluno aprovado." << endl;
    }
    else if (average < 5)
    {
        cout << "Media: " << average << endl;
        cout << "Aluno reprovado." << endl;
    }
    else
    {
        cin >> finalgrade;
        
        cout << "Media: " << average << endl;
        cout << "Aluno em exame." << endl;
        cout << "Nota do exame: " << finalgrade << endl;

        if (((finalgrade+average)/2)>=5)
        {
            cout << "Aluno aprovado." << endl;
            cout << "Media final: " << (finalgrade+average)/2.0 << endl;
        }
        else
        {
            cout << "Aluno reprovado." << endl;
            cout << "Media final: " << (finalgrade+average)/2.0 << endl;
        }   
    }
    return 0;
}