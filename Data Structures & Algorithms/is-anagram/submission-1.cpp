class Solution {
public:
    bool isAnagram(string s, string t) {
        int trvu = 0;
        std::unordered_map<char, int> sm;
        std::unordered_map<char, int> tm;
        
        if (s.size() != t.size()) {return false;}

        for (int i = 0; i < s.size(); i++) {
            if (!sm[s[i]]) {sm[s[i]] = 1;}
            if (!tm[t[i]]) {tm[t[i]] = 1;}

            if (sm[s[i]]) {sm[s[i]]++;}
            if (tm[t[i]]) {tm[t[i]]++;}
        }

        for (int j = 0; j < t.size(); j++) {
            if (sm[s[j]] == tm[s[j]]) {trvu++;}
        }

        if (trvu == t.size()) {return true;}

        return false;
    }
};
