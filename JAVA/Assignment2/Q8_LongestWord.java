// Q8. Find the Longest Word
// Assignment II - Array & String
// Subject: Object Oriented Programming with JAVA (MCAN-293)

import java.util.Scanner;

public class Q8_LongestWord {

    static class WordFinder {
        public String findLongestWord(String sentence) {
            String[] words = sentence.split("\\s+");
            String longest = "";
            for (String word : words) {
                // Remove punctuation for fair comparison
                String cleaned = word.replaceAll("[^a-zA-Z]", "");
                if (cleaned.length() > longest.length()) {
                    longest = cleaned;
                }
            }
            return longest;
        }
    }

    public static void main(String[] args) {
        WordFinder finder = new WordFinder();
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter sentence: ");
        String sentence = scanner.nextLine();
        System.out.println("Longest Word: " + finder.findLongestWord(sentence));

        scanner.close();

        // Test case
        System.out.println("\n--- Test Case ---");
        String testSentence = "Innovation distinguishes between a leader and a follower.";
        System.out.println("Input: " + testSentence);
        System.out.println("Longest Word: " + finder.findLongestWord(testSentence));
        // Expected: distinguishes
    }
}
