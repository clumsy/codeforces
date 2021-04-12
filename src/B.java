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
            char[][] grid = new char[n][n];
            for (int i = 0; i < n; i++) {
                String line = readString();
                for (int j = 0; j < n; j++) {
                    grid[i][j] = line.charAt(j);
                }
            }
            doSolve(n, grid);
        }
    }

    private static void doSolve(int n, char[][] grid) {
        int x1 = -1;
        int y1 = -1;
        int x2 = -1;
        int y2 = -1;
        outer: for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '.') {
                    continue;
                }
                if (x1 < 0) {
                    x1 = i;
                    y1 = j;
                } else {
                    x2 = i;
                    y2 = j;
                    break outer;
                }
            }
        }
        if (x1 == x2) {
            x1 = (x1 + 1) % n;
            x2 = (x2 + 1) % n;
        } else if (y1 == y2) {
            y1 = (y1 + 1) % n;
            y2 = (y2 + 1) % n;
        } else {
            x1 = swap(x2, x2 = x1);
        }
        grid[x1][y1] = '*';
        grid[x2][y2] = '*';
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                out.print(grid[i][j]);
            }
            out.println();
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
