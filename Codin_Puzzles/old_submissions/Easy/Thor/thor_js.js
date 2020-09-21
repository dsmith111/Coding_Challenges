/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/

var inputs = readline().split(' ');
const lightX = parseInt(inputs[0]); // the X position of the light of power
const lightY = parseInt(inputs[1]); // the Y position of the light of power
const initialTX = parseInt(inputs[2]); // Thor's starting X position
const initialTY = parseInt(inputs[3]); // Thor's starting Y position
const thorStPos = [initialTX,initialTY];
var thorPos = thorStPos;
// game loop
while (true) {
    const remainingTurns = parseInt(readline()); // The remaining amount of turns Thor can move. Do not remove this line.

    // Write an action using console.log()
    // To debug: console.error('Debug messages...');


const lightPos = [lightX,lightY];
const stDist = [thorPos[0]-lightPos[0],thorPos[1]-lightPos[1]];
var dx,dy;
//Convert to binary, divide by absolute value
var unitPos = stDist.map(x=>x/Math.abs(x));
if(unitPos[0]>=1){
dx = "W";}
else if(unitPos[0]<=-1){
    dx = "E";}
    else{dx="";}
if(unitPos[1]>=1){
dy = "N";}
else if(unitPos[1]<=-1){
    dy = "S";}
else{dy="";}
thorPos[0] = thorPos[0] - unitPos[0];
thorPos[1] = thorPos[1] - unitPos[1];
var dir = dy+dx;
    // A single line providing the move to be made: N NE E SE S SW W or NW
    
    console.log(dir);
}