
import java.util.*;

public class FoxSnake {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            if (i % 2 == 1) {
                // Odd rows: full ###
                for (int j = 0; j < m; j++) {
                    System.out.print('#');
                }
                System.out.println();
            } 
            else if (i % 4 == 2) {
                // Even, not multiple of 4: ...#
                for (int j = 0; j < m - 1; j++) {
                    System.out.print('.');
                }
                System.out.print('#');
                System.out.println();
            } else {
                // Multiple of 4: #...
                System.out.print('#');
                for (int j = 1; j < m; j++) {
                    System.out.print('.');
                }
                System.out.println();
            }
        }
        sc.close();
    }
}
