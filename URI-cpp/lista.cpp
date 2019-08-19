#include <iostream>
#include <iomanip>
#include <math.h>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main() 
{
    float a;
    vector<float> list;

    for (int i = 0; i < 3; i++)
    {
        cin >> a;
        list.push_back(a);
    }
    for (int i = 0; i < 3; i++)
    {
        cout << list[i] << endl;
    }

    sort(list.begin(),list.end(),greater<>());
    for (int i = 0; i < 3; i++)
    {
        cout << list[i] << endl;
    }
    
    return 0;
}