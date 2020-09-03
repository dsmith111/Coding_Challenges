using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

/**
 * Don't let the machines win. You are humanity's last hope...
 **/
class Player
{
    static void Main(string[] args)
    {
        int width = int.Parse(Console.ReadLine()); // the number of cells on the X axis
        int height = int.Parse(Console.ReadLine()); // the number of cells on the Y axis
        string[,] arrayMap = new string[height+1,width+1];
        for (int i = 0; i < height; i++)
        {
            string line = Console.ReadLine(); // width characters, each either 0 or .
            for(int j = 0; j<width;j++)
            {
                arrayMap[i,j] = ""+line[j];
            }
            //Console.Error.WriteLine(line);
        }
        
        for(int i =0;i<(height);i++)
        {
            for(int j = 0; j<width;j++)
            {
                switch(arrayMap[i,j])
                {
                    case "0":
                    
                 Console.WriteLine(j+" "+i+CheckMap(arrayMap,i,j,width,height));
                // Console.Error.WriteLine(j+" "+i+CheckMap(arrayMap,i,j,width,height));
                 break;
                    
                    default:
                    break;
                    
                }
            }
        }
        

        // Write an action using Console.WriteLine()
        // To debug: Console.Error.WriteLine("Debug messages...");


        // Three coordinates: a node, its right neighbor, its bottom neighbor
      //  Console.WriteLine("0 0 1 0 0 1");
    }
    
    //Function for checking coordinates
    static string CheckMap(string[,] array,int row, int col,int width,int height)
    {
        string neighborCoor ="";
        for(int i =1;i<=(width-col);i++){
        if(array[row,(col+i)] == "0" && ((width-col)-i) >= 1)
        {
            neighborCoor += " "+(col+i)+" "+row;
           // Console.Error.WriteLine(neighborCoor);
            break;
        }
        else if(((width-col)-i) < 1)
        {
            neighborCoor += " -1 -1";
        }
        }
        for(int i =1;i<=(height-row);i++){
        if(array[(row+i),(col)] == "0" && ((height-row)-i) >= 1)
        {
            neighborCoor += " "+(col)+" "+(row+i);
            break;
            //Console.Error.WriteLine(neighborCoor);
        }
        else if(((height-row)-i) < 1) 
        {
            neighborCoor += " -1 -1";
        }}
        //Console.Error.WriteLine(neighborCoor);
        return(neighborCoor);
    }
}