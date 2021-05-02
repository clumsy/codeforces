import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.BitSet;
import java.util.List;
import java.util.StringTokenizer;

public class E {
    static void solve() {
        int t = readInt();
        while (t-- > 0) {
            int n = readInt();
            int l = readInt();
            int r = readInt();
            int s = readInt();
            doSolve(n, l, r, s);
        }
    }

    private static void doSolve(int n, int l, int r, int s) {
        int need = r - l + 1;
        if (need > n) { // we don't have enough numbers
            out.println(-1);
            return;
        }
        BitSet used = new BitSet(n + 1);
        if (!calculate(n, need, s, used)) {
            out.println(-1);
            return;
        }
        BitSet other = new BitSet();
        other.or(used);
        while (l-- > 1) {
            int i = other.nextClearBit(1);
            other.set(i);
            out.print(i);
            out.print(' ');
        }
        for (int i = used.nextSetBit(1); i != -1 ; i = used.nextSetBit(i + 1)) {
            out.print(i);
            out.print(' ');
        }
        while (r++ < n) {
            int i = other.nextClearBit(1);
            other.set(i);
            out.print(i);
            out.print(' ');
        }
        out.println();
    }

    private static boolean calculate(int n, int count, int s, BitSet used) {
        if (count == 0) {
            return s == 0;
        }
        int max = ((n - count + 1) + n) * count / 2; // max sum using count numbers
        if (max < s) {
            return false;
        }
        int min = (1 + (count - 1))*(count - 1)/2; // min sum using count-1 numbers
        int remains = s - min;
        if (remains < count) {
            return false;
        }
        int next = used.previousClearBit(Math.min(n, remains));
        if (next <= count - 1) { // check if we had to use the numbers that form min sum
            return false;
        }
        used.set(next);
        return calculate(n, count - 1, s - next, used);
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
