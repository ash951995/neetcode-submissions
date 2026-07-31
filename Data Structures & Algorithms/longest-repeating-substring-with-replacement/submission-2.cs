public class Solution {
    public int CharacterReplacement(string s, int k) {
        int[] counts = new int[26];
        int left = 0;
        int maxFreq = 0;
        int maxLength = 0;
        for(int right = 0 ; right < s.Length ; right ++)
        {
            char c = s[right];
            counts[c - 'A'] ++;

            maxFreq = Math.Max(maxFreq,counts[c- 'A']);
            int windowLength = right - left +1;
            while(windowLength - maxFreq > k)
            {
                counts[s[left] - 'A'] --;
                left ++ ;
               windowLength = right - left +1;
            }
             maxLength = Math.Max(maxLength,windowLength);
        }
        return maxLength;
        
    }
}
