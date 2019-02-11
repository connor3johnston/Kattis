/*
Rating: ~ 2.1 / 10
Link: https://open.kattis.com/problems/plantingtrees
*/

import java.util.*;

public class plantingtrees {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int trees = Integer.parseInt(scan.nextLine());
      String[] line = scan.nextLine().split(" ");
      Integer[] days = new Integer[line.length];
      int index = 0;
      for (String here: line) {
         days[index] = Integer.parseInt(here);
         index++;
      }
      Arrays.sort(days, Collections.reverseOrder());
      int min = days[0] + 2;
      for (int x = 2; x <= trees; x++) {
         int check = days[x-1] + x + 1;
         if (check > min) {
            min = check;
         }
      }
      System.out.println(min);
   }
}
