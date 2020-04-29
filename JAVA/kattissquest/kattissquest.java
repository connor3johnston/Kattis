/*
Rating: ~ 3.1 / 10
Link: https://open.kattis.com/problems/kattissquest
*/

import java.util.TreeMap;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Collections;

public class kattissquest {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    TreeMap<Integer, PriorityQueue<Integer>> map = new TreeMap<>();

    int cases = Integer.parseInt(scan.nextLine());
    for (int i = 0; i < cases; i++) {
      String[] line = scan.nextLine().split(" ");

      if (line[0].equals("add")) {
        int E = Integer.parseInt(line[1]);
        int G = Integer.parseInt(line[2]);

        if (!map.containsKey(E)) {
          map.put(E, new PriorityQueue<Integer>(Collections.reverseOrder()));
        }

        PriorityQueue<Integer> q = map.get(E);
        q.add(G);
        map.put(E, q);
      } else {
        int X = Integer.parseInt(line[1]);
        long out = 0;
        while (X > -1) {
          Integer key = map.floorKey(X);

          if (key == null) {
            System.out.println(out);
            break;
          }

          while (X - key > -1 && map.containsKey(key)) {
            PriorityQueue<Integer> gold = map.get(key);
            out += gold.poll();

            if (gold.isEmpty()) {
              map.remove(key);
            } else {
              map.put(key, gold);
            }

            X -= key;
          }
        }
      }
    }
  }
}
