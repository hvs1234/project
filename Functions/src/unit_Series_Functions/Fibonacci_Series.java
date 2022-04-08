package unit_Series_Functions;
import java.util.Scanner;
public class Fibonacci_Series {
    static int fibo(int n)
    {
    	if(n==0) return 0;
    	else if(n==1) return 1;
    	else return fibo(n-2)+fibo(n-1);
    }
	public static void main(String[] args) {
         int n;
         System.out.println("Enter the last term of fibonacci series: ");
         Scanner s = new Scanner(System.in);
         n = s.nextInt();
         System.out.println("Fibonnaci Series is: ");
         for(int i=0;i<=n;i++)
         {
        	 System.out.print(fibo(i)+" ");
         }
	}
}
