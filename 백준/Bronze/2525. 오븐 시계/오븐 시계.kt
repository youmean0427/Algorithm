fun main() {

    var input = readln().split(" ")
    var C = readln().toInt()

    var A = input[0].toInt()
    var B = input[1].toInt()
    var hh = A
    var mm = B + C

    if (B + C >= 60) {
        mm = (B + C) % 60
        hh += (B + C) / 60
    }

    if (hh >= 24) {
        hh = hh % 24
    }

    println("$hh $mm")
}
