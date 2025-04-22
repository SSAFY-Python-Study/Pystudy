import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String st = sc.nextLine().trim(); // 앞뒤 공백 제거!
		
		if (st.isEmpty()) {
			System.out.println(0); // 아무 단어도 없음!
			return;
		}

		String[] stArr = st.split("\\s+"); // 하나 이상의 공백을 기준으로 split
		System.out.println(stArr.length);
	}
}