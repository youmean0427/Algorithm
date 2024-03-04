import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.util.StringTokenizer

fun main() = with(System.`in`.bufferedReader()) {

    val bw = BufferedWriter(OutputStreamWriter(System.out))

    try{
        while(true) {
            val st = StringTokenizer(readLine())
            val a = st.nextToken().toInt()
            val b = st.nextToken().toInt()
            bw.write("${a + b}\n")
        }
    } catch (e: Exception) {
        bw.flush()
        bw.close()
    }
}