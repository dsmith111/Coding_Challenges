/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

const n = parseInt(readline()); // the number of temperatures to analyse
var inputs = readline().split(' ');
var y =[];
for (let i = 0; i < n; i++) {
    const t = (parseInt(inputs[i])); // a temperature expressed as an integer ranging from -273 to 5526
    y[i] =t
}
//Collect & Sort Data Into an Array
y[n]=0;
var TempArray = y.sort(compare);
var result = 0;
//Eliminate Similar Numbers

//Eliminate all Elements Not within 1 range of zero
var pos = TempArray.indexOf(0);
//Compare Two Remaining Elements
//For Pos and Neg Values
if(!((isNaN(TempArray[pos-1])||isNaN(TempArray[pos+1])))  ){
  if( Math.abs(TempArray[pos-1])<Math.abs(TempArray[pos+1]))
  {
   result = TempArray[pos-1];}
   else if( Math.abs(TempArray[pos+1])<Math.abs(TempArray[pos-1]))
   {
  result = TempArray[pos+1];
}

  else{
      result = TempArray[pos+1];
  }
}
else if((isNaN(TempArray[pos-1])) && !(isNaN(TempArray[pos+1]))){
    result = TempArray[pos+1];
}
else if((isNaN(TempArray[pos+1])) && !(isNaN(TempArray[pos-1]))){
    result = TempArray[pos-1];
}
else { result = 0;}
// Write an action using console.log()
// To debug: console.error('Debug messages...');

function compare(a,b) {
    return a - b;
}

console.log(result);
