import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class B2 {
    static void solve() {
        int n = readInt();
        int[] w = new int[n];
        int[] h = new int[n];
        for (int i = 0; i < n; i++) {
            w[i] = readInt();
            h[i] = readInt();
        }
        doSolve(n, w, h);
    }

    private static void doSolve(int n, int[] w, int[] h) {
        long pairs = 0;
        Map<Integer, Integer> dimension_to_count = new HashMap<>(n, 1);
        Map<Long, Integer> dimensions_to_count = new HashMap<>(n, 1);
        for (int i = 0; i < n; i++) {
            if (w[i] == h[i]) {
                int w_count = dimension_to_count.getOrDefault(w[i], 0);
                dimension_to_count.put(w[i], w_count + 1);
                pairs += w_count;
            } else {
                long min = Math.min(w[i], h[i]);
                long max = Math.max(w[i], h[i]);
                long key = min << 32 | max;
                int exact = dimensions_to_count.getOrDefault(key, 0);
                dimensions_to_count.put(key, exact + 1);
                int w_count = dimension_to_count.getOrDefault(w[i], 0);
                dimension_to_count.put(w[i], w_count + 1);
                int h_count = dimension_to_count.getOrDefault(h[i], 0);
                dimension_to_count.put(h[i], h_count + 1);
                pairs += w_count + h_count - exact;
            }
        }
        out.println(pairs);
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

    static int gcd(int a, int b) {
        while (b > 0) {
            a %= b;
            b = swap(a, a = b);
        }
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
