/*Write a java program to print the following sequence:
2,1,4,2,6,6,8,24,10, and so on up to a given limit.*/
public class QN7 {

    void printSeries(int n){
        int a = 1, b = 1,  k = 1;
        for(int i=1; i<=n; i++){
            if(i % 2 != 0){
                System.out.print(2*k + ", ");
                k++;
            }else{
                a = a*b;
                System.out.print(a + ", ");
                b++;
            }
        }
    }

    public static void main(String args[]){
        int n = 10;
        QN7 obj = new QN7();
        obj.printSeries(n);
    }
}