package unit_Series_Functions;
import java.util.Scanner;
public class Sum_Of_Series_01 {
    static void series01(int n)
    {
    	int i,sum=0;
    	System.out.println("Series is: ");
    	for(i=1;i<=n;i++)
    	{
    		sum+=i;
    		System.out.print("+"+i);
    	}
    	System.out.println("\nSum of Series is: "+sum);
    }
	public static void main(String[] args) {
        int n;
        System.out.println("Enter the last term of series: ");
        Scanner s = new Scanner(System.in);
        n = s.nextInt();
        series01(n);
	}
}
