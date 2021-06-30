import java.lang.Integer.max
import java.lang.System.out

fun main() {
    solve();
}

private fun solve() {
    var t = readLine()!!.toInt()
    while (t-- > 0) {
        val n_and_k = readLine()!!.split(" ").map { it.toInt() }
        val n = n_and_k[0]
        val k = n_and_k[1]
        val l = IntArray(n)
        val r = IntArray(n)
        for (i in 0 until n) {
            val l_and_r = readLine()!!.split(" ").map { it.toInt() }
            l[i] = l_and_r[0]
            r[i] = l_and_r[1]
        }
        doSolve(n, k, l, r)
    }
}

private fun doSolve(n: Int, k: Int, l: IntArray, r: IntArray) {
    var max = 0
    for (i in 0 until n) {
        if (k >= l[i] && k <= r[i]) {
            max = max(max, r[i] - max(l[i], k) + 1)
        }
    }
    out!!.println(max)
}
