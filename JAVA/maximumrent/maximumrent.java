/*
Rating: ~ 2.8 / 10
Link: https://open.kattis.com/problems/maximumrent
*/

import java.io.*;
import java.util.*;

public class maximumrent {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      String[] line1 = scan.nextLine().split(" ");
      String[] line2 = scan.nextLine().split(" ");
      int rentFoot = Integer.parseInt(line1[0]);
      int rentBulb = Integer.parseInt(line1[1]);
      int maxThings = Integer.parseInt(line2[0]);
      int outlets = Integer.parseInt(line2[1]);

      int fts = maxThings/2;
      int bulbs = maxThings - fts;
      int rent = 0;

      while (bulbs > 0) {
         int track = 2 * fts + bulbs;
         if (track < outlets) {
            break;
         }
         int tryRent = rentFoot * fts  + rentBulb * bulbs;
         if (tryRent > rent) {
            rent = tryRent;
         }
         bulbs--;
         fts++;
      }
      bulbs = maxThings/2;
      fts = maxThings - bulbs;
      while (fts > 0) {
         int track = 2 * fts + bulbs;
         if (track < outlets) {
            break;
         }
         int tryRent = rentFoot * fts  + rentBulb * bulbs;
         if (tryRent > rent) {
            rent = tryRent;
         }
         fts--;
         bulbs++;
      }
      System.out.println(rent);
   }
}
