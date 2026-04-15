//Write a program to generate 5 Random nos. between 1 to 100.
import java.util.Random;

class RandomNumbers {
    void randomNumbers() {
        Random rand = new Random();

        System.out.println("5 Random Numbers:");

        for (int i = 0; i < 5; i++) {
            int num = rand.nextInt(100) + 1;
            System.out.print(num + " ");
        }
    }
}

public class QN15 {
    public static void main(String[] args) {
        RandomNumbers obj = new RandomNumbers();
        obj.randomNumbers();
    }
}