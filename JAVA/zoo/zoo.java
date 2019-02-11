/*
Rating: ~ 1.6 / 10
Link: https://open.kattis.com/problems/zoo
*/

import java.io.*;
import java.util.*;

public class zoo {
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
