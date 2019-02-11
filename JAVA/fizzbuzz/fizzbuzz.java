/*
Rating: ~ 1.3 / 10
Link: https://open.kattis.com/problems/acm2
*/

import java.util.Scanner;

public class fizzbuzz {
   public static void main(String[] args) {

      Scanner scan = new Scanner(System.in);
      String[] input = scan.nextLine().split(" ");
      int x = Integer.parseInt(input[0]);
      int y = Integer.parseInt(input[1]);
      int n = Integer.parseInt(input[2]);

      for (int i = 1; i <= n; i++) {
         if (i%x == 0 && i%y == 0) {
            System.out.println("FizzBuzz");
         }
         else if (i%x == 0) {
            System.out.println("Fizz");
         }
         else if (i%y == 0) {
            System.out.println("Buzz");
         }
         else {
            System.out.println(i);
         }
      }
   }
}
