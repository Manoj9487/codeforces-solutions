import java.util.*;
public class EqualCandies {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        while(t-- > 0) {
            int n = sc.nextInt();

            int [] arr = new int[n];

            for(int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }

            Arrays.sort(arr);

            int min = arr[0];
            int total = 0;

            for (int i : arr) {
                total += (i - min);
            }
            System.out.println(total);


        }

        sc.close();
    }
    
}
