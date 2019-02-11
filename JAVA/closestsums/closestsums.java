/*
Rating: ~ 3.0 / 10
Link: https://open.kattis.com/problems/acm2
*/

import java.util.Scanner;

public class closestsums {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int cases = 0;
      while (scan.hasNextInt()) {
         cases++;
         System.out.println("Case " + cases + ":");
         int distinct = scan.nextInt();
         int[] numbers = new int[distinct];
         for (int x = 0; x < distinct; x++) {
            numbers[x] = scan.nextInt();
         }
         int queries = scan.nextInt();
         int sum = -1;
         for (int y = 0; y < queries; y++) {
            int q = scan.nextInt();
            for (int z = 0; z < numbers.length; z++) {
               for (int p = 1; p < numbers.length; p++) {
                  if (z == 0 && p == 1) {
                     sum = numbers[z] + numbers[p];
                  }
                  if (z == p) {
                     continue;
                  }
                  else {
                     int check = numbers[z] + numbers[p];
                     if (Math.abs(q - check) < Math.abs(q - sum)) {
                        sum = check;
                     }
                  }
               }
            }
            System.out.println("Closest sum to " + q + " is " + sum +".");
         }
      }
   }
}
