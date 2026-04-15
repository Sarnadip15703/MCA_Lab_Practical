//Java Program to Display Factors of a Number.
import java.util.Scanner;

public class QN12 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter n :");
        int n=sc.nextInt();
        demo d=new demo();
        d.fact(n);
        sc.close();
        
    }

}
class demo{
    void fact(int n){
        System.out.println("all the factor of "+n);
       for(int i=1;i<=n;i++){
            if(n%i==0){
                System.out.println(""+i);
            }
        }
    }
}