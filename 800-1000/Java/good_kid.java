
import java.util.*;

public class GoodKid {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int test = 0; test < t; test++) {
            int n = sc.nextInt();
            int[] a = new int[n];
            long prod = 1;
            boolean hasZero = false;
            int minNonZero = 10;
            for (int i = 0; i < n; i++) {
                a[i] = sc.nextInt();
                if (a[i] == 0) hasZero = true;
                else if (a[i] < minNonZero) minNonZero = a[i];
                prod *= a[i];
            }
            long ans;
            if (hasZero) {
                ans = 1;
                for (int num : a) {
                    if (num != 0) ans *= num;
                }
            } else {
                ans = prod / minNonZero * (minNonZero + 1);
            }
            System.out.println(ans);
        }
        sc.close();
    }
}
