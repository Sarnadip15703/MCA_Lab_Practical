//Write a java program to check whether a given number is palindrome number or not.
import java.util.Scanner;

class Palindrome {

    boolean isPalindrome(int num) {
        int original = num;
        int reverse = 0;

        while (num > 0) {
            int digit = num % 10;
            reverse = reverse * 10 + digit;
            num = num / 10;
        }

        return original == reverse;
    }
}

public class QN14 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();

        Palindrome obj = new Palindrome();

        if (obj.isPalindrome(n)) {
            System.out.println(n + " is a Palindrome");
        } else {
            System.out.println(n + " is NOT a Palindrome");
        }

        sc.close();
    }
}
