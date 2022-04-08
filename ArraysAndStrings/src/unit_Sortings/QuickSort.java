package unit_Sortings;

import java.util.Scanner;

public class QuickSort {

	static void print(int[] arr, int n)
    {
    	int i;
    	for(i=0;i<n;i++)
    	{
    		System.out.print(arr[i]+" ");
    	}
    }
	static int partition(int[] arr, int low, int high)
	{
		int pivot = arr[low];  int temp;
		int i = low+1;  int j = high;
		do {
		    while(arr[i]<=pivot) i++;
		    while(arr[j]>pivot) j--;
		    if(i<j) {
		    	temp = arr[i];
		    	arr[i] = arr[j];
		    	arr[j] = temp;
		    }
		} while(i<j);
		temp = arr[low];
		arr[low] = arr[j];
		arr[j] = temp;
		return j;
	}
	static void quicksort(int[] arr, int low, int high)
	{
		int p;
		if(low<high)
		{
			p = partition(arr,low,high);
			quicksort(arr,low,p-1);
			quicksort(arr,p+1,high);
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
       quicksort(arr,0,n-1);
       System.out.println();
       print(arr,n);
	}
}
