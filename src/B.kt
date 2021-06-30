import java.lang.System.out

fun main() {
    solve();
}

private fun solve() {
    var t = readLine()!!.toInt()
    while (t-- > 0) {
        val n = readLine()!!.toInt()
        val a = readLine()!!.split(" ").map { it.toInt() }.toIntArray()
        doSolve(n, a)
    }
}

private fun doSolve(n: Int, a: IntArray) {
    var pre = a[0]
    for (i in 1 until n) {
        if ((a[i] - pre + 1) % 2 == 1) {
            out!!.println("YES")
            return
        }
        pre = a[i];
    }
    out!!.println("NO")
}
