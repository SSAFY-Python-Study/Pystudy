import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for(int tc = 1; tc <= 10; ++tc){
            int N = Integer.parseInt(br.readLine());
            LinkedList<String> cipherList = new LinkedList<>();
            // 원본 암호문 추가
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; ++i) {
                cipherList.add(st.nextToken());
            }

            int M = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            while(st.hasMoreTokens()){
                String cmd = st.nextToken();

                // I (삽입)
                if(cmd.equals("I")){
                    int x = Integer.parseInt(st.nextToken());
                    int y = Integer.parseInt(st.nextToken());
                    for (int i = 0; i < y; ++i) {
                        cipherList.add(x + i, st.nextToken());
                    }
                // D (삭제)
                } else if (cmd.equals("D")) {
                    int x = Integer.parseInt(st.nextToken());
                    int y = Integer.parseInt(st.nextToken());
                    for (int i = 0; i < y; i++) {
                        if (x < cipherList.size()) {
                            cipherList.remove(x);
                        }
                    }
                // A (추가)
                } else if (cmd.equals("A")) {
                    int y = Integer.parseInt(st.nextToken());
                    for (int i = 0; i < y; i++) {
                        cipherList.add(st.nextToken());
                    }
                }
            }

            // 결과 출력
            System.out.print("#" + tc + " ");
            for(int i = 0; i < 10 && i < cipherList.size(); ++i){
                System.out.print(cipherList.get(i) + " ");
            }
            System.out.println();
        }
        br.close();
    } // main
} // class
