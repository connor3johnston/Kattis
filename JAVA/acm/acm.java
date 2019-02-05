/*
Rating: ~ 1.5 / 10
Link: https://open.kattis.com/problems/acm
*/

import java.io.*;
import java.util.*;

public class acm {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    String check = scan.nextLine();
    int total_problems = 0;
    int total_time = 0;
    HashMap<String, Integer> incorrect = new HashMap<String, Integer>();
    while (!check.equals("-1")) {
      String[] split_ = check.split(" ");
      int time = Integer.parseInt(split_[0]);
      String problem = split_[1];
      String solution = split_[2];
      if (solution.equals("right")) {
        if (incorrect.containsKey(problem)) {
          total_time += incorrect.get(problem);
          incorrect.remove(problem);
        }
        total_time += time;
        total_problems++;
      }
      else {
        int add = 20;
        if (incorrect.containsKey(problem)) {
          add += incorrect.get(problem);
        }
        incorrect.put(problem, add);
      }
      check = scan.nextLine();
    }
    System.out.println(total_problems + " " + total_time);
  }
}
