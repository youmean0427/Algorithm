fun main() {

    val input = readln().toInt()
    var ans = ""
    when (input) {
        in 90..100 -> ans = "A"
        in 80 .. 89 -> ans = "B"
        in 70 .. 79 -> ans = "C"
        in 60 .. 69 -> ans = "D"
        else -> ans = "F"
    }

    println(ans)

}