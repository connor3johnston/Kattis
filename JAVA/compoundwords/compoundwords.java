/*
Rating: ~ 1.8 / 10
Link: https://open.kattis.com/problems/compoundwords
*/

import java.io.*;
import java.util.*;

public class compoundwords {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		ArrayList<String> words = new ArrayList<String>();
		TreeSet<String> sorted = new TreeSet<String>();
		while (scan.hasNext()) {
			String next = scan.next();
			words.add(next);
		}
		for (int x = 0; x <  words.size(); x++) {
			for (int y = 0; y < words.size(); y++) {
				if (x == y) {
					continue;
				}
				String here = words.get(y);
				String there = words.get(x);
				String combine = here + there;
				sorted.add(combine);
			}
		}

		for (String h: sorted) {
			System.out.println(h);
		}
	}
}
