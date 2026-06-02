import java .util.Scanner;

class prefix 
{
    void findPrefix(String str[])
    {
        String pre=str[0];
        for(int i=1;i<str.length;i++)
        {
            while(!str[i].startsWith(pre))
            {
                pre=pre.substring(0,pre.length()-1);
                if(pre.length()==0)
                {
                    System.out.println("No common prefix");
                    return;
                }
            }
        
        }
        System.out.println("Longest common prefix is: "+pre);
    }

}

class Question1
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner (System.in);
        int n=sc.nextInt();
        sc.nextLine();
        String str[]=new String[n];
        for(int i=0;i<n;i++)
        {
            str[i]=sc.nextLine();
        }
        prefix p=new prefix();
        p.findPrefix(str);  
    }
}