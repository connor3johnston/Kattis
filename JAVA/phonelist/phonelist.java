/*
Rating: ~ 4.1 / 10
Link: https://open.kattis.com/problems/acm2
*/

import java.util.HashMap;
import java.util.Set;
import java.util.Set;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class phonelist {
   public static void main(String[] args) throws IOException {
      BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
      int cases = Integer.parseInt(scan.readLine());
      for (int x = 0; x < cases; x++) {
         boolean con = true;
         int numbers = Integer.parseInt(scan.readLine());
         HashMap<String, String> catalog = new HashMap<String, String>();
         for (int y = 0; y < numbers; y++) {
            String number = scan.readLine();
            catalog.put(number, number);
         }
         if (cons(catalog)) {
            System.out.println("YES");
         }
         else {
            System.out.println("NO");
         }
      }
   }

   public static boolean cons(HashMap catalog) {
      Set<String> set = catalog.keySet();
      for (String s: set) {
         String[] split = s.split("");
         String output = "";
         for (int x = 0; x < split.length; x++) {
            output += split[x];
            if (catalog.containsKey(output) && !output.equals(s)) {
               return false;
            }
         }
      }
      return true;
   }
}
