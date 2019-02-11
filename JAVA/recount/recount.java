/*
Rating: ~ 2.1 / 10
Link: https://open.kattis.com/problems/recount
*/

import java.util.Scanner;
import java.util.HashMap;
import java.util.Set;

public class recount {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		HashMap<String, Integer> votes = new HashMap<String, Integer>();
		String input;
		Set<String> ballot;
		while (scan.hasNextLine()) {
			input = scan.nextLine();
			if (input.equals("***")) {
				break;
			}
			if (votes.containsKey(input)) {
				int vote = votes.get(input);
				vote++;
				votes.put(input, vote);
			}
			else {
				int vote = 1;
				votes.put(input, vote);
			}
		}
		ballot = votes.keySet();
		int track = -1;
		String winner = "";
		for (String name: ballot) {
			if (votes.get(name) > track) {
				track = votes.get(name);
				winner = name;
			}
		}
		votes.remove(winner);
		if (votes.containsValue(track)) {
			System.out.println("Runoff!");
		}
		else {
			System.out.println(winner);
		}
	}
}
