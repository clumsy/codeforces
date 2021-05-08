import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.BitSet;
import java.util.StringTokenizer;

public class A {
    static void solve() {
        int t = readInt();
        while (t-- > 0) {
            int n = readInt();
            String s = readString();
            doSolve(s);
        }
    }

    private static void doSolve(String s) {
        BitSet seen = new BitSet(26);
        for (int i = 0; i < s.length(); i++) {
            int bitIndex = s.charAt(i) - 'A';
            if (i > 0 && (s.charAt(i - 1) != s.charAt(i) && seen.get(bitIndex))) {
                out.println("NO");
                return;
            }
            seen.set(bitIndex);
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
