fun main() {
    val N: Int = readln().toInt()
    var ans = "int"

    for (i in 1..N/4) {
        ans = "long " + ans
    }
    println(ans)
}
