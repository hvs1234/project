package unit_Sortings;
import java.util.Scanner;
public class BubbleSort {
    static void bubblesort(int[] arr, int n)
    {
    	int i,j,temp;
    	for(i=0;i<n;i++)
    	{
    		for(j=0;j<n-i-1;j++)
    		{
    			if(arr[j]>arr[j+1])
    			{
    				temp = arr[j];
    				arr[j] = arr[j+1];
    				arr[j+1] = temp;
    			}
    		}
    	}
    }
    static void print(int[] arr, int n)
    {
    	int i;
    	for(i=0;i<n;i++)
    	{
    		System.out.print(arr[i]+" ");
    	}
    }
	public static void main(String[] args) {
       int n;
       Scanner s = new Scanner(System.in);
       n = s.nextInt();
       int[] arr = new int[n];
       int i;
       for(i=0;i<n;i++)
       {
    	   arr[i] = s.nextInt();
       }
       print(arr,n);
       bubblesort(arr,n);
       System.out.println();
       print(arr,n);
	}
}
