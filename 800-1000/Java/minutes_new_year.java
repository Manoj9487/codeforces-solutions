import java.util.*;

public class Minutes_New_Year {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int t = sc.nextInt();

        while(t-- > 0) {
            int h = sc.nextInt();
            int m = sc.nextInt();

            System.out.println((24 - h - 1) * 60 + 60 - m);
        }


        sc.close();
    }
    
}
