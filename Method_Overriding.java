public class Learn_java_code {
    public static void main(String[] args)
    {
        A obj1 = new A();
        obj1.m1();
        B obj2 = new B();
        obj2.m1();
    }
}

class A
{
	int x = 13;
	public void m1()
	{
		x = this.x;
		System.out.println(x);
	}
}
class B extends A
{
	public void m1()
	{
		System.out.println("Method of class B ...");
	}
}


