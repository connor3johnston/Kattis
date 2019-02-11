/*
Rating: ~ 1.3 / 10
Link: https://open.kattis.com/problems/apaxiaaans
*/

import java.io.*;
import java.util.*;

public class apaxiaaans {
  public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String name = scan.nextLine();
		String out = "";
		for (int x = 1; x < name.length(); x++) {
			if (name.charAt(x - 1) != name.charAt(x)) {
				out += name.charAt(x-1);
			}
		}
		out += name.charAt(name.length() - 1);
		System.out.println(out);
  }
}
