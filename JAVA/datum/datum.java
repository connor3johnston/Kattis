/*
Rating: ~ 1.3 / 10
Link: https://open.kattis.com/problems/datum
*/

import java.io.*;
import java.util.*;

public class datum {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int[] days = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    HashMap<Integer, String> week = new HashMap<Integer,String>();
    week.put(1,"Thursday");
    week.put(2, "Friday");
    week.put(3, "Saturday");
    week.put(4, "Sunday");
    week.put(5, "Monday");
    week.put(6, "Tuesday");
    week.put(0, "Wednesday");
    int day = scan.nextInt();
    int month = scan.nextInt();
    int total = 0;
    for (int x = 0; x < month-1; x++) {
      total += days[x];
    }
    total += day;
    System.out.println(week.get(total%7));
  }
}
