package unit_arraysAndstrings;

import java.util.Scanner;

public class CountSort {

	static void print(int[] arr, int n)
    {
    	int i;
    	for(i=0;i<n;i++)
    	{
    		System.out.print(arr[i]+" ");
    	}
    }
	static void countsort(int[] arr, int size)
	{
		int max = arr[0];
		int i;
		int[] count = new int[1000];
		int[] output = new int[1000];
		for(i=0;i<=size-1;i++)
		{
			if(arr[i]>max) max = arr[i];
		}
		for(i=0;i<=max;++i)
		{
			count[i] = 0;
		}
		for(i=0;i<size;i++)
		{
			count[arr[i]]++;
		}
		for(i=1;i<=max;i++)
		{
			count[i]+=count[i-1];
		}
		for(i=size-1;i>=0;i--)
		{
			output[count[arr[i]]-1] = arr[i];
			count[arr[i]]--;
		}
		for(i=0;i<size;i++)
		{
			arr[i] = output[i];
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
       countsort(arr,n);
       System.out.println();
       print(arr,n);
	}
}
