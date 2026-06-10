// Q7. Unique Characters in a String
// Assignment II - Array & String
// Subject: Object Oriented Programming with JAVA (MCAN-293)

import java.util.HashSet;
import java.util.Scanner;

public class Q7_UniqueCharacters {

    static class CharacterChecker {
        public boolean hasAllUniqueCharacters(String str) {
            HashSet<Character> seen = new HashSet<>();
            for (char c : str.toCharArray()) {
                if (!seen.add(c)) return false;
            }
            return true;
        }
    }

    public static void main(String[] args) {
        CharacterChecker checker = new CharacterChecker();
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String input = scanner.nextLine();

        if (checker.hasAllUniqueCharacters(input)) {
            System.out.println("All characters are unique.");
        } else {
            System.out.println("String contains duplicate characters.");
        }

        scanner.close();

        // Test cases (for demonstration)
        System.out.println("\n--- Test Cases ---");
        System.out.println("\"abcde\" -> " + (checker.hasAllUniqueCharacters("abcde") ? "All characters are unique." : "String contains duplicate characters."));
        System.out.println("\"hello\" -> " + (checker.hasAllUniqueCharacters("hello") ? "All characters are unique." : "String contains duplicate characters."));
    }
}
