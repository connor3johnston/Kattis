/*
Rating: ~ 2.7 / 10
Link: https://open.kattis.com/problems/game
*/

import java.io.*;

public class Guess {
	public static void main(String[] args) throws IOException {
		BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
		int low = 1;
		int high = 1000;
		for (int x = 1; x <= 10; x++) {
			int guess = low + (high - low + 1)/2;
			System.out.println(guess);
			System.out.flush();
			String input = scan.readLine();
			if (input.equals("lower")) {
				high = guess - 1;
			}
			else if (input.equals("higher")) {
				low = guess + 1;
			}
			else {
				break;
			}
		}
	}
}
