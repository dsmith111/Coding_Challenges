#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/
int main()
{
    int lightX; // the X position of the light of power
    int lightY; // the Y position of the light of power
    int initialTX; // Thor's starting X position
    int initialTY; // Thor's starting Y position
    cin >> lightX >> lightY >> initialTX >> initialTY; cin.ignore();
    
    int lx = lightX;
    int ly = lightY;
    int tx = initialTX;
    int ty = initialTY;
    
    // game loop
    while (1) {
        int remainingTurns; // The remaining amount of turns Thor can move. Do not remove this line.
        cin >> remainingTurns; cin.ignore();

        // Write an action using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;
if ((tx == lx) || (ty == ly)) // Determining if an angled path should be taken, or not
{
if (tx < lx)
{
    cout << "E" << endl;
    tx=tx+1;
}
else if (tx > lx)
{
    cout << "W" << endl;
    tx=tx-1;
}

if (ty < ly)
{
    cout << "S" << endl;
    ty=ty+1;
}
else if (ty > ly)
{
    cout << "N" << endl;
    ty=ty-1;
}
}
else
{
   if  ((tx > lx) && (ty > ly))
   {
        cout << "NW" << endl;
        tx=tx-1;
        
        
        
        ty=ty-1;
        
        
   }
   else if ((tx > lx) && (ty < ly))
   {
       ty=ty+1;
        tx=tx-1;
     cout << "SW" << endl;   
   }
    else if ((tx < lx) && (ty > ly))
   {
       cout << "NE" << endl;
        tx=tx+1;
       ty=ty-1;
       
   }
    else if ((tx < lx) && (ty < ly))
   {
       cout << "SE" << endl;
       ty=ty+1;
       tx=tx+1;
   }
}

    }
}