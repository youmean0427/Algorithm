fun main() {

    val x = readln().toInt()
    val y = readln().toInt()

    fun check(x : Int, y: Int) : Int {
        if (x > 0 && y > 0) {
            return 1
        } else if (x > 0 && y < 0) {
            return 4
        } else if (x < 0 && y < 0) {
            return 3
        } else {
            return 2
        }
    }

    println(check(x, y))

}
