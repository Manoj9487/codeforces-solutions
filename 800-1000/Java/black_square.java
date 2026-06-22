import java.util.*;
public class Black_Square {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int [] arr = new int[4];

        for(int i = 0; i < 4; i++) {
            arr[i] = sc.nextInt();
        }

        String s = sc.next();
        
        int sum = 0; 
        int idx;
        for (int i = 0; i < s.length(); i++) {
            idx = (int) s.charAt(i) - 49;
            sum += arr[idx];
            
        }
        
        System.out.println(sum);

        sc.close();
    }
    
}
