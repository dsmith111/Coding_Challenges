#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
int main()
{
    int N;  
    cin >> N; cin.ignore();
    
    int y[N];
    int x,c;
   // cerr << y[N] << endl;
    
    for (int i = 0; i < N; i++) {
        int Pi;
        cin >> Pi; cin.ignore();
        y[i] = Pi;        
    }
sort (y ,y + N);

int e = y[N - 1];
    for (int i = 1; i < N; i++){
        x = y[i];
        c = y[i - 1];
        int d;
        d = abs(x - c);
        if (d < e){
            e = d;}
    }

    // Write an action using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;



    cout << e << endl;
}