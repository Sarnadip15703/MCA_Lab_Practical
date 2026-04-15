/*Write a java program to print the following sequence:
0,2,1,4,1,8,2,16,3,32,5,64,8,... up to a given limit.*/
public class QN4{

    void printSeries(int n){
        int a = 0, b = 1, c = 0, k = 1;
        for(int i=1; i<=n; i++){
            if(i % 2 != 0){
                System.out.print(a + ", ");
                c = a + b;
                a = b;
                b = c;
            }
            else{
                System.out.print((int)Math.pow(2, k) + ", ");
                k++;
            }
        }
    }

    public static void main(String args[]){
        int n = 20;
        QN4 obj = new QN4();
        obj.printSeries(n);
    }
}
