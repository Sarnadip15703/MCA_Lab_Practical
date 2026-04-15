//Java Program to Check Whether a Number can be Expressed as Sum of Two Prime Numbers.
import java.util.Scanner;

class SumOfTwoPrimes{

    boolean isPrime(int num) {
        if (num <= 1) return false;
        for (int i = 2; i <= num / 2; i++) {
            if (num % i == 0)
                return false;
        }
        return true;
    }

}

public class QN13 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();

        SumOfTwoPrimes obj = new SumOfTwoPrimes();
        boolean found = false;

        for (int i = 2; i <= n / 2; i++) {
            if (obj.isPrime(i) && obj.isPrime(n - i)) {
                System.out.println(n + " = " + i + " + " + (n - i));
                found = true;
            }
        }

        if (!found) {
            System.out.println(n + " cannot be expressed as sum of two primes.");
        }

        sc.close();
    }
}