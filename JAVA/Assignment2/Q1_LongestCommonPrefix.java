// Q1. Longest Common Prefix
// Assignment II - Array & String
// Subject: Object Oriented Programming with JAVA (MCAN-293)

public class Q1_LongestCommonPrefix {

    static class PrefixFinder {
        public String longestCommonPrefix(String[] strs) {
            if (strs == null || strs.length == 0) return "";
            String prefix = strs[0];
            for (int i = 1; i < strs.length; i++) {
                while (!strs[i].startsWith(prefix)) {
                    prefix = prefix.substring(0, prefix.length() - 1);
                    if (prefix.isEmpty()) return "";
                }
            }
            return prefix;
        }
    }

    public static void main(String[] args) {
        PrefixFinder finder = new PrefixFinder();

        // Example 1
        String[] strs1 = {"flower", "flow", "flight"};
        System.out.println("Input: [\"flower\", \"flow\", \"flight\"]");
        System.out.println("Output: \"" + finder.longestCommonPrefix(strs1) + "\""); // Expected: "fl"

        // Example 2
        String[] strs2 = {"dog", "race", "car"};
        System.out.println("\nInput: [\"dog\", \"race\", \"car\"]");
        System.out.println("Output: \"" + finder.longestCommonPrefix(strs2) + "\""); // Expected: ""
    }
}
