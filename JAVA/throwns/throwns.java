/*
Rating: ~ 3.0 / 10
Link: https://open.kattis.com/problems/throwns
*/

import java.io.*;
import java.util.*;

public class throwns {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int students = scan.nextInt();
    int numcommands = scan.nextInt();
    scan.nextLine();
    String[] commands = scan.nextLine().split(" ");
    int index = 0;
    int position = 0;
    Stack<Integer> stack = new Stack<Integer>();
    while (index < commands.length) {
      String current = commands[index];
      if (current.equals("undo")) {
        index++;
        int undo = Integer.parseInt(commands[index]);
        for (int x = 0; x < undo; x++) {
          int back = 0 - stack.pop();
          position = move(students, position, back);
        }
      }
      else {
        int moves = Integer.parseInt(current);
        stack.push(moves);
        position = move(students, position, moves);
      }
      index++;
    }
    System.out.println(position);
  }

  public static int move(int students, int position, int moves) {
    int newposition = position + moves;
    while (newposition >= students) {
      newposition -= students;
    }
    while (newposition < 0) {
      newposition += students;
    }
    return newposition;
  }
}
