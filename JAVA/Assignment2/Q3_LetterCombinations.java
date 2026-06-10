// Q3. Letter Combinations of a Phone Number
// Assignment II - Array & String
// Subject: Object Oriented Programming with JAVA (MCAN-293)

import java.util.ArrayList;
import java.util.List;

public class Q3_LetterCombinations {

    static class PhoneMapper {
        private final String[] phoneMap = {
            "",     // 0
            "",     // 1
            "abc",  // 2
            "def",  // 3
            "ghi",  // 4
            "jkl",  // 5
            "mno",  // 6
            "pqrs", // 7
            "tuv",  // 8
            "wxyz"  // 9
        };

        public List<String> letterCombinations(String digits) {
            List<String> result = new ArrayList<>();
            if (digits == null || digits.isEmpty()) return result;
            backtrack(result, digits, 0, new StringBuilder());
            return result;
        }

        private void backtrack(List<String> result, String digits, int index, StringBuilder current) {
            if (index == digits.length()) {
                result.add(current.toString());
                return;
            }
            String letters = phoneMap[digits.charAt(index) - '0'];
            for (char c : letters.toCharArray()) {
                current.append(c);
                backtrack(result, digits, index + 1, current);
                current.deleteCharAt(current.length() - 1);
            }
        }
    }

    public static void main(String[] args) {
        PhoneMapper mapper = new PhoneMapper();

        // Example 1
        System.out.println("Input: digits = \"23\"");
        System.out.println("Output: " + mapper.letterCombinations("23"));
        // Expected: [ad, ae, af, bd, be, bf, cd, ce, cf]

        // Example 2
        System.out.println("\nInput: digits = \"\"");
        System.out.println("Output: " + mapper.letterCombinations(""));
        // Expected: []

        // Example 3
        System.out.println("\nInput: digits = \"2\"");
        System.out.println("Output: " + mapper.letterCombinations("2"));
        // Expected: [a, b, c]
    }
}
