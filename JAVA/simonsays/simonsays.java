/*
Rating: ~ 1.6 / 10
Link: https://open.kattis.com/problems/acm2
*/

import java.util.Scanner;

public class simonsays {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int cases = scan.nextInt();
		scan.nextLine();
		for (int x = 0; x < cases; x++) {
			String line  = scan.nextLine();
			if (line.length() >= 10 && line.substring(0, 10).equals("Simon says")) {
				System.out.println(line.substring(10));
			}
		}
	}
}
