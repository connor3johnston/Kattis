/*
Rating: ~ 1.5 / 10
Link: https://open.kattis.com/problems/aaah
*/

import java.io.*;
import java.util.*;

public class aaah {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		String jon = scan.nextLine();
		String doc = scan.nextLine();

		if (jon.length() >= doc.length()) {
			System.out.println("go");
		}
		else {
			System.out.println("no");
		}
	}
}
