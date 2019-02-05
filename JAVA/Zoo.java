import java.util.Scanner;
import java.util.HashMap;
import java.util.Arrays;

public class Zoo {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int lists = 0;
   
      int animals = Integer.parseInt(scan.nextLine());
      while (animals != 0) {
         lists++;
         HashMap<String, Integer> zoo = new HashMap<String, Integer>();
         for (int x = 0; x < animals; x++) {
            String[] line = scan.nextLine().split(" ");
            String animal = line[line.length - 1].toLowerCase();
            if (zoo.containsKey(animal)) {
               int sum = 1 + zoo.get(animal);
               zoo.put(animal, sum);
            }
            else {
               zoo.put(animal, 1);
            }
         }
         Object[] keys = zoo.keySet().toArray();
         Arrays.sort(keys);
         System.out.println("List " + lists + ":");
         for (Object key: keys) {
            System.out.println(key + " | " + zoo.get(key));
         }
         animals = Integer.parseInt(scan.nextLine());
      }
   }
}