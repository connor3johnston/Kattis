import java.util.Scanner;

public class Filip {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      String[] number1;
      String[] number2;
      String[] input = scan.nextLine().split(" ");
      
      number1 = input[0].split("");
      number2 = input[1].split("");
   
      String one = "";
      String two = "";
   
      for (int x = 2; x > -1; x--) {
         one += number1[x];
         two += number2[x];
      }
      
      int first = Integer.parseInt(one);
      int second = Integer.parseInt(two);
      
      if (first > second) {
         System.out.println(first);
      }
      else {
         System.out.print(second);
      }
   }
}