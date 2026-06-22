import java.util.*;
public class BlankSpace {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while(t-- > 0) {
            int n = sc.nextInt();

            int [] arr = new int[n];

            int cnt = 0;
            int longest = 0;

            for(int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();

                if (arr[i] == 0) {
                    cnt += 1;
                    longest = Math.max(cnt, longest);
                }
                else {
                    cnt = 0;
                }
            }
            System.out.println(longest);
        }

        sc.close();
    }
}
