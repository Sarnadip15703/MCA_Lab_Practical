class PrimeChecker {
    void printPrimes() {
        for (int i = 2; i <= 1000; i++) {
            int p = 1;
            for (int j = 2; j * j <= i; j++) {
                if (i % j == 0) {
                    p = 0;
                    break;
                }
            }
            if (p == 1) {
                System.out.println(i);
            }
        }
    }
}

public class Question2 {
    public static void main(String[] args) {
        PrimeChecker p = new PrimeChecker();
        p.printPrimes();
    }
}

