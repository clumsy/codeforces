import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class B {
    static void solve() {
        int t = readInt();
        while (t-- > 0) {
            String s = readString();
            doSolve(s);
        }
    }

    private static void doSolve(String s) {
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) == '0') {
                left++;
                continue;
            }
            if (s.charAt(right) == '1') {
                right--;
                continue;
            }
            boolean removed = false;
            if (s.charAt(left + 1) != '1') {
                left++;
                removed = true;
            }
            if (s.charAt(right - 1) != '0') {
                right--;
                removed = true;
            }
            if (!removed) {
                out.println("NO");
                return;
            }
        }
        out.println("YES");
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
