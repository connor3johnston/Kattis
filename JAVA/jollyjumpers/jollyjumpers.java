/*
Rating: ~ 3.2 / 10
Link: https://open.kattis.com/problems/acm2
*/

import java.util.*;

public class jollyjumpers {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		while (scan.hasNextLine()) {
			String[] line = scan.nextLine().split(" ");
			int nums = line.length;
			if (nums == 2) {
				System.out.println("Jolly");
				continue;
			}
			int[] lineNums = new int[nums - 1];
			int values = 0;
			int highest = Integer.MIN_VALUE;
			for (int x = 0; x < nums; x++) {
				if (x == 0) {
					values = Integer.parseInt(line[0]);
				}
				else {
					lineNums[x - 1] = Integer.parseInt(line[x]);
					if (Math.abs(lineNums[x - 1]) > highest) {
						highest = Math.abs(lineNums[x-1]);
					}
				}
			}
			HashSet<Integer> set = new HashSet<Integer>();
			for (int y = 1; y < values; y++) {
				int right = lineNums[y];
				int left = lineNums[y-1];
				int dif = Math.abs(right - left);
				if (dif > 0 && dif < highest) {
					set.add(dif);
				}
			}
			if (set.size() == nums -2) {
				System.out.println("Jolly");
			}
			else {
				System.out.println("Not jolly");
			}
		}
	}
}
