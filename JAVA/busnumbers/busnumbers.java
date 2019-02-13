/*
Rating: ~ 2.3 / 10
Link: https://open.kattis.com/problems/mixedfractions
*/

import java.util.Scanner;
import java.util.Arrays;

public class busnumbers {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int buses = Integer.parseInt(scan.nextLine());
      int[] group = new int[buses];
      for (int x = 0; x < buses; x++) {
         group[x] = scan.nextInt();
      }
      Arrays.sort(group);
      String[] out = new String[buses];
      int track = 0;
      int y = 1;
      while (y < buses) {
         int index1 = y - 1;
         while (y < buses && group[y] - group[y-1] == 1) {
            y++;
         }
         int index2 = y - 1;
         String output = "";
         if (index1 == index2) {
            output = Integer.toString(group[index1]);
            out[track] = output;
         }
         else if (group[index2] - group[index1] == 1) {
            output = Integer.toString(group[index1]);
            out[track] = output;
            track++;
            output = Integer.toString(group[index2]);
            out[track] = output;
         }
         else {
            output = group[index1] + "-" + group[index2];
            out[track] = output;
         }
         track++;
         y++;
      }
      if (group[buses - 1] - group[buses-2] != 1) {
         out[track] = Integer.toString(group[buses-1]);
      }
      for (String here: out) {
         if (here == null) {
            break;
         }
         System.out.print(here + " ");
      }
   }
}
