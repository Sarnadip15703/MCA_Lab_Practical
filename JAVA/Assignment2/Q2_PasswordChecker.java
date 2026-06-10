// Q2. Password Checker
// Assignment II - Array & String
// Subject: Object Oriented Programming with JAVA (MCAN-293)

public class Q2_PasswordChecker {

    static class PasswordValidator {
        public int checkPassword(String str) {
            if (str == null) return 0;
            int n = str.length();

            // At least 4 characters
            if (n < 4) return 0;

            // Starting character must not be a number
            if (Character.isDigit(str.charAt(0))) return 0;

            boolean hasDigit = false;
            boolean hasUpperCase = false;

            for (int i = 0; i < n; i++) {
                char c = str.charAt(i);

                // Must not have space or slash
                if (c == ' ' || c == '/') return 0;

                if (Character.isDigit(c)) hasDigit = true;
                if (Character.isUpperCase(c)) hasUpperCase = true;
            }

            // At least one numeric digit and at least one capital letter
            if (!hasDigit || !hasUpperCase) return 0;

            return 1;
        }
    }

    public static void main(String[] args) {
        PasswordValidator validator = new PasswordValidator();

        // Example
        System.out.println("Input: aA1_67");
        System.out.println("Output: " + validator.checkPassword("aA1_67")); // Expected: 1

        // Sample Input
        System.out.println("\nInput: a987");
        System.out.println("Output: " + validator.checkPassword("a987")); // Expected: 0 (no uppercase)

        System.out.println("\nInput: abC012");
        System.out.println("Output: " + validator.checkPassword("abC012")); // Expected: 1
    }
}
