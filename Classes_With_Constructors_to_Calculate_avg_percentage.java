package unit_Learn_java;
import java.util.Scanner;
public class Learn_java_code {
    public static void main(String[] args)
    {
    	Scanner s = new Scanner(System.in);
    	String Name;
    	int age;
    	String section;
    	int percentage;
    	student[] arr;
    	int sum = 0;
    	for(int i=0;i<6;i++)
    	{
    		System.out.println("Enter the Name: ");
    		Name = s.next();
    		System.out.println("Enter the age: ");
    		age = s.nextInt();
    		System.out.println("Enter the Section: ");
    	    section = s.next();
    	    System.out.println("Enter the percentage: ");
    	    percentage = s.nextInt();
        	student obj = new student(Name,age,section,percentage);
    	    obj.display();
    	    sum+=percentage;
    	}
    	int avg = sum/6;
    	System.out.println("Average percentage is: "+avg);
    }
}

class student
{
	String Name;
	int age;
	String section;
	int percentage;
	student(String a, int b, String c, int d)
	{
		Name = a;
		age = b;
		section = c;
		percentage = d;
	}
	static int count = 0;
	void display()
	{
	    System.out.println("Name is: "+Name);
	    System.out.println("Name is: "+age);
	    System.out.println("Name is: "+section);
	    System.out.println("Name is: "+percentage);
	}
}
