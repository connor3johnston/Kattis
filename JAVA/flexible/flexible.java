/*
Rating: ~ 1.8 / 10
Link: https://open.kattis.com/problems/flexible
*/

import java.io.*;
import java.util.*;

public class flexible {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		TreeSet<Integer> set = new TreeSet<Integer>();
		int width = scan.nextInt();
		set.add(width);
		int partitions = scan.nextInt();
		int[] keep = new int[partitions];
		for (int x = 0; x < partitions; x++) {
			keep[x] = scan.nextInt();
		}
		for (int y = 0; y < partitions; y++) {
			int here = keep[y];
			set.add(here);
			set.add(width - here);
			for (int z = 0; z < partitions; z++) {
				if (y == z) {
					continue;
				}
				int there = keep[z];
				set.add(Math.abs(here - there));
			}
		}
		for (int a: set) {
			System.out.print(a + " ");
		}
	}
}
