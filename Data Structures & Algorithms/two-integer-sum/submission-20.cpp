// class Solution {
// public:
//     vector<int> twoSum(vector<int>& nums, int target) {
//         std::unordered_map<int, int> m;
//         for (int i = 0; i < nums.size(); i++) {
//             int x=target-nums[i];
//             if (m.contains(x)) {return {m[x], i};}
//             m[nums[i]] = i;}
//       return {};}};

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        m.reserve(nums.size());

        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            auto it = m.find(complement);

            if (it != m.end())
                return {it->second, i};

            m.emplace(nums[i], i);
        }

        return {};
    }
};