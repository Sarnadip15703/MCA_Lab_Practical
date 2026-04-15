//Write a java program to print Factorial of a given number. Use any loop.
public class QN6 {

    int fact(int n){
        int f = 1;
        for(int i=1; i<=n; i++){
            f *= i;
        }
        return f;
    }

    public static void main(String args[]){
        int n = 8;
        QN6 obj = new QN6();
        System.out.println("Factorial is: " + obj.fact(n));
    }
}