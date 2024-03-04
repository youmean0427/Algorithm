import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.util.StringTokenizer

fun main() = with(System.`in`.bufferedReader()) {

    val bw = BufferedWriter(OutputStreamWriter(System.out))

    while (true) {
        val st = StringTokenizer(readLine())
        val a = st.nextToken().toInt()
        val b = st.nextToken().toInt()

        if (a == 0 && b == 0) {
            break
        }
        bw.write("${a + b}\n")
    }
    bw.flush()
    bw.close()
}