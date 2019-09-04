/*
Rating: ~ 1.2 / 10
Link: https://open.kattis.com/problems/dicecup
*/

import java.util.Scanner;

public class dicecup {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);

		int a = scan.nextInt();
		int b = scan.nextInt();

		int end = Math.max(a,b) + 1;
		int start = Math.min(a,b) + 1;

		for (int x = start; x <= end; x++) {
			System.out.println(x);
		}
	}
}
