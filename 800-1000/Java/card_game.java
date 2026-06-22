import java.util.*;

public class CardGame {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String card = sc.next();

        Boolean win = false;
        for(int i = 0; i < 5; i++) {
            char cardRank = card.charAt(0);
            char cardSuit = card.charAt(1);

            String ct = sc.next();

            if (ct.charAt(0) == cardRank || ct.charAt(1) == cardSuit) {
                win = true;
            }
        
        }
        if (win) {
            System.out.println("YES");
        }
        else {
            System.out.println("NO");
        }
        sc.close();
    }
}
