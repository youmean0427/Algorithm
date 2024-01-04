fun main(args: Array<String>) {
    val input = readln().split(" ").map { it.toInt() }
    val A = input[0]
    val B = input[1]
    val C = input[2]
    println((A + B) % C)
    println(((A % C) + (B % C)) % C )
    println((A * B) % C)
    println(((A % C) * (B % C)) % C)
}