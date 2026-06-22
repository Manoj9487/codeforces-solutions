import java.util.*;
public class TargetPractice {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();
        sc.nextLine();
        while(t-- > 0) {
            int score = 0;
            for(int i = 0; i < 10; i++) {
                String s = sc.nextLine();
                
                for(int j = 0; j < 10; j++) {
                    char ch = s.charAt(j);

                    if (ch == 'X') {
                        int spot = j + 1;

                        if (spot <= 5) {
                            score += spot;
                        }
                        else {
                            if (spot == 10) {
                                score += 1;
                            }
                            else {
                                score += 6 - spot % 5;
                            }
                        }
                    }
                }
            }
            System.out.println(score);
        }
        sc.close();
    }
}
