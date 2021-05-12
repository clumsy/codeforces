import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class E {
    static void solve() {
        int t = readInt();
        while (t-- > 0) {
            int n = readInt();
            String s = readString();
            doSolve(n, s);
        }
    }

    private static void doSolve(int n, String s) {
        long total = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '*') {
                total++;
            }
        }
        long answer = 0;
        long left = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '*') {
                left++;
                continue;
            }
            answer += Math.min(left, total - left);
        }
        out.println(answer);
    }

    //////////////////////// Template ////////////////////////
    static int readInt() {
        return Integer.parseInt(readString());
    }

    static long readLong() {
        return Long.parseLong(readString());
    }

    static String readString() {
        while (tok == null || !tok.hasMoreTokens()) {
            try {
                tok = new StringTokenizer(in.readLine());
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        return tok.nextToken();
    }

    static int swap(int a, int b) { // usage: y = swap(x, x=y);
        return a;
    }

    static BufferedReader in;
    static PrintWriter out;
    static StringTokenizer tok;

    public static void main(String[] arg) {
        in = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(System.out);
        solve();
        out.close();
    }
}
