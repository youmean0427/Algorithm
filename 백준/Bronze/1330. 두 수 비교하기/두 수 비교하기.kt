fun main() {

    val input = readLine()!!.split(" ")
    val a: Int = input[0].toInt()
    val b: Int = input[1].toInt()

    if (a > b) {
        println(">")
    } else if (a < b) {
        println("<")
    } else {
        println("==")
    }

}
