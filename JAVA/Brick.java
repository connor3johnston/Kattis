import java.util.*;

public class Brick {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int height = scan.nextInt();
      int width = scan.nextInt();
      int bricks = scan.nextInt();
      int layer = 0;
      boolean here = false;
      int check;
      int x = 0;
      while (x < bricks) {
         check = 0;
         while (check < width) {
            check += scan.nextInt();
            x++;
         }
         if (check != width) {
            break;
         }
         layer++;
         if (layer == height) {
            here = true;
            break;
         }
      }
      if (here) {
         System.out.println("YES");
      }
      else {
         System.out.println("NO");
      }
   }
}