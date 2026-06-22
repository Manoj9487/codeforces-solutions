import java.util.*;
public class FairPlayoff {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        while(t-- > 0) {
            int s1 = sc.nextInt();
            int s2 = sc.nextInt();
            int s3 = sc.nextInt();
            int s4 = sc.nextInt();

            int max1 = Math.max(s1, s2);

            int max2 = Math.max(s3, s4);

            int [] arr = {s1, s2, s3, s4};

            Arrays.sort(arr);

            if ((max1 == arr[3] && max2 == arr[2]) ||(max1 == arr[2] && max2 == arr[3])) {
                System.out.println("YES");
            }
            else {
                System.out.println("NO");
            }
 
        }

        sc.close();
    }
}
