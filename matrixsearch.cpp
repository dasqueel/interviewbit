class Solution {
public:
    int searchMatrix(vector<vector<int> > &matrix, int target) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function


        //search row first
        int low = 0;
        int high = matrix.size();

        while(low < high) {
            int mid = low + (high - low) / 2;
            int cur = matrix[mid][0];

            if(cur == target) {
                return 1;
            } else if(cur > target) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }

        --low;

        if(low < 0) {
            return 0;
        }

        return bin(matrix[low], target);

    }

    bool bin(vector<int>& arr, int target) {
        int low = 0;
        int high = arr.size();
        while(low < high) {
            int mid = low + (high - low) / 2;
            int cur = arr[mid];

            if(cur == target) {
                return 1;
            } else if(cur > target) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }

        return 0;

    }
};