import java.util.Scanner;

public class TurtleMaster {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      char[][] board = new char[8][8];
      for (int x = 0; x < 8; x++) {
         String[] line = scan.nextLine().split("");
         for (int y = 0; y < 8; y++) {
            board[x][y] = line[y].charAt(0);
         }
      }
      board[7][0] = 'T';
      int x = 7;
      int y = 0;
      boolean here = true;
      final int left = 9;
      final int up = 12;
      final int down = 6;
      final int right = 3;
      int direction = right;
      char track = '.';
      String[] commands = scan.nextLine().split("");
      for (String com: commands) {
         if (com.equals("F")) {
            int tempX = -1;
            int tempY = -1;
            switch (direction) {
               case right:
                  tempX = x;
                  tempY = y + 1;
                  break;
                  
               case left:
                  tempX = x;
                  tempY = y - 1;
                  break;
                  
               case up:
                  tempX = x - 1;
                  tempY = y;
                  break;
                  
               case down:
                  tempX = x + 1;
                  tempY = y;
                  break;
            }
            if (tempX > 7 || tempX < 0 || tempY > 7 || tempY < 0 || board[tempX][tempY] == 'C' || board[tempX][tempY] == 'I') {
               here = false;
               break;
            }
            board[x][y] = '.';
            x = tempX;
            y = tempY;
            track = board[x][y];
            board[x][y] = 'T';
         
         }
         else if (com.equals("R")) {
            if (direction + 3 == 15) {
               direction = 3;
            }
            else {
               direction += 3;
            }            }
         else if (com.equals("L")) {
            if (direction - 3 == 0) {
               direction = 12;
            }
            else {
               direction -= 3;
            }
         }
         else if (com.equals("X")) {
            int tempX = -1;
            int tempY = -1;
            switch (direction) {
               case right:
                  tempX = x;
                  tempY = y + 1;
                  break;
                  
               case left:
                  tempX = x;
                  tempY = y - 1;
                  break;
                  
               case up:
                  tempX = x - 1;
                  tempY = y;
                  break;
                  
               case down:
                  tempX = x + 1;
                  tempY = y;
                  break;
            }
            if (tempX > 7 || tempX < 0 || tempY > 7 || tempY < 0 || board[tempX][tempY] != 'I') {
               here = false;
               break;
            }
            board[tempX][tempY] = '.';
         }
      }
      if (track == 'D' && here) {
         System.out.println("Diamond!");
      
      }
      else {
         System.out.println("Bug!");
      }
   }
}