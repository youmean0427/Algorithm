fun main(args: Array<String>) {
    val nums = readln().split(" ").map { it.toInt() }
    println(nums[0] + nums[1])
    println(nums[0] - nums[1])
    println(nums[0] * nums[1])
    println(nums[0] / nums[1])
    println(nums[0] % nums[1])
}