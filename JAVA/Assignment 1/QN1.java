/*Write a java program to print first 10 numbers in Fibonacci sequence.
Also print the sum of the numbers.*/
public class QN1{

    void fibo(int n){
        int a = 0, b = 1, c = 0, sum = 0;
        for(int i=1; i<=n; i++){
            sum += a;
            System.out.print(a + ", ");
            c = a + b;
            a = b;
            b = c;
        }

        System.out.print("\nSum is: " + sum);
    }

    public static void main(String args[]){
        int n = 10;
        QN1 obj = new QN1();
        obj.fibo(n);
    }
}