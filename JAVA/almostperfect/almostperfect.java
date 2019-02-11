/*
Rating: ~ 3.4 / 10
Link: https://open.kattis.com/problems/almostperfect
*/

import java.io.*;
import java.util.*;

public class almostperfect {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      while (scan.hasNext()) {
         int number = scan.nextInt();
         int check = factors(number);
         if (check == number) {
            System.out.println(number + " perfect");
         }
         else if (Math.abs(number - check) <= 2) {
            System.out.println(number + " almost perfect");
         }
         else {
            System.out.println(number + " not perfect");
         }
      }
   }

   public static int factors(int number) {
      int sum = 1;
      double root = Math.sqrt(number);
      for (int x = 2; x <= root; x++) {
         if (number%x == 0) {
            sum += x;
            if (x == root) {
               continue;
            }
            sum += (number/x);
         }
      }
      return sum;
   }
}
