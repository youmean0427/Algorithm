import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.util.StringTokenizer

fun main() = with(System.`in`.bufferedReader()) {
    val bw = BufferedWriter(OutputStreamWriter(System.out))
    
    val aT = StringTokenizer(readLine())
    val a = aT.nextToken().toInt()
    val arrT = StringTokenizer(readLine())
    val bT = StringTokenizer(readLine())
    val b = bT.nextToken().toInt()
    var ans = 0

    for (i in 1..a) {
        val num = arrT.nextToken().toInt()
        if (num == b) {
            ans += 1
        }
    }

    bw.write("${ans}")
    bw.flush()
    bw.close()

}