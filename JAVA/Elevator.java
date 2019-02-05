import java.util.*;

public class Elevator {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      long floors = scan.nextLong();
      long start = scan.nextLong();
      long goal = scan.nextLong();
      long up = scan.nextLong();
      long down = scan.nextLong();
   
      long moves = 0;
      boolean check = false;
      if (start > goal && down == 1) {
         moves = start - goal;
         check = true;
      }
      else if (start < goal && up == 1) {
         moves = goal - start;
         check = true;
      }
      else if ((start > goal && down > up) || (start < goal && up > down)) {
         moves += (Math.abs((goal - start))/(up + down)) * 2;
         check = true;
      }
      if (check) {
         System.out.println(moves);
      }
      else {
         System.out.println("use the stairs");
      }
   }
}