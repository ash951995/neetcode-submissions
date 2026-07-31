public class Solution {
    public bool CheckInclusion(string s1, string s2) {
        if (s1.Length > s2.Length) return false;
        int[] s1Count = new int[26];
        int[] s2Count = new int[26];
        foreach(char c in s1)
        {
            s1Count[c-'a'] ++ ;
        }
        int windowsize = s1.Length;
        for(int i =0;i<windowsize ;i++)
        {
            s2Count[s2[i] - 'a'] ++;
                    }
        int matches = 0;
        for(int i =0;i<26 ;i++)
        {
            if(s1Count[i] == s2Count[i]) matches ++;
                    }

        if (matches == 26) return true;

        for(int right = windowsize;right<s2.Length;right++)
        {
            char enter = s2[right];
            char leave = s2[right - windowsize];
            if(s1Count[leave - 'a'] == s2Count[leave -'a']) matches --;
            s2Count[leave -'a'] --;
            if(s1Count[leave - 'a'] == s2Count[leave -'a']) matches ++;

            if(s1Count[enter - 'a'] == s2Count[enter -'a']) matches --;
            s2Count[enter -'a'] ++;
            if(s1Count[enter - 'a'] == s2Count[enter -'a']) matches ++;

            if (matches == 26) return true;
        }
return false;
    }
}
