import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class F2 {
    static void solve() {
        int n = readInt();
        SegmentTree st = new SegmentTree(n);
        int t = readInt();
        while (t-- > 0) {
            int k = readInt();
            doSolve(st, n, k);
        }
    }

    private static void doSolve(SegmentTree seg_tree, int n, int k) {
        int left = 1;
        int right = n;
        while (left < right) {
            int middle = left + (right - left)/2;
            int left_sum = real_query(left, middle) + seg_tree.query(left, middle);
            int left_zeroes = (middle - left + 1) - left_sum;
            if (k > left_zeroes) {
                k -= left_zeroes;
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        out.println("! " + left);
        out.flush();
        seg_tree.update(left, left, 1);
    }
    
    private static final class SegmentTree {
        private final int[] left;
        private final int[] right;
        private final int[] value;
        private final int[] delta;
        
        private SegmentTree(int n) {
            this.left  = new int[4*n + 1];
            this.right = new int[4*n + 1];
            this.value = new int[4*n + 1];
            this.delta = new int[4*n + 1];
            initialize(1, 1, n);
        }

        void initialize(int i, int l, int r) {
            left[i]  = l;
            right[i] = r;

            if (l == r) {
                return;
            }

            int m = l + (r - l)/2;
            initialize(2*i,   l, m);
            initialize(2*i+1, m+1, r);
        }

        void propagate(int i) {
            delta[2*i]   += delta[i];
            delta[2*i+1] += delta[i];
            delta[i] = 0;
        }

        void update(int i) {
            value[i] = (value[2*i] + delta[2*i]) + (value[2*i+1] + delta[2*i+1]);
        }

        void update(int i, int l, int r, int val) {
            if (r < left[i] || right[i] < l) {
                return;
            }
 
            if (l <= left[i] && right[i] <= r) {
                delta[i] += val;
                return;
            }

            propagate(i);

            update(2*i,   l, r, val);
            update(2*i+1, l, r, val);

            update(i);
        }

        // CircularRMQ!
        int query(int i, int l, int r) {
            if (r < left[i] || right[i] < l) {
                return 0;
            }

            if (l <= left[i] && right[i] <= r) {
                return value[i] + delta[i];
            }

            propagate(i);

            int left_result  = query(2*i,   l, r);
            int right_result = query(2*i+1, l, r);

            update(i);

            return left_result + right_result;
        }

        public void update(int l, int r, int val) {
            update(1, l, r, val);
        }

        public int query(int l, int r) {
            return query(1, l, r);
        }
    }

    private static final Map<Long, Integer> CACHE = new HashMap<>();
    
    private static long merge(long a, int b) {
        return a << 32 | b;
    }
    
    private static int real_query(int left, int right) {
        long key = merge(left, right);
        Integer cached = CACHE.get(key);
        if (cached != null) {
            return cached;
        }

        out.println("? " + left + " " + right);
        out.flush();
        int result = readInt();
        if (result == -1) {
            System.exit(0);
        }

        CACHE.put(key, result);
        return result;
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
