/*Write a java program to print the following sequence:
0,-1,1,-4,1,-7,2,-10,3,-13,5,-16,8,... up to a given limit. */
public class QN5{

    void printSeries(int n){
        int a = 0, b = 1, c = 0, k = -1;
        for(int i=1; i<=n; i++){
            if(i % 2 != 0){
                System.out.print(a + ", ");
                c = a + b;
                a = b;
                b = c;
            }else{
                System.out.print(k + ", ");
                k-=3;
            }
        }
    }

    public static void main(String args[]){
        int n = 20;
        QN5 obj = new QN5();
        obj.printSeries(n);
    }
}