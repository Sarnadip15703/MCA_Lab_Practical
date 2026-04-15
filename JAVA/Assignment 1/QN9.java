//Write a java program to print sum of n terms in the series 1/1! +1/2!+1/3!.....
public class QN9{

    int fact(int n){
        int f = 1;
        for(int i=1; i<=n; i++){
            f *= i;
        }
        return f;
    }

    void printSeries(int n){
        int sum = 0;
        for(int i=1; i<=n; i++){
            sum += (i/fact(i));
            System.out.print( i + "/" + i + "!" + " + ");
        }
        System.out.println(": " + sum);
    }

    public static void main(String args[]){
        int n = 5;
        QN9 obj = new QN9();
        obj.printSeries(n);
    }
}