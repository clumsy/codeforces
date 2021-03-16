import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class C {
    static void solve() {
        int n = readInt();
        String[] names = new String[n];
        for (int i = 0; i < n; i++) {
            names[i] = readString();
        }
        doSolve(n, names);
    }

    private static void doSolve(int n, String[] names) {
        Map<String, Integer> nameCounts = new HashMap<>(n, 1);
        for (int i = 0; i < n; i++) {
            Integer previous = nameCounts.get(names[i]);
            if (previous == null) {
                out.println("OK");
                previous = 0;
            } else {
                String newName = names[i] + previous;
                out.println(newName);
            }
            nameCounts.put(names[i], previous + 1);
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
