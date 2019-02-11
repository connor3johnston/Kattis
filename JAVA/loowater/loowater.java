/*
Rating: ~ 2.8 / 10
Link: https://open.kattis.com/problems/loowater
*/

import java.util.*;

public class loowater {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      String[] here = scan.nextLine().split(" ");
      int headsC = Integer.parseInt(here[0]);
      int knightsC = Integer.parseInt(here[1]);

      while (headsC != 0 && knightsC != 0) {
         int coins = 0;
         int[] heads = new int[headsC];
         int[] knights = new int[knightsC];
         for (int x = 0; x < headsC; x++) {
            heads[x] = Integer.parseInt(scan.nextLine());
         }
         for (int x = 0; x < knightsC; x++) {
            knights[x] = Integer.parseInt(scan.nextLine());
         }

         Arrays.sort(heads);
         Arrays.sort(knights);
         boolean check = true;
         int dif = knightsC - headsC;
         int index = 0;
         for (int x = 0; x < knightsC; x++) {
            int height = knights[x];
            int diam = heads[index];
            if (height >= diam) {
               coins += height;
               index++;
            }
            if (index >= heads.length) {
               check = false;
               break;
            }
         }

         if (check) {
            System.out.println("Loowater is doomed!");
         }
         else {
            System.out.println(coins);
         }
         here = scan.nextLine().split(" ");
         headsC = Integer.parseInt(here[0]);
         knightsC = Integer.parseInt(here[1]);
      }
   }
}
