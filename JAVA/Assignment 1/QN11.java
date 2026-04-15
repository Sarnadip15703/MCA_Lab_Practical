//Java Program to Calculate the Power of a Number.
import java.util.Scanner;
public class QN11 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter base :");
        int x=sc.nextInt();
        System.out.println("enter exponient :");
        int y=sc.nextInt();
        demo d=new demo();
        d.print(x,y);
        sc.close();

    }
}
class demo{
    void print(int x,int y){
        System.out.println(" "+(int)Math.pow(x, y));
    }
}
