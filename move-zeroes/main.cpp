class Solution {
    public:
        void moveZeroes(vector<int>& nums) {
            int l1 = nums.size();
            nums.erase(remove(nums.begin(), nums.end(), 0), nums.end());
            int l2 = nums.size();
            nums.insert(nums.end(), l1-l2, 0);
        }
    };