import java.util.Scanner;
public class Learn_java_code {
    public static void main(String[] args)
    {
    	int a,b;
    	Scanner s = new Scanner(System.in);
    	System.out.println("Enter two numbers: ");
    	a = s.nextInt();
    	b = s.nextInt();
    	one obj1 = new one(a,b);
    	obj1.print1();
    	two obj2 = new two(a,b);
    	obj2.print2();
    	three obj3 = new three(a,b,2);
    	obj3.print3();
    }
}

class one
{
	int a,b;
	one(int x, int y)
	{
		a = x; b = y;
	}
	public void print1()
	{
		System.out.println(a+b);
	}
}

class two extends one
{
	int c,d;
	two(int x, int y)
	{
		super(x,y);
		c = x;
		d = y;
	}
	public void print2()
	{
		System.out.println(c*d);
	}
}

class three extends two
{
	int e,f;
	three(int p, int q, int r)
	{
		super(p,q);
		e = p*q;  f = r; 
	}
	public void print3()
	{
		System.out.println(e*f);
	}
}
