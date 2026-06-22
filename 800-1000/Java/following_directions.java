import java.util.*;
public class Following_Directions {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        while(t-- > 0) {
            int n = sc.nextInt();
            sc.nextLine(); // consume newline
            String s = sc.nextLine();
            
            int X = 0, Y = 0;
            boolean foundCandy = false;
            
            for(int i = 0; i < n; i++) {
                char ch = s.charAt(i);
                
                if (ch == 'L') X--;
                else if (ch == 'R') X++;
                else if (ch == 'U') Y++;
                else if (ch == 'D') Y--; // explicit else if for clarity
                
                if (X == 1 && Y == 1) {
                    foundCandy = true;
                    break; // optimization: no need to continue
                }
            }
            
            System.out.println(foundCandy ? "YES" : "NO");
        }
        sc.close();
    }
}
