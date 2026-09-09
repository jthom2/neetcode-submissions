// class Solution {public:vector<int> twoSum(vector<int>& nums, int target) {
//         std::unordered_map<int, int> m;
//         for (int i = 0; i < nums.size(); i++) {
//             int x=target-nums[i];
//             if (m.contains(x)) {return {m[x], i};}
//             m[nums[i]] = i;} return {};}};

#include <vector>
#include <cstddef>
#include <cstdint>
#include <climits>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        const int n = static_cast<int>(nums.size());

        // Open-addressing table sized to a power of two, load factor <= 0.5.
        // Power-of-two size means bucket indexing is `& mask` instead of `% cap`,
        // which avoids integer division (division is ~20-40x slower than AND).
        std::size_t cap = 16;
        while (cap < static_cast<std::size_t>(n) * 2) cap <<= 1;
        const std::size_t mask = cap - 1;

        // key+idx stored together (not in two separate arrays) so a probe that
        // finds the key already has the value in the same cache line.
        struct Entry { int key; int idx; };

        // INT_MIN can never be a real input value (constraints guarantee
        // |nums[i]| <= 1e9), so it's a safe "empty slot" sentinel — no
        // separate occupied-bitmap needed.
        std::vector<Entry> table(cap, Entry{INT_MIN, 0});

        // MurmurHash3 finalizer: mixes bits so masking down to `cap` buckets
        // doesn't cluster inputs that happen to share low bits.
        auto mix = [](std::uint32_t h) {
            h ^= h >> 16; h *= 0x85ebca6bu;
            h ^= h >> 13; h *= 0xc2b2ae35u;
            h ^= h >> 16;
            return h;
        };

        for (int i = 0; i < n; ++i) {
            const int v = nums[i];
            const int need = target - v;

            // Single probe pass replaces contains() + operator[] (two hashes,
            // two lookups) with one hash and one linear-probe walk.
            std::size_t p = mix(static_cast<std::uint32_t>(need)) & mask;
            while (table[p].key != INT_MIN) {
                if (table[p].key == need) return {table[p].idx, i};
                p = (p + 1) & mask;
            }

            p = mix(static_cast<std::uint32_t>(v)) & mask;
            while (table[p].key != INT_MIN) p = (p + 1) & mask;
            table[p] = Entry{v, i};
        }
        return {};
    }
};