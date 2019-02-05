import java.util.Scanner;
import java.util.HashMap;
import java.text.DecimalFormat;
import java.math.BigInteger;

public class AnagramCounting {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      DecimalFormat df = new DecimalFormat("##0");
      while (scan.hasNextLine()) {
         HashMap<String, Long> map = new HashMap<String, Long>();
         String[] line = scan.nextLine().split("");
         for (int x = 0; x < line.length; x++) {
            String key = line[x];
            if (map.containsKey(key)) {
               long add = map.get(key) + 1;
               map.put(key, add);
            }
            else {
               map.put(key, (long) 1);
            }
         }
         BigInteger combos = factorial(BigInteger.valueOf(line.length));
         for (String key: map.keySet()) {
            BigInteger check = BigInteger.valueOf(map.get(key));
            if (check.compareTo(BigInteger.valueOf(1)) == 0) {
               continue;
            }
            else {
               combos = combos.divide(factorial(check));
            }
         }
         System.out.println(combos);
      }
   }

   public static BigInteger factorial (BigInteger n) {
      if (n.compareTo(BigInteger.valueOf(1)) == 0) {
         return BigInteger.valueOf(1);
      }
      else {
         return n.multiply(factorial(n.subtract(BigInteger.valueOf((long) 1))));
      }
   }
}