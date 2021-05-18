import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class C {
    static void solve() {
        int t = readInt();
        while (t-- > 0) {
            int n = readInt();
            int m = readInt();
            int[] x = new int[n];
            for (int i = 0; i < n; i++) {
                x[i] = readInt();
            }
            char[] d = new char[n];
            for (int i = 0; i < n; i++) {
                d[i] = readString().charAt(0);
            }
            doSolve(n, m, x, d);
        }
    }

    private static void doSolve(int n, int m, int[] x, char[] d) {
        int[] e = new int[n];
        int remains = n;
        Map<Integer, List<Integer>> coordinate_to_robots = new HashMap<>();
        int time = 0;
        while (remains > 1) {
            time++;
            coordinate_to_robots.clear();
            for (int i = 0; i < n; i++) {
                if (e[i] > 0) {
                    continue; // exploded
                }
                if (d[i] == 'L' && --x[i] == 0) {
                    d[i] = 'R';
                }
                if (d[i] == 'R' && ++x[i] == m) {
                    d[i] = 'L';
                }
                List<Integer> robots = coordinate_to_robots.get(x[i]);
                if (robots == null) {
                    robots = new ArrayList<>();
                    coordinate_to_robots.put(x[i], robots);
                }
                robots.add(i);
            }
            for (int coordinate : coordinate_to_robots.keySet()) {
                List<Integer> robots = coordinate_to_robots.get(coordinate);
                if (robots.size() > 1) {
                    remains -= robots.size();
                    for (int robot : robots) {
                        e[robot] = time;
                    }
                }
            }
        }
        for (int exploded : e) {
            out.print(exploded > 0 ? exploded : -1);
            out.print(' ');
        }
        out.println();
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
