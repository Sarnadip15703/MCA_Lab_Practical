import java.util.Scanner;
class Validation {
    public static boolean validateUsername(String username) {
        if (username.isEmpty()) return false;
        if (username.length() < 3) {
            System.out.println("Username must be at least 3 characters long");
            return false;
        if (username.length() > 15) {
            System.out.println("Username must be at most 15 characters long");
            return false;
        }
        return true;
    }

    public static boolean validateEmail(String email) {
        if (!email.contains("@")) return false;
        int dotCount = 0;
        for (char c : email.toCharArray()) {
            if (c == '.') dotCount++;
        }
        return dotCount <= 1;
    }

    

    public static String extractDomain(String email) {
        int atIndex = email.indexOf("@");
        if (atIndex == -1) return "";
        return email.substring(atIndex + 1);
    }
}

public class uservalidation {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        User user = new User();
        
        System.out.print("Enter username: ");
        String username = sc.nextLine();
        user.setUsername(username.toLowerCase());
        
        System.out.print("Enter email: ");
        String email = sc.nextLine();
        user.setEmail(email);
        
        System.out.print("Enter password: ");
        String password = sc.nextLine();
        user.setPassword(password);
        
        boolean isValid = true;
        if (!Validation.validateUsername(user.getUsername())) {
            System.out.println("Username cannot be empty");
            isValid = false;
        }
        if (!Validation.validateEmail(user.getEmail())) {
            System.out.println("Invalid email: must contain '@' and at most one '.'");
            isValid = false;
        }
        if (!Validation.validatePassword(user.getPassword())) {
            System.out.println("Password must be longer than 8 characters, contain at least one capital letter, one digit, and one symbol");
            isValid = false;
        }
        
        if (isValid) {
            System.out.println("User validation successful");
            System.out.println("Username: " + user.getUsername());
            System.out.println("Domain: " + Validation.extractDomain(user.getEmail()));
        }
    }  
}
