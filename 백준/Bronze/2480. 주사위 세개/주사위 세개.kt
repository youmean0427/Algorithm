fun main() {

    var input = readln().split(" ").map{ it.toInt() }

    val a = input[0]
    val b = input[1]
    val c = input[2]

    var ans: Int = 0

    if (a == b && b == c) {
        ans = 10000 + (a * 1000)
    } else if (a != b && b != c && a != c) {
        ans = maxOf(a, b, c) * 100
    } else {
        if (a == b) {
            ans = 1000 + (a * 100)
        } else {
            ans = 1000 + (c * 100)
        }
    }

    println(ans)

}
