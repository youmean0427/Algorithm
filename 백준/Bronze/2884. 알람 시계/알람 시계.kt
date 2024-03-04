fun main() {

    var input = readln().split(" ")

    var H = input[0].toInt()
    var M = input[1].toInt()

    if (M - 45 < 0) {
        M = 60 + M - 45
        H -= 1
        if (H < 0) {
            H = 24 + H
        }
    } else {
        M -= 45
    }

    println("$H $M")
}
