fun main() {
    val T = readln().toInt()
    for (i in 1..T) {
        val input = readln().split(" ").map { it.toInt() }
        val total = input[0] + input[1]
        println("Case #$i: $total")
    }
}