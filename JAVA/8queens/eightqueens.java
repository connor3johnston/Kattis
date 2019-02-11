/*
Rating: ~ 3.2 / 10
Link: https://open.kattis.com/problems/acm2
*/

import java.util.Scanner;

public class eightqueens {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      char[][] board = new char[8][8];
      int count = 0;
      for (int x = 0; x < 8; x++) {
         String piece = scan.nextLine();
         String[] pieces = piece.split("");
         for (int y = 0; y < 8; y++) {
            board[x][y] = pieces[y].charAt(0);
            if (pieces[y].charAt(0) == '*') {
               count++;
            }
         }
      }
      if (count != 8) {
         System.out.println("invalid");
      }
      else {
      boolean output = true;
      for (int check = 0; check < 4; check++) {
         if (check == 0) {
            output = rightDiagonal(board);
         }
         else if (check == 1) {
            output = leftDiagonal(board);
         }
         else if (check == 2) {
            output = horizontal(board);
         }
         else if (check == 3) {
            output = vertical(board);
         }
         if (!output) {
            break;
         }
      }
            System.out.println(output ? "valid" : "invalid");

      }
   }

   public static boolean rightDiagonal(char[][] board) {
      for (int x = 7; x > -1; x--) {
         int x1 = x;
         int y = 0;
         int count = 0;
         while (x1 > -1) {
            if (board[x1][y] == '*') {
               count++;
            }
            if (count > 1) {
               return false;
            }
            x1--;
            y++;
         }
      }
      for (int y = 0; y < 8; y++) {
         int y1 = y;
         int x = 7;
         int count = 0;
         while (y1 < 8) {
            if (board[x][y1] == '*') {
               count++;
            }
            if (count > 1) {
               return false;
            }
            x--;
            y1++;
         }
      }
      return true;
   }

   public static boolean leftDiagonal(char[][] board) {
      for (int x = 0; x < 8; x++) {
         int x1 = x;
         int y = 0;
         int count = 0;
         while (x1 < 8) {
            if (board[x1][y] == '*') {
               count++;
            }
            if (count > 1) {
               return false;
            }
            x1++;
            y++;
         }
      }
      for (int y = 0; y < 8; y++) {
         int y1 = y;
         int x = 0;
         int count = 0;
         while (y1 < 8) {
            if (board[x][y1] == '*') {
               count++;
            }
            if (count > 1) {
               return false;
            }
            x++;
            y1++;
         }
      }
      return true;
   }

   public static boolean vertical(char[][] board) {
      for (int x = 0; x < 8; x++) {
         int count = 0;
         for (int y = 0; y < 8; y++) {
            if (board[x][y] == '*') {
               count++;
            }
            if (count > 1) {
               return false;
            }
         }
      }
      return true;
   }

   public static boolean horizontal(char[][] board) {
      for (int y = 0; y < 8; y++) {
         int count = 0;
         for (int x = 0; x < 8; x++) {
            if (board[x][y] == '*') {
               count++;
            }
            if (count > 1) {
               return false;
            }
         }
      }
      return true;
   }
}
