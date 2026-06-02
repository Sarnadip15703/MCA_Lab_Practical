import java.util.Scanner;
class Password
{
    void check (String str)
    {
        int cap=0,digit=0;
        if(str.length()<4)
        {
            System.out.println("Invalid");
            return;
        }
        if(Character.isDigit(str.charAt(0)))
        {
            System.out.println("Invalid");
            return;
        }
        for(int i=0;i<str.length();i++)
        {
            char ch=str.charAt(i);

            if(Character.isUpperCase(ch))
            {
                cap++;
            }
            if(Character.isDigit(ch))
            {
                digit++;
            }
            if((ch == ' ') || (ch == '/'))
            {
                System.out.println("Invalid");
                return;
            }
        }
        if(cap>0 && digit>0)
        {
            System.out.println("Valid");
        }
        else
        {
            System.out.println("Invalid");
        }
    }
}

class Question2
{
    public static void main(String args[])
    {
        Scanner sc =new Scanner(System.in);
        String str=sc.nextLine();
        Password p=new Password();
        p.check(str);
    }
}