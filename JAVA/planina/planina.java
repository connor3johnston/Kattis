/*
Rating: ~ 1.3 / 10
Link: https://open.kattis.com/problems/planina
*/

import java.util.*;

public class planina {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int it = scan.nextInt();
		int cur = 3;
		for (int x = 1; x < it; x++) {
			cur = cur + cur - 1;
		}
		System.out.println(cur * cur);
	}
}
