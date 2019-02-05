/*
Rating: ~ 2.5 / 10
Link: https://open.kattis.com/problems/acm2
*/

import java.util.*;

public class acm2 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		TreeSet<Integer> set = new TreeSet<Integer>();
		int probs = scan.nextInt();
		int index = scan.nextInt();
		int time = 0;
		int penalty = 0;
		int solve = 0;
		boolean check = true;
		for (int x = 0; x < probs; x++) {
			int cur = scan.nextInt();
			if (x == index && cur > 300) {
				check = false;
			}
			if (x == index && cur <= 300) {
				time += cur;
				penalty += cur;
				solve++;
				continue;
			}
			set.add(cur);
		}
		if (check) {
			for (int here: set) {
				if (time + here > 300) {
					break;
				}
				time += here;
				solve++;
				penalty += time;
			}
		}
		System.out.println(solve + " " + penalty);
	}
}
