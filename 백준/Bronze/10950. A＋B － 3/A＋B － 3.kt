fun main() {

    val T = readln().toInt()
    for (i in 1..T) {
        val input = readln().split(" ").map { it.toInt() }
        val a = input[0]
        val b = input[1]
        println(a+b)
    }

}
