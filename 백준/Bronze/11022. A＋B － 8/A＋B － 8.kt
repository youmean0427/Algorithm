import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.util.StringTokenizer

fun main() = with(System.`in`.bufferedReader()) {

    val T = readLine().toInt()
    val bw = BufferedWriter(OutputStreamWriter(System.out))

    for (i in 1..T) {
        val st = StringTokenizer(readLine())
        val a = st.nextToken().toInt()
        val b = st.nextToken().toInt()
        bw.write("Case #$i: $a + $b = ${a+b}\n")
    }
    bw.flush()
    bw.close()
}