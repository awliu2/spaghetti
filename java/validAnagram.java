class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        int table[] = new int[26];

        for (int i = 0; i < s.length(); i++) {
            table[s.charAt(i) - 'a']++;
        }

        for (int j = 0; j < t.length(); j++) {
            table[t.charAt(j) - 'a']--;
            if (table[t.charAt(j) - 'a'] < 0) {
                return false;
            }
        }
        
        for (int k = 0; k < table.length; k++) {
            if (table[k] != 0) {
                return false;
            }
        }
        return true;
    }

    //     Map<Character, Integer> countS = new HashMap<>();
    //     int len_s = s.length();
    //     int len_t = t.length();

    //     if (len_s != len_t) {
    //         return false;
    //     }
    //     for (int i = 0; i < len_s; i++) {
    //         if (countS.containsKey(s.charAt(i))) {
    //             countS.put(s.charAt(i), 1 +countS.get(s.charAt(i)));
    //         }
    //         else {
    //             countS.put(s.charAt(i), 1);
    //         }
    //     }

    //     for (int j = 0; j < len_t; j++) {
    //         if (!countS.containsKey(t.charAt(j))) {
    //             return false;
    //         }
    //         if (countS.get(t.charAt(j)) == 0) {
    //             return false;
    //         }
    //         countS.put(t.charAt(j),countS.get(t.charAt(j)) - 1);
    //     }
    //     for (Integer i : countS.values()) {
    //         if (i != 0) {
    //             return false;
    //         }
    //     }

    //     return true;
    // }
}