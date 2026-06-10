// Q9. Convert Sentence to Title Case
// Assignment II - Array & String
// Subject: Object Oriented Programming with JAVA (MCAN-293)

import java.util.Scanner;

public class Q9_TitleCase {

    static class TitleCaseConverter {
        public String toTitleCase(String sentence) {
            if (sentence == null || sentence.isEmpty()) return sentence;
            String[] words = sentence.split("\\s+");
            StringBuilder result = new StringBuilder();
            for (String word : words) {
                if (!word.isEmpty()) {
                    result.append(Character.toUpperCase(word.charAt(0)))
                          .append(word.substring(1).toLowerCase())
                          .append(" ");
                }
            }
            return result.toString().trim();
        }
    }

    public static void main(String[] args) {
        TitleCaseConverter converter = new TitleCaseConverter();
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter sentence: ");
        String sentence = scanner.nextLine();
        System.out.println("Title Case: " + converter.toTitleCase(sentence));

        scanner.close();

        // Test case
        System.out.println("\n--- Test Case ---");
        String testSentence = "java programming is fun";
        System.out.println("Input: " + testSentence);
        System.out.println("Title Case: " + converter.toTitleCase(testSentence));
        // Expected: Java Programming Is Fun
    }
}
