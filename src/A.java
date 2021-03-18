import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class A {
    static void solve() {
        int t = readInt();
        while (t-- > 0) {
            int n = readInt();
            int k = readInt();
            String s = readString();
            if (doSolve(n, k, s, 0)) {
                out.println("YES");
            } else {
                out.println("NO");
            }
        }
    }

    private static boolean doSolve(int n, int k, String s, int start) {
        if (k == 0) {
            return true;
        }
        for (int i = 0, end = (n - 1)/2 - k + 1; i < end; i++) {
            int offset = start + i;
            if (s.charAt(offset) == s.charAt(s.length() - offset - 1)) {
                if (doSolve(n - 2*(i + 1), k - 1, s, offset + 1)) {
                    return true;
                }
            } else {
                return false;
            }
        }
        return false;
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
