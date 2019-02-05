import java.util.*;

public class Chewbacca {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      long n = scan.nextLong();
      long k = scan.nextLong();
      long q = scan.nextLong();
      ArrayList<HashSet<Long>> map = new ArrayList<HashSet<Long>>();
      map.add(null);
      long track = 2;
      long parent = 1;
      while (track <= n) {
         HashSet<Long> children = new HashSet<Long>();
         long count = 0;
         while (count <  k && track <= n) {
            children.add(track);
            track++;
            count++;
         }
         map.add(children);
         parent++;
      }
      for (int x = 0; x < q; x++) {
         long val1 = scan.nextLong();
         long val2 = scan.nextLong();
         ArrayList<Long> path1 = new ArrayList<Long>();
         ArrayList<Long> path2 = new ArrayList<Long>();
         long parent1 = val1;
         long parent2 = val2;
         boolean end1 = false;
         boolean end2 = false;
         path1.add(parent1);
         while (!end1) {
            for (HashSet<Long> here: map) {
               if (parent1 == 1) {
                  end1 = true;
                  break;
                  
               }
               if (here == null) {
                  continue;
               }
               if(here.contains(parent1)) {
                  parent1 = map.indexOf(here);
                  path1.add(parent1);
               
                  break;
               }
            }
         }	
         path2.add(parent2);
         while (!end2) {
            for (HashSet<Long> here: map) {
               if (parent2 == 1) {
                  end2 = true;
                  break;
                  
               }
               if (here == null) {
                  continue;
               }
               if(here.contains(parent2)) {
                  parent2 = map.indexOf(here);
                  path2.add(parent2);
               
                  break;
               }
            }
         }
         boolean equal = false;
         ArrayList<Long> larger;
         ArrayList<Long> smaller;
         if (path1.size() >= path2.size()) {
            larger = path1;
            smaller = path2;
         }
         else {
            larger = path2;
            smaller = path1;
         }
         int point = Math.abs(path1.size() - path2.size());
         int index = 0;
         long moves = point;
         while (!equal) {
            if (larger.get(index + point).equals(smaller.get(index))) {
               equal = true;
               break;
            }
            moves += 2;
            index++;
         }
         System.out.println(moves);					    
      }
   }
}