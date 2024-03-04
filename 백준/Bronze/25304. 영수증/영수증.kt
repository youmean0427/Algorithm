fun main() {
    var total: Int = readln().toInt()
    val T = readln().toInt()
    for (i in 1..T) {
        val input = readln().split(" ").map { it.toInt() }
        val a = input[0]
        val b = input[1]
        total -= a * b
    }
    if (total != 0) {
        println("No")
    } else {
        println("Yes")
    }
}