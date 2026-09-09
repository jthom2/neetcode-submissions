class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> diffs;

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];

            if (diffs.count(diff)) {
                if (i < diffs[nums[i]]) {
                    return {i, diffs[diff]};
                } else {
                    return {diffs[diff], i};
                }
            } else {
                diffs.insert({nums[i], i});
            }
        }

    

      return {-1};
    }
};
