#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main()
{ 
    int time,hours,minutes,seconds;

    cin >> time;

    hours = time/3600;
    time %= 3600;
    minutes = time/60;
    seconds = time%60;

    cout << hours << ":" << minutes << ":" << seconds << endl;

    return 0;
}