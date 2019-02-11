/*
Rating: ~ 2.0 / 10
Link: https://open.kattis.com/problems/armystrengthhard
*/

import java.io.*;
import java.util.*;

public class armystrengthhard {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int cases = Integer.parseInt(scan.nextLine());
    for (int x = 0; x < cases; x++) {
      scan.nextLine();
      String[] line = scan.nextLine().split(" ");
      int god = Integer.parseInt(line[0]);
      int mega = Integer.parseInt(line[1]);
      String[] gArm = scan.nextLine().split(" ");
      String[] mArm = scan.nextLine().split(" ");
      int[] gArmy = new int[god];
      int[] mArmy = new int[mega];
      for (int a = 0; a < god; a++) {
        gArmy[a] = Integer.parseInt(gArm[a]);
      }
      for (int y = 0; y < mega; y++) {
        mArmy[y] = Integer.parseInt(mArm[y]);
      }
      Arrays.sort(mArmy);
      Arrays.sort(gArmy);
      int m = mArmy[mega-1];
      int g = gArmy[god-1];
      if (g >= m) {
        System.out.print("Godzilla");
      }
      else {
        System.out.print("MechaGodzilla");
      }
      System.out.println();
    }
  }
}
