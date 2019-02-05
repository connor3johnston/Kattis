import java.util.Scanner;

public class SimonSays {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int cases = Integer.parseInt(scan.nextLine());
      for (int x = 0; x < cases; x++) {
         String line = scan.nextLine();
         String sub = "";
         if (line.length() >= 11) {
            sub = line.substring(0, 10).toLowerCase();
            if (sub.equals("simon says")) {
               System.out.println(line.substring(11));
            }
            else {
                System.out.println();
            }
         }
         else {
                System.out.println();
         }
      }
   }
}