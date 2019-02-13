/*
Rating: ~ 3.4 / 10
Link: https://open.kattis.com/problems/pathtracing
*/

import java.util.*;

public class pathtracing {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      ArrayList<String> moves = new ArrayList<String>();
      int highest = 0;
      int lowest = 0;
      int rightest = 0;
      int leftest = 0;
      int x = 0;
      int y = 0;
      while(scan.hasNextLine()) {
         moves.add(scan.nextLine());
      }
      for(String move: moves) {
         if (move.equals("right")) {
            x++;
         }
         else if (move.equals("left")) {
            x--;
         }
         else if (move.equals("up")) {
            y++;
         }
         else {
            y--;
         }

         if (x > rightest) {
            rightest = x;
         }
         else if (x < leftest) {
            leftest = x;
         }
         if (y > highest) {
            highest = y;
         }
         else if (y < lowest) {
            lowest = y;
         }
      }
      int width = rightest - leftest + 3;
      int height = highest - lowest + 3;
      String[][] map = new String[height][width];
      for (int j = 0; j < height; j++) {
         map[j][0] = "#";
         map[j][width - 1] = "#";
      }
      for (int k = 0; k < width; k++) {
         map[0][k] = "#";
         map[height - 1][k] = "#";
      }
      int start_x = highest + 1;
      int start_y = 0 - leftest + 1;
      int row = start_x;
      int col = start_y;
      map[start_x][start_y] = "S";
      for(String move: moves) {
         if (move.equals("right")) {
            col++;
         }
         else if (move.equals("left")) {
            col--;
         }
         else if (move.equals("up")) {
            row--;
         }
         else {
            row++;
         }
         map[row][col] = "*";
      }
      map[row][col] = "E";
      map[start_x][start_y] = "S";
      for (int a = 0; a < height; a++) {
         for (int b = 0; b < width; b++) {
            if (map[a][b] == null) {
               System.out.print(" ");
            }
            else {
               System.out.print(map[a][b]);
            }
         }
         System.out.println();
      }
   }
}
