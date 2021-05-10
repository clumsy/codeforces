import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class D {
    static void solve() {
        int t = readInt();
        while (t-- > 0) {
            int n = readInt();
            int[] a = new int[n];
            int i = 0;
            while (i < n) {
                a[i++] = readInt();
            }
            doSolve(a);
        }
    }

    private static void doSolve(int[] a) {
        Map<Integer, Integer> numbers = new HashMap<>();
        long count = 0;
        for (int i = 0; i < a.length; i++) {
            Integer matches = numbers.get(a[i] - i);
            if (matches == null) {
                matches = 0;
            }
            count += matches;
            numbers.put(a[i] - i, matches + 1);
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
