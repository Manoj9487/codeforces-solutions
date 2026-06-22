import java.util.*;

public class Erasing_Zeroes {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();
        sc.nextLine();
        while(t-- > 0) {
            String s = sc.nextLine().trim();

            int first = -1;
            int last = -1;

            for(int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '1') {
                    first = i;
                    break;
                }
            }
            if (first == -1) {
                System.out.println(0);
                continue;
            }

            for(int i = s.length() - 1; i >= 0; i--) {
                if (s.charAt(i) == '1') {
                    last = i;
                    break;
                }
            }

            int count = 0;

            for(int i = first; i <= last; i++) {
                if (s.charAt(i) == '0') {
                    count += 1;
                }
            }
            
            System.out.println(count);
        }
        sc.close();
    }
}