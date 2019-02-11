/*
Rating: ~ 2.6 / 10
Link: https://open.kattis.com/problems/froshweek2
*/

import java.util.*;

public class froshweek2 {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int t = scan.nextInt();
      int i = scan.nextInt();
      scan.nextLine();
      String[] tasks = scan.nextLine().split(" ");
      String[] intervals = scan.nextLine().split(" ");

      Arrays.sort(tasks);
      Arrays.sort(intervals);
      int track = 0;
      int index = 0;
      for (int x = 0; x < i; x++) {
         int interval = Integer.parseInt(intervals[x]);
         int task = Integer.parseInt(tasks[index]);
         if (task <= interval) {
            track++;
            index++;

         }
      }
      System.out.println(track);
   }
}
