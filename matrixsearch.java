public class Solution {
	public boolean searchMatrix(int[][] a, int b) {
		if(a==null || a.length==0 || a[0].length==0)
			return false;

		int m = a.length;
		int n = a[0].length;

		int start = 0;
		int end = m*n-1;

		while(start<=end){
			int mid=(start+end)/2;
			int midX=mid/n;
			int midY=mid%n;

			if(a[midX][midY]==b)
				return true;

			if(a[midX][midY]<b){
				start=mid+1;
			}else{
				end=mid-1;
			}
		}

		return false;
	}
}