/*
Rating: ~ 2.1 / 10
Link: https://open.kattis.com/problems/turtlemaster
*/

import java.util.Scanner;

public class beehives {

   public static int distance(double[][] hives, int cases, double x1, double y1, double dist, int sour) {
      for (int x = 0; x < cases; x++) {
         double x2 = hives[x][0];
         double y2 = hives[x][1];
         double distance = Math.sqrt(Math.pow((x1 - x2), 2) + Math.pow((y1 - y2), 2));
         if (distance < dist && distance > 0) {
            sour += 1;
            break;
         }
      }

      return sour;
   }

   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      double distance = scan.nextDouble();
      int cases = scan.nextInt();
      String output = "";

      while (distance != 0 && cases != 0) {
         int sweet = 0;
         int sour = 0;
         double[][] hives = new double[cases][2];
         for (int x = 0; x < cases; x++) {
            for (int y = 0; y < 2; y++) {
               hives[x][y] = scan.nextDouble();
            }
         }
         for (int x = 0; x < cases; x++) {
            double x1 = hives[x][0];
            double y1 = hives[x][1];
            sour = distance(hives, cases, x1, y1, distance, sour);
            sweet = cases - sour;;
         }

         output += (sour + " sour, " + sweet + " sweet\n");
         distance = scan.nextDouble();
         cases = scan.nextInt();
      }
      System.out.println(output);
   }
}

