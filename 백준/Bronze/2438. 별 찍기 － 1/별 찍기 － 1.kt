
fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()

    for (i in 1..N) {
        val star = "*".repeat(i)
        println(star)
    }

}