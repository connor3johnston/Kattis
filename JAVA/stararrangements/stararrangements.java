/*
Rating: ~ 1.4 / 10
Link: https://open.kattis.com/problems/stararrangements
*/

import java.io.*;
import java.util.*;

public class stararrangements {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int number = scan.nextInt();
      System.out.println(number + ":");
      for (int x = 2; x <= (number/2) + 1; x++) {
         int row1 = x;
         int row2 = row1 - 1;
         int track = row1 + row2;
         int check = 1;
         while (track < number) {
            if (check%2 ==1) {
               track += row1;
            }
            else {
               track += row2;
            }
            check++;
         }
         if (track == number) {
            System.out.println(row1 + "," + row2);
         }
         if (number%row1 == 0) {
            System.out.println(row1 + "," + row1);
         }
      }
   }
}
