package unit_arraysAndstrings;

import java.util.Scanner;

public class InsertionSort {

	static void print(int[] arr, int n)
    {
    	int i;
    	for(i=0;i<n;i++)
    	{
    		System.out.print(arr[i]+" ");
    	}
    }
	static void insertionsort(int[] arr, int n)
	{
		int key,i,j,temp;
		for(i=1;i<=n-1;i++)
		{
			key = arr[i];
			j = i-1;
			while(j>=0 && arr[j]>key)
			{
				arr[j+1] = arr[j];
				j--;
			}
			arr[j+1] = key;
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
       insertionsort(arr,n);
       System.out.println();
       print(arr,n);
	}
}
