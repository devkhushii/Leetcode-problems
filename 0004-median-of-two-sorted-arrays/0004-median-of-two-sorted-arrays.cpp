class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        double ans=0;
        int m=nums1.size();
        int n=nums2.size();
        vector<int> merged(m+n,0);
        int right=merged.size()-1;
        int i=m-1;
        int j=n-1;
        while(right>=0 && j>=0 && i>=0){
            if(nums1[i]>=nums2[j]){
                merged[right]=nums1[i];
                i--;
               
            }else{
                merged[right]=nums2[j];
                j--;
                
            }
            

             right--;  
    }
    if(j>i){
        while(j>=0){
            merged[right]=nums2[j];
            j--;
            right--;
        }
    }else{
        while(i>=0){
            merged[right]=nums1[i];
            i--;
            right--;
        }
    }
    int mid=merged.size()/2;
    if (merged.size()%2==0){
        ans=(merged[mid]+merged[mid-1])/2.0;
    }else{
        ans=merged[mid];
    }
    return ans;
    }
};