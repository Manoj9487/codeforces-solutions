import java.util.*;
public class Polycarp_Coins {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        while(t-- > 0) {
            int n = sc.nextInt();
            int rem = n % 3;
            if (n == 1) {
                System.out.println(1 + " " + 0);
            }
            else if (n == 2) {
                System.out.println(0 + " " + 1);
            }
            else {
                if (rem == 1) {
                    System.out.println((int) n / 3 + 1 + " " + (int) n / 3);
                }
                else if (rem == 2) {
                    System.out.println((int) n / 3  + " " + (int) (n / 3 + 1));
                }
                else {
                    System.out.println((int) n / 3 + " " + (int) n / 3);
                }
            }
        }

        sc.close();

    }
    
}
