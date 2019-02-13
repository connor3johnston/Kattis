/*
Rating: ~ 1.6 / 10
Link: https://open.kattis.com/problems/server
*/

import java.io.*;
import java.util.*;

public class server {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int tasks = scan.nextInt();
		int max = scan.nextInt();
		int track = 0;
		int count = 0;
		for (int x = 0; x <  tasks; x++) {
			int next = scan.nextInt();
			if (track + next > max) {
				break;
			}
			track += next;
			count++;
		}
		System.out.println(count);
	}
}
