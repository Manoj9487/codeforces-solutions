import java.util.*;

public class TargetScoring {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine();  // Consume newline
        
        int[] rings = {1, 2, 3, 4, 5};
        
        for (int test = 0; test < t; test++) {
            char[][] grid = new char[10][10];
            int total = 0;
            
            for (int i = 0; i < 10; i++) {
                String line = sc.nextLine().trim();
                for (int j = 0; j < 10; j++) {
                    grid[i][j] = line.charAt(j);
                }
            }
            
            for (int i = 0; i < 10; i++) {
                for (int j = 0; j < 10; j++) {
                    if (grid[i][j] == 'X') {
                        int dist = Math.min(i, 9 - i);
                        dist = Math.min(dist, Math.min(j, 9 - j));
                        total += rings[dist];
                    }
                }
            }
            System.out.println(total);
            
            // Consume any extra newline between test cases if needed
            if (test < t - 1) {
                sc.nextLine();
            }
        }
        sc.close();
    }
}
