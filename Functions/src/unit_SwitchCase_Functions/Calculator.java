package unit_SwitchCase_Functions;

import java.util.Scanner;

public class Calculator {

	static int sum(int a, int b)
	{
		return a+b;
	}
	static int subtract(int a, int b)
	{
		return a-b;
	}
	static int multiply(int a, int b)
	{
		return a*b;
	}
	static int divide(int a, int b)
	{
		return a/b;
	}
	public static void main(String[] args)
	{
	    int x,y;
	    Scanner s = new Scanner(System.in);
	    System.out.println("Enter the first number: ");
	    x = s.nextInt();
	    System.out.println("Enter the second number: ");
	    y = s.nextInt();
	    String ch;
	    int c;
	    do
	    {
	    	System.out.println("Enter the choice from [+,-,*,/]: ");
		    ch = s.next();
	    	switch(ch)
		    {
		    case "+" -> System.out.println(sum(x,y));
		    case "-" -> System.out.println(subtract(x,y));
		    case "*" -> System.out.println(multiply(x,y));
		    case "/" -> System.out.println(divide(x,y));
		    default -> System.out.println("Invalid Choice ...");
		    }
	    	System.out.println("Do you want to continue: [1=yes , 0=no] ");
	    	c = s.nextInt();
	    	if(c==0) break;
	    } while(c!=0);
	}
}
