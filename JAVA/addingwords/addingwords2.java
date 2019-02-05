import java.util.*;

public class addingwords2 {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    HashMap definitions = new HashMap();
    HashMap solutions = new HashMap();
    while (scan.hasNextLine()) {
      String line = scan.nextLine();
      String[] line2 = line.split(" ");
      if (line[0] == "clear") {
        definitions = new HashMap();
        solutions = new HashMap();
        continue;
      }
      if (line[0] == "def") {
        definitions.put(line[1], Integer.parseInt(line[2]);
        solutions.put(Integer.parseInt(line[2]), line[1]);
        continue;
      }
      if (definitions.get(line[1]) == null) {
        System.out.println(line2 + " unknown");
        continue;
      }
      int answer = definitions.get(line[1]);
      boolean valid = true;
      for (int x = 2; x < line.length()-2; x += 2) {
        char sign = line[x].charAt(0);
        if (definitions.get(line[x+1]) == null) {
          System.out.println(line2 + " unknown");
          valid = false;
          break;
        }
        if (sign == '+') {
          answer += definitions.get(line[x+1]);
        }
        else {
          answer -= definitions.get(line[x+1]);
        }
      }
      if (valid) {
        if (solutions.get(answer) == null) {
          System.out.println(line2 + " unknown");
          continue;
        }
        System.out.println(line2 + " "+ solutions.get(answer));
      }
    }
  }
}
