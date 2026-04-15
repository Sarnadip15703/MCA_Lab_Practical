/*Write a program to find sum of all integers greater than 100 and less than 200
that are divisible by 7.*/
public class QN16 {
    public static void main(String[] args) {
        int sum = 0;

        for (int i = 105; i < 200; i += 7) {
            sum += i;
            System.out.print(i + " ");
        }

        System.out.println("\nSum = " + sum);
    }
}