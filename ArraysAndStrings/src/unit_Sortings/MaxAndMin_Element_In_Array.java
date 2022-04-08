package unit_Sortings;

import java.util.Scanner;

public class MaxAndMin_Element_In_Array {
	static void find(int[] arr, int n)
    {
    	int max = arr[0];
    	int min = arr[0];
    	for(int i=1;i<n;i++)
    	{
    		if(arr[i]>max)
    		{
    			max = arr[i];
    		}
    		if(arr[i]<min)
    		{
    			min = arr[i];
    		}
    	}
		System.out.println("Max and Min element in array is: "+max+" "+min);
    }
	public static void main(String[] args) {
		 int n;
		 Scanner s = new Scanner(System.in);
	     n = s.nextInt();
	     int[] arr = new int[100];
	     for(int i=0;i<n;i++)
	     {
	    	 arr[i] = s.nextInt();
	     }
	     find(arr,n);
	}
}
