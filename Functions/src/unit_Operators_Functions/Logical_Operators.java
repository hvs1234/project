package unit_Operators_Functions;

public class Logical_Operators {
    static void Logical_Operator()
    {
    	        //Boolean ...
    			boolean a = true;
    			boolean b = false;
    			if(a && b) System.out.println("Yes ...");
    			else System.out.println("No ...");
    			int c = 2, d = 5;
    			System.out.println(c>=d);
    			//Logical AND OR NOT ...
    			boolean x = true;  boolean y = true;
    			boolean z = false;  boolean w = false;
    			if(x && y) System.out.println("Yes ...");
    			else System.out.println("No ...");
    			if(x || y) System.out.println("Yes");
    			else System.out.println("No ...");
    			if(!y && !x) System.out.println("Not in there ...");
    }
	public static void main(String[] args) {
          Logical_Operator();
	}
}
