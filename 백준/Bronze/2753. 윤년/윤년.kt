fun main() {

    val input = readln().toInt()
    var ans : Int = 0
    if (input % 4 == 0 && (input % 100 != 0 || input % 400 == 0)) {
        ans = 1
    }
    println(ans)
    
}