/*
Rating: ~ 1.9 / 10
Link: https://open.kattis.com/problems/baconeggsandspam
*/

import java.io.*;
import java.util.*;

public class baconeggsandspam {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int customers = Integer.parseInt(scan.nextLine());
    while (customers != 0) {
      HashMap<String,ArrayList<String>> storage = new HashMap<String, ArrayList<String>>();
      for (int x = 0; x < customers; x++) {
        String[] line = scan.nextLine().split(" ");
        for (int y = 1; y < line.length; y++) {
          ArrayList<String> here = new ArrayList<String>();
          if (storage.containsKey(line[y])) {
            here = storage.get(line[y]);
          }
          here.add(line[0]);
          storage.put(line[y], here);
        }
      }
      Set<String> keys = storage.keySet();
      ArrayList<String> keys2 = new ArrayList<String>(keys);
      Collections.sort(keys2);
      for(String key: keys2) {
        ArrayList<String> temp = storage.get(key);
        Collections.sort(temp);
        System.out.print(key + " ");
        for (String cust: temp) {
          System.out.print(cust + " ");
        }
        System.out.println();
      }
      System.out.println();
      customers = Integer.parseInt(scan.nextLine());
   }
  }
}
