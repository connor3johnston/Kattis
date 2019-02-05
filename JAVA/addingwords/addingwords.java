/*
Rating: ~ 4.2 / 10
Link: https://open.kattis.com/problems/addingwords
*/

import java.util.Scanner;
import java.util.HashMap;

public class addingwords {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    HashMap<String, Integer> values = new HashMap<String, Integer>();

    while (scan.hasNext()) {
      String[] line = scan.nextLine().split(" ");
      if (line[0].equals("clear")) {
        values.clear();
      }
      else if (line[0].equals("calc")) {
        System.out.println(calc(values, line));
      }
      else {
        values.put(line[1], Integer.parseInt(line[2]));
      }
    }
  }

  public static String calc(HashMap<String, Integer> values, String[] calculation) {
    int answer;
    String output = "";
    if (!values.containsKey(calculation[1])) {
      for (int x = 1; x < calculation.length; x++) {
        output += calculation[x] + " ";
      }
      output += "unknown";
      return output;
    }
    answer = values.get(calculation[1]);
    output = calculation[1] + " ";
    for (int x = 2; x < calculation.length; x+=2) {
      if (calculation[x].equals("+")) {
        if (!values.containsKey(calculation[x+1])) {
          for (int y = x; y < calculation.length; y++) {
            output += calculation[y] + " ";
          }
          output += "unknown";
          return output;
        }
        answer += values.get(calculation[x+1]);
        output += "+ " + calculation[x+1] + " ";
      }
      else if (calculation[x].equals("-")) {
        if (!values.containsKey(calculation[x+1])) {
          for (int y = x; y < calculation.length; y++) {
            output += calculation[y] + " ";
          }
          output += "unknown";
          return output;
        }
        answer -= values.get(calculation[x+1]);
        output += "- " + calculation[x+1] + " ";
      }
      else {
        output += "= " + getKeyFromValue(values, answer);
        break;
      }
    }
    return output;
  }

  public static String getKeyFromValue(HashMap<String, Integer> values, int answer) {
    for (String check: values.keySet()) {
      if (values.get(check).equals(answer)) {
        return check;
      }
    }
    return "unknown";
  }
}
