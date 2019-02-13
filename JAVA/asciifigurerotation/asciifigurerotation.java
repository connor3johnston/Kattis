/*
Rating: ~ 3.8 / 10
Link: https://open.kattis.com/problems/asciifigurerotation
*/

import java.util.*;

public class asciifigurerotation {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int lines = Integer.parseInt(scan.nextLine());
      while (lines != 0) {
         char[][] grid = new char[lines][100];
         int max = 0;
         for (int x = 0; x < lines; x++) {
            char[] here = scan.nextLine().toCharArray();
            int check = here.length;
            for (int y = 0; y < check ; y++) {
               grid[x][y] = here[y];
            }
            if (check > max) {
               max = check;
            }
         }

         for (int col = 0; col < max; col++) {
            String output = "";
            for (int row = lines - 1; row > -1; row--) {
               char print = grid[row][col];
               if (print == '|') {
                  output += "-";
               }
               else if (print == '-') {
                  output += "|";;
               }
               else if (print == '\0') {
                  output += " ";
               }
               else {
                  output += print;
               }
            }
            for (int p = output.length() - 1; p > -1; p--) {
               if (output.charAt(p) == ' ') {
                  output = output.substring(0, p);
               }
               else if (output.charAt(p) != ' ') {
                  break;
               }
            }
            System.out.println(output);
         }
         lines = Integer.parseInt(scan.nextLine());
         if (lines != 0) {
            System.out.println();
         }
      }
   }
}
