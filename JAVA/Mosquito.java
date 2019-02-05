import java.util.*;

public class Mosquito {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		while (scan.hasNextLine()) {
			String[] line = scan.nextLine().split(" ");
			int mosquito = Integer.parseInt(line[0]);
			int pupae = Integer.parseInt(line[1]);
			int larvae = Integer.parseInt(line[2]);
			int eggs = Integer.parseInt(line[3]);
			int survivalL = Integer.parseInt(line[4]);
			int survivalP = Integer.parseInt(line[5]);
			int weeks = Integer.parseInt(line[6]);
			int sunday = 0;

			while (sunday < weeks) {
				int newMosquitos = 0;
				int newPupae = 0;
				int newLarvae = 0;
				if (survivalP != 0) {
					newMosquitos = pupae / survivalP;
				}
				if (survivalL != 0) {
					newPupae = larvae / survivalL;
				}
				newLarvae = mosquito * eggs;
				mosquito = newMosquitos;
				pupae = newPupae;
				larvae = newLarvae;
				sunday++;
			}
			System.out.println(mosquito);
		}
	}
}