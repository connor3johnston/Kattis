/*
Rating: ~ 3.0 / 10
Link: https://open.kattis.com/problems/guessinggame
*/

import java.io.*;
import java.util.*;

public class guessinggame {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int next = Integer.parseInt(scan.nextLine());
      int highest = 10;
      int lowest = 1;
      while (next != 0) {
         String where = scan.nextLine();
         if (where.equals("right on")) {
            if (next <= highest && next >= lowest) {
               System.out.println("Stan may be honest");
            }
            else {
               System.out.println("Stan is dishonest");
            }
            highest = 10;
            lowest = 1;
         }
         if (where.equals("too low")) {
            if (next >= lowest) {
               lowest = next + 1;
            }
         }
         if (where.equals("too high")) {
            if (next <= highest) {
               highest = next - 1;
            }
         }
         next = Integer.parseInt(scan.nextLine());
      }
   }
}
