public class Solution {
    public int LengthOfLongestSubstring(string s) {
        int left = 0;
        int maxLength = 0;
        Dictionary<char,int> lastSeen = new Dictionary<char,int>();
        for(int right = 0 ; right < s.Length ; right++)
        {
            char c = s[right];
            if (lastSeen.ContainsKey(c) && lastSeen[c] >= left)
            {
                left = lastSeen[c] + 1;
            }
            lastSeen[c] = right;

            maxLength = Math.Max(maxLength,right - left +1);
        }
return maxLength;
    }
}
