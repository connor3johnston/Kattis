/*
Rating: ~ 2.1 / 10
Link: https://open.kattis.com/problems/whatdoesthefoxsay
*/

import java.util.*;

public class whatdoesthefoxsay {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int cases = Integer.parseInt(scan.nextLine());

      for (int x = 0; x < cases; x++) {
         ArrayList<String> map = new ArrayList<String>();
         String[] line = scan.nextLine().split(" ");
         String next = scan.nextLine();
         while (!next.equals("what does the fox say?")) {
            String[] split = next.split(" goes ");
            String sound = split[1];
            map.add(sound);
            next = scan.nextLine();
         }
         String output = "";
         for (String key: line) {
            if (!map.contains(key)) {
               output += (key + " ");
            }
         }
         System.out.println(output);
      }
   }
}
