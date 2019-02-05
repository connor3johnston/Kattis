/*
Rating: ~ 1.9 / 10
Link: https://open.kattis.com/problems/recipes
*/

import java.io.*;
import java.util.*;
import java.text.*;

public class recipes {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    DecimalFormat df = new DecimalFormat("#.0");
    int cases = Integer.parseInt(scan.nextLine());
    for (int x = 1; x <= cases; x++) {
      String[] instructions = scan.nextLine().split(" ");
      int ingredients = Integer.parseInt(instructions[0]);
      double mult = Double.parseDouble(instructions[2])/Double.parseDouble(instructions[1]);
      double[] percents = new double[ingredients];
      String[] names = new String[ingredients];
      double save = 0;
      for (int y = 0; y < ingredients; y++) {
        String[] line = scan.nextLine().split(" ");
        double check = Double.parseDouble(line[2]);
        if (check == 100) {
          save = Double.parseDouble(line[1]);
        }
        names[y] = line[0];
        percents[y] = check;
      }
      System.out.println("Recipe # " + x);
      for (int z = 0; z < ingredients; z++) {
        double calc = mult * save * (percents[z]/100);
        System.out.println(names[z] + " " + df.format(calc));
      }
      for(int p = 0; p < 40; p++) {
        System.out.print("-");
      }
      System.out.println();
    }
  }
}
