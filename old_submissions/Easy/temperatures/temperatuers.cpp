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
    int n; // the number of temperatures to analyse
    cin >> n; cin.ignore();
if (n > 1){
    int y[n];
    for (int i = 0; i < n; i++) {
        int t; // a temperature expressed as an integer ranging from -273 to 5526
        cin >> t; cin.ignore(); 
        y[i] = t;
    }
    sort (y,y + n);
    int x,z; 
    
    x = y[0];
    z = y[0];
    
    for (int i = 0; i < n; i++){
 
        if (abs(y[i]) < abs(x)){
                x = y[i];}
        else if (abs(y[i]) == abs(x)){
             z = y[i];}
    }
    if (abs(x) == abs(z)){
        if(x > z){
            cout << x <<endl;}
        else if (z > x){
            cout << z << endl;}
        else 
            {cout << z << endl;}
    }
    else if (abs(x) < abs(z)){
        cout << x << endl;}
    else if (abs(z) < abs(x)){
        cout << z << endl;}
       
            
     cerr << "x= " << x <<endl;
        cerr << "z= "<<z<<endl;
}
else if ( n == 1){
    int t;
    cin >> t; cin.ignore();
    cout << t << endl;}
else{
    cout << 0 << endl;}
       
    // Write an action using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    
}