import java.util.Scanner;

class second
{
    int update(int n)
    {
        return n*5;
    }
}
class updemo {
    public static void main (String a[])
    {
        int x,y;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number");
        x = sc.nextInt();
        second obj = new second();
        y = obj.update(x);
        sc.close();
        System.out.println("Updated value: " + y);
    }
    
}
