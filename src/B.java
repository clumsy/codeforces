import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class B {
    static void solve() {
        int d = readInt();
        int sumTime = readInt();
        int[] minTime = new int[d];
        int[] maxTime = new int[d];
        for (int i = 0; i < d; i++) {
            minTime[i] = readInt();
            maxTime[i] = readInt();
        }
        doSolve(d, sumTime, minTime, maxTime);
    }

    private static void doSolve(int d, int sumTime, int[] minTime, int[] maxTime) {
        int[] hours = new int[d];

        // make sure we satisfy minimum
        for (int i = 0; i < d; i++) {
            if (sumTime <= 0) {
                break;
            }
            if (sumTime < minTime[i]) {
                out.println("NO");
                return;
            }
            sumTime -= minTime[i];
            hours[i] += minTime[i];
        }

        // try to fix max possible in the remaining
        for (int i = 0; i < d; i++) {
            if (sumTime <= 0) {
                break;
            }
            int studied = Math.min(sumTime, maxTime[i] - hours[i]);
            sumTime -= studied;
            hours[i] += studied;
        }

        if (sumTime <= 0) {
            out.println("YES");
            for (int i = 0; i < d; i++) {
                out.print(hours[i]);
                out.print(' ');
            }
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
