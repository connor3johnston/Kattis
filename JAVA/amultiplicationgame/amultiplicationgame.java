/*
Rating: ~ 5.0 / 10
Link: https://open.kattis.com/problems/amultiplicationgame
*/

import java.util.Scanner;

public class amultiplicationgame {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      while(scan.hasNext()) {
         long p = 1;
         int count = 0;
         long num = scan.nextLong();

         while (p < num) {
            if (count%2 == 0) {
               p *= 9;
               count++;
            }
            else {
               p *= 2;
               count++;
            }
         }
         if (count%2 == 1) {
            System.out.println("Stan wins.");
         }
         else {
            System.out.println("Ollie wins.");
         }
      }
   }
}
