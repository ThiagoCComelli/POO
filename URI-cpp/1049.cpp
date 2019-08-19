#include <iostream>
#include <iomanip>
#include <math.h>
#include <vector>
#include <bits/stdc++.h>
#include <cstring>

using namespace std;

int main() 
{
    string nome,nome1,nome2;

    cin >> nome >> nome1 >> nome2;

    if (nome == "vertebrado")
    {
        if (nome1 == "ave")
        {
            if (nome2 == "carnivoro")
            {
                cout << "aguia" << endl;
            }
            else if (nome2 == "onivoro")
            {
                cout << "pomba" << endl;
            }
        }
        else if (nome1 == "mamifero")
        {
            if (nome2 == "onivoro")
            {
                cout << "homem" << endl;
            }
            else if (nome2 == "herbivoro")
            {
                cout << "vaca" << endl;
            }
        } 
    }
    else if (nome == "invertebrado")
    {
        if (nome1 == "inseto")
        {
            if (nome2 == "hematofago")
            {
                cout << "pulga" << endl;
            }
            else if (nome2 == "herbivoro")
            {
                cout << "lagarta" << endl;
            }
        }
        else if (nome1 == "anelideo")
        {
            if (nome2 == "hematofago")
            {
                cout << "sanguessuga" << endl;
            }
            else if (nome2 == "onivoro")
            {
                cout << "minhoca" << endl;
            } 
        } 
    }
    return 0;
}