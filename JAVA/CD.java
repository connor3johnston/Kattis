import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.io.IOException;

public class CD {
   public static void main(String[] args) throws IOException {
      BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
   	
      String[] line = scan.readLine().split(" ");
      int jack = Integer.parseInt(line[0]);
      int jill = Integer.parseInt(line[1]);
   
      while (jack != 0 && jill != 0) {
         HashSet<Integer> catalog = new HashSet<Integer>();
      
         int count = 0;
      
         for (int x = 0; x < jack; x++) {
            catalog.add(Integer.parseInt(scan.readLine()));
         }
      
         for (int y = 0; y < jill; y++) {
            if(catalog.contains(Integer.parseInt(scan.readLine()))) {
               count++;
            }
         }
      
         System.out.println(count);
         line = scan.readLine().split(" ");
         jack = Integer.parseInt(line[0]);
         jill = Integer.parseInt(line[1]);
      }
   }
}