//Write a java program to print primes from 1 to 1000.
public class QN2 {
    void prime(){
        for (int i=1;i<1000;i++){
            int count=0;
            for(int j=1;j<=i;j++){
                if(i%j==0){
                    count++;
                }
            }
            if(count==2){
                System.out.println(i);
            }
        }
    }
}
class Prime {
    public static void main(String[] args) {
        QN2 d=new QN2();
        d.prime();

    }
}