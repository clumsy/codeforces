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
            int[] a = new int[n + 2];
            for (int i = 0; i < a.length; i++) {
                a[i] = readInt();
            }
            doSolve(a);
        }
    }

    private static void doSolve(int[] a) {
        long sum = 0;
        Map<Integer, Integer> nums = new HashMap<>(a.length, 1); 
        for (int i = 0; i < a.length; i++) {
            sum += a[i];
            nums.put(a[i], i);
        }
        for (int i = 0; i < a.length; i++) {
            long twice = sum - a[i];
            int half = (int) twice/2;
            Integer half_index = nums.get(half);
            if (twice == 2*half && half_index != null && half_index != i) {
                for (int j = 0; j < a.length; j++) {
                    if (j != i && j != half_index) {
                        out.print(a[j]);
                        out.print(' ');
                    }
                }
                out.println();
                return;
            }
        }
        out.println(-1);
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
