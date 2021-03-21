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
            int k1 = readInt();
            int k2 = readInt();
            int w = readInt();
            int b = readInt();
            doSolve(n, k1, k2, w, b);
        }
    }

    private static void doSolve(int n, int k1, int k2, int w, int b) {
        int whites = k1 + k2;
        if (2*w <= whites && 2*b <= 2*n - whites) {
            out.println("YES");
        } else {
            out.println("NO");
        }
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
