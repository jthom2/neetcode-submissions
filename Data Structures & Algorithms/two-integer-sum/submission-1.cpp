class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int diff;
        // vector[int] result[1] = {-1, -1};
        std::unordered_map<int, int> diffs;

        for (int i = 0; i < nums.size(); i++) {
            diff = target - nums[i];

            if (diffs.count(diff)) {
                if (i < diffs[diff]) {
                    return {i, diffs[diff]};
                } else {
                    return {diffs[diff], i};
                }
            } else {
                diffs.insert({nums[i], i});
            }
        }

        std:cout << diffs[1];

      return {-1};
    }
};
