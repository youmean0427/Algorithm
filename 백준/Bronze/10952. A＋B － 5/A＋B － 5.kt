import java.util.StringTokenizer

fun main() = with(System.`in`.bufferedReader()) {
    while (true) {
        val st = StringTokenizer(readLine())
        val a = st.nextToken().toInt()
        val b = st.nextToken().toInt()

        if (a == 0 && b == 0) {
            break
        }
        println(a + b)
    }
}