class Solution {
public:
    int maxProduct(int n) {
        vector<int> digit;
        while(n!=0){
            int rem=n%10;
            n=n/10;
            digit.push_back(rem);
        }
        int product;
        int maxprod=0;
        for(int i=0;i<digit.size();i++){
            for(int j=i+1;j<digit.size();j++){
                product=digit[i]*digit[j];
                maxprod=max(maxprod,product);
            }
        }
        return maxprod;
    }
};