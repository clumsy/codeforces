import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class B {
    static void solve() {
        int t = readInt();
        while (t-- > 0) {
            int n = readInt();
            int k = readInt();
            String s = readString();
            doSolve(n, k, s);
        }
    }

    private static void doSolve(int n, int k, String s) {
        int i = 0;
        StringBuilder modified = new StringBuilder(s);
        while (i < n && modified.charAt(i) != '*') {
            i++;
        }
        int count = 0;
        if (i < n) {
            modified.setCharAt(i, 'x');
            count++;
        }
        int j = n - 1;
        while (j > i && modified.charAt(j) != '*') {
            j--;
        }
        if (modified.charAt(j) == '*') {
            modified.setCharAt(j, 'x');
            count++;
        }
        for (i = i + k; i < j; i += k) {
            while (modified.charAt(i) != '*') {
                i--;
            }
            modified.setCharAt(i, 'x');
            count++;
        }
        out.println(count);
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
