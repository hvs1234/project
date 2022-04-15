package unit_Strings;
public class Methods_Of_Strings {
	public static void main(String[] args) {
           String s1 = "Hello World In Java ...";
           String s2 = "Hello World In Java ...";
           System.out.println(s1==s2);
           String x1 = new String("Java ...");
           String x2 = new String("Java ...");
           System.out.println(x1==x2); 
           boolean a = s1.startsWith("H");
           boolean b = s2.endsWith("J");
           System.out.println(a);
           System.out.println(b);
           boolean c = s1.equals(s2);
           System.out.println(c);
           String d = s1.trim();
           System.out.println(d);
           boolean e = s1.contains("ld");
           System.out.println(e);
           String f = s1.toLowerCase();
           String g = s2.toUpperCase();
           System.out.println(f);
           System.out.println(g);
           int l = s1.length();  System.out.println(l);
           String h = s1.repeat(3);
           System.out.println(h+" ");
           char i = s2.charAt(4);  System.out.println(i);
           String j = x1.substring(5);  System.out.println(j);
           int k = s1.indexOf("a");
           System.out.println(k);
           int m = s2.lastIndexOf("a");
           System.out.println(m);
	}
}
