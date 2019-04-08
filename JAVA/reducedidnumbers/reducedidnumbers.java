/*
Rating: ~ 3.7 / 10
Link: https://open.kattis.com/problems/reducedidnumbers
*/

import java.io.*;
import java.util.*;

public class reducedidnumbers {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int numbers = Integer.parseInt(scan.nextLine());
    int maxSin = (int) Math.pow(10, 6);
    HashSet<Integer> store = new HashSet<Integer>();

    for (int x = 0; x < numbers; x++) {
      store.add(Integer.parseInt(scan.nextLine()));
    }

    for (int y = 1; y < maxSin; y++) {
      HashSet<Integer> check = new HashSet<Integer>();
      boolean found = true;
      for (int here: store) {
        int temp = here % y;
        if (check.contains(temp)) {
          found = false;
          break;
        }
        check.add(temp);
      }
      if (found) {
        System.out.println(y);
        break;
      }
    }
  }
}
