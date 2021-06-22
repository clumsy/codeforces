import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class D {
    static void solve() {
        int t = readInt();
        while (t-- > 0) {
            doSolve(readInt(), readInt(), readInt());
        }
    }

    private static void doSolve(int a, int b, int k) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] {a, b, k});
        while (!queue.isEmpty()) {
            int[] current = queue.remove();
            int current_k = current[2];
            int first = current[0];
            int second = current[1];
            if (current_k == 0) {
                if (first == second) {
                    out.println("YES");
                    return;
                }
                continue;
            }
            if (first < second) { // make sure first is smaller
                first = swap(second, second = first);
            }
            if (first == 1) {
                continue;
            }
            for (int i = 2, max = (int) Math.sqrt(first); i <= max; i++) {
                if (first % i == 0) {
                    queue.add(new int[] {second, first/i, current_k - 1});
                }
            }
        }
        out.println("NO");
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
