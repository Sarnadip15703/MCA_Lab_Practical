// Q5. Anagram Check
// Assignment II - Array & String
// Subject: Object Oriented Programming with JAVA (MCAN-293)

import java.util.Arrays;

public class Q5_AnagramCheck {

    static class AnagramChecker {
        public boolean isAnagram(String s, String t) {
            if (s.length() != t.length()) return false;
            char[] sArr = s.toCharArray();
            char[] tArr = t.toCharArray();
            Arrays.sort(sArr);
            Arrays.sort(tArr);
            return Arrays.equals(sArr, tArr);
        }
    }

    public static void main(String[] args) {
        AnagramChecker checker = new AnagramChecker();

        // Example 1
        String s1 = "anagram", t1 = "nagaram";
        System.out.println("Input: s = \"" + s1 + "\", t = \"" + t1 + "\"");
        System.out.println("Output: " + checker.isAnagram(s1, t1)); // Expected: true

        // Example 2
        String s2 = "rat", t2 = "car";
        System.out.println("\nInput: s = \"" + s2 + "\", t = \"" + t2 + "\"");
        System.out.println("Output: " + checker.isAnagram(s2, t2)); // Expected: false
    }
}
