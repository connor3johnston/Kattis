/*
Rating: ~ 2.6 / 10
Link: https://open.kattis.com/problems/simplicity
*/

import java.util.*;

public class simplicity {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      while (scan.hasNextLine()) {
         String[] line = scan.nextLine().split("");
         HashMap<String, Integer> map = new HashMap<String, Integer>();
         int simplicity = 0;
         for (String here: line) {
            if (map.containsKey(here)) {
               int value = map.get(here) + 1;
               map.put(here, value);
            }
            else {
               map.put(here, 1);
               simplicity++;
            }
         }
         int track = 1;
         int remove = 0;
         while (simplicity > 2) {
            if (map.containsValue(track)) {
               simplicity--;
               remove += track;
               map.values().remove(track);
            }
            else {
               track++;
            }
         }
         System.out.println(remove);
      }
   }
}
