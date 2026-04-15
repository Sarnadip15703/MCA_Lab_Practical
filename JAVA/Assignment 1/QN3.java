/*Write a java program to print a Fibonacci sequence where only first 
8 positive prime numbers are present. Also print the prime numbers separately. */
public class QN3 {
    int a=0,b=1,c=0,COUNT=0;
    void fibbo(){
        while(true){
            c=a+b;
            a=b;
            b=c;
            int count=0;
            for(int j=1;j<=a;j++){
                if(a%j==0){
                    count++;
                }
            }
            if(count==2){
                System.out.println(a);
                COUNT++;
                if(COUNT==8){
                    break;
                }
                
            }

        }
    }
}
class Prime_fibbo {
    public static void main(String[] args) {
        QN3 s=new QN3();
        s.fibbo();    
    }
}
