class Fibonacci {
    void printFirstTen() {
        int a = 0;
        int b = 1;
        int sum = 0;

        System.out.println("First 10 Fibonacci numbers:");
        for (int i = 1; i <= 10; i++) {
            System.out.print(a + (i < 10 ? " " : ""));
            sum += a;
            int next = a + b;
            a = b;
            b = next;
        }

        System.out.println();
        System.out.println("Sum of the first 10 Fibonacci numbers: " + sum);
    }
}

public class Question1 {
    public static void main(String[] args) {
        Fibonacci fibonacci = new Fibonacci();
        fibonacci.printFirstTen();
    }
}
