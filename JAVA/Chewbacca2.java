import java.util.*;

public class Arithmetic {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      String here = scan.nextLine();
      long binary = Long.parseLong(here, 8);
      String output = Long.toHexString(binary);
      System.out.println(output.toUpperCase());
   	
   }
}
