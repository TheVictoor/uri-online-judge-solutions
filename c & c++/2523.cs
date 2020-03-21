using System;

class Program
{
    static void Main()
    {
       string abc;
       int n;
       string[] w;
       string nn;
       
       
        while(true){
            try{
               abc = Console.ReadLine();
               n = Convert.ToInt32(Console.ReadLine());
               nn = Console.ReadLine();
               w = nn.Split();
               
               for(int i = 0; i < n; i++ ){
                   Console.Write(abc[Convert.ToInt32(w[i]) - 1]);
               }
               
               Console.WriteLine("");
            }catch{
                break;
            }
        }
    }
}
