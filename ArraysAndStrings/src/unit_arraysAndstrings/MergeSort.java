package unit_arraysAndstrings;

import java.util.Scanner;

public class MergeSort {

	static void print(int[] arr, int n)
    {
    	int i;
    	for(i=0;i<n;i++)
    	{
    		System.out.print(arr[i]+" ");
    	}
    }
	static void merge(int[] arr, int l, int m, int r)
	{
		int n1 = m-l+1;
		int n2 = r-m;
		int[] L = new int[n1];
		int[] R = new int[n2];
		int i,j,k;
		for(i=0;i<n1;i++)
		{
			L[i] = arr[l+i];
		}
		for(j=0;j<n2;j++)
		{
			R[j] = arr[m+j+1];
		}
		i=0; j=0; k=l;
		while(i<n1 && j<n2)
		{
			if(L[i]<=R[j])
			{
				arr[k] = L[i];
				i++;
			}
			else {
				arr[k] = R[j];
				j++;
			}
			k++;
		}
		while(i<n1)
		{
			arr[k] = L[i];
			i++;  k++;
		}
		while(j<n2)
		{
			arr[k] = R[j];
			j++;  k++;
		}
	}
	static void mergesort(int[] arr, int l, int r)
	{
		if(l<r)
		{
			int m = (l+r)/2;
			mergesort(arr,l,m);
			mergesort(arr,m+1,r);
			merge(arr,l,m,r);
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
       mergesort(arr,0,n-1);
       System.out.println();
       print(arr,n);
	}
}
