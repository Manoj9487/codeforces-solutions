import java.util.*;
public class Collecting_Coins {
    public static void main(String [] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while(t-- > 0) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            int n = sc.nextInt();

            int maxi1 = Math.max(a, b);
            int maxi = Math.max(maxi1, c);
            
            int toShare = (maxi - a) + (maxi - b) + (maxi - c);
            if (toShare <= n && (n - toShare) % 3 == 0) {
                System.out.println("YES");
            }
            else {
                System.out.println("NO");
            }
        }
        sc.close();
    }
}
