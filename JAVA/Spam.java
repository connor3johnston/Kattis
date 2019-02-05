
import java.util.Scanner;

public class Spam {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      String line = scan.nextLine();
      double whitespace = 0;
      double lowercase = 0;
      double uppercase = 0;
      double symbols = 0;
   
      for (int x = 0; x < line.length(); x++) {
         char letter = line.charAt(x);
         if (letter == '_') {
            whitespace++;
         }
         else if (letter > 64 && letter < 91) {
            uppercase++;
         }
         else if (letter > 96 && letter < 123) {
            lowercase++;
         }
         else {
            symbols++;
         }
      }
      System.out.println(whitespace/(line.length()));
      System.out.println(lowercase/(line.length()));
      System.out.println(uppercase/(line.length()));
      System.out.println(symbols/(line.length()));		
   
   }
}
