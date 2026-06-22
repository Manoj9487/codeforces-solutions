import java.util.*;
public class LameKing {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();
        
        while(t-- > 0) {
            int r = sc.nextInt();
            int c = sc.nextInt();

            if (r == 0 | c == 0) {
                System.out.println(Math.abs(r + c) * 2 - 1G);
            }
            else {
                r = Math.abs(r);
                c = Math.abs(c);

                int diff = Math.abs(r - c);

                if (diff == 0) {
                    System.out.println(r + c);
                }
                else {
                    System.out.println(r + c + diff - 1);
                }
            }
        }

        sc.close();
    }
}
