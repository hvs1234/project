package unit_arraysAndstrings;
import java.util.Scanner;
public class SelectionSort {
	static void print(int[] arr, int n)
    {
    	int i;
    	for(i=0;i<n;i++)
    	{
    		System.out.print(arr[i]+" ");
    	}
    }
	static void selectionsort(int[] arr, int n)
	{
		int min,i,j,temp;
		for(i=0;i<=n-1;i++)
		{
			min = i;
			for(j=0;j<n;j++)
			{
				if(arr[j]>arr[min])
				{
					min = j;
				}
			}
			temp = arr[i];
			arr[i] = arr[min];
			arr[min] = temp;
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
	       selectionsort(arr,n);
	       System.out.println();
	       print(arr,n);
	}  
}
