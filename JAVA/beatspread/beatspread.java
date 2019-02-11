/*
Rating: ~ 2.4 / 10
Link: https://open.kattis.com/problems/acm2
*/

import java.util.*;

public class beatspread {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int cases = scan.nextInt();
      for (int x = 0; x < cases; x++) {
         int total = scan.nextInt();
         int dif = scan.nextInt();
         boolean track = false;
         int start = 0;
         int end = total;
         if (total < dif || (total + dif)%2 != 0) {
            System.out.println("impossible");
         }
         else {
            String high = Integer.toString((total + dif)/2);
            String low = Integer.toString((total - dif)/2);
            System.out.println(high + " " + low);
         }
      }
   }
}
