//Java Program to Find GCD of two Numbers.
public class QN8{

    int gcd(int a, int b){
        int g = 1;
        for(int i=1; i<=Math.min(a, b); i++){
            if(a%i == 0 && b%i == 0){
                g = i;
            }
        }
        return g;
    }

    public static void main(String args[]){
        QN8 obj = new QN8();
        System.out.println(obj.gcd(12, 6));
    }
}