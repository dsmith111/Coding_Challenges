using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution
{
      enum alphabet{
        A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a
    }
    static void Main(string[] args)
    {
        int L = int.Parse(Console.ReadLine());
        int H = int.Parse(Console.ReadLine());
        string M = Console.ReadLine();
        string T="";
        bool isLetter = false;
        foreach(char letter in M)
        {
         string  rL = letter+"";
         rL = rL.ToUpper();
       //  Console.Error.WriteLine(rL);
      //  Console.Error.WriteLine(Enum.GetNames(typeof(alphabet)).Length);
          for(int i=0;i < Enum.GetNames(typeof(alphabet)).Length;i++)
          {
          if(rL == (((alphabet) i)+""))
          {
              isLetter= true;
              break;
          }}
         // Console.Error.WriteLine(isLetter);
        //  Console.Error.WriteLine(rL);
          if(isLetter == true)
          {
              T += rL;
              isLetter = false;
          }
          else if(isLetter != true)
          {
              T += "a";
          }//Console.Error.WriteLine(rL);
       // Console.Error.WriteLine(T);  
        }
        int N = T.Length;
        //Console.Error.WriteLine(T);
        string[,] ascii = new string[H,L*(Enum.GetNames(typeof(alphabet)).Length)];
        char[] line;
        string[] alNum = new string[Enum.GetNames(typeof(alphabet)).Length];
      
        //Console.Error.WriteLine(T+" "+H+" "+L); 
        
        for (int i = 0; i < H; i++)
        {
            
           string ROW = Console.ReadLine();
          // Console.Error.WriteLine(i);
          //  Console.Error.WriteLine(ROW);
            line = ROW.ToCharArray();
           
           
        
       
            for(int j=0;j<line.Length;j++)
            {
                ascii[i,j] = ""+line[j];
            }
            
        }
        for (int i=0;i<Enum.GetNames(typeof(alphabet)).Length;i++)
        {
            alNum[i]  = ((alphabet) i)+"";
        }
        for(int j=0;j<H;j++)
        {
          string rowRead ="";
          for(int i=0;i<N;i++){
        //Console.Error.WriteLine(N);
          //Double For Loop to Cycle through 2D Matrix
          for(int k=0;k<L ;k++){
               // Console.Error.WriteLine((Array.IndexOf(alNum,T[i].ToString())*4));
         rowRead += ascii[j,(Array.IndexOf(alNum,T[i].ToString())*L)+k] ;
       
          }//Console.WriteLine(rowRead);
          }
          
          Console.WriteLine(rowRead);
          
        }
       // Console.Error.WriteLine(H+" "+L);

        // Write an action using Console.WriteLine()
        // To debug: Console.Error.WriteLine("Debug messages...");

        //Console.WriteLine("### ");
        //Console.WriteLine("#   ");
        //Console.WriteLine("##  ");
        //Console.WriteLine("#   ");
        //Console.WriteLine("### ");
    }
}