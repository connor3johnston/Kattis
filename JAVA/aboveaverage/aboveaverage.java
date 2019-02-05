/*
Rating: ~ 2.0 / 10
Link: https://open.kattis.com/problems/aboveaverage
*/

import java.util.Scanner;
import java.text.DecimalFormat;

public class aboveaverage {
   public static void main(String[] args) {

      Scanner sc = new Scanner(System.in);
      DecimalFormat df = new DecimalFormat("##0.000'%'");
      int cases = sc.nextInt();

      for (int x = 0; x < cases; x++) {
         int people = sc.nextInt();
         double people2 = (double) people;
         double[] input = new double[people];
         double total = 0;

         for (int y = 0; y < people; y++) {
            input[y] = sc.nextInt();
            total += input[y];
         }

         double average = total/people2;
         double above = 0;
         for (int c = 0; c < people; c++) {
            if (input[c] > average) {
               above++;
            }
         }

         System.out.println(df.format((above/people2) * 100));
      }
   }
}
