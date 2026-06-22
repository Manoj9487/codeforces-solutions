import java.util.*;
public class ColourBlindness {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        while(t-- > 0) {
            int n = sc.nextInt();
            sc.nextLine();
            String r1 = sc.nextLine();
            String r2 = sc.nextLine();

            boolean flag = true;

            for(int i = 0; i < n; i++) {
                char ch1 = r1.charAt(i);
                char ch2 = r2.charAt(i);

                if ((ch1 == 'R' && ch2 == 'G') || (ch1 == 'G' && ch2 == 'R')) {
                    flag = false;
                    break;
                }
                else if ((ch1 == 'R' && ch2 == 'B') || (ch1 == 'B' && ch2 == 'R')) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                System.out.println("YES");
            }
            else {
                System.out.println("NO");
            }

        }
        sc.close();
    }
    
}
