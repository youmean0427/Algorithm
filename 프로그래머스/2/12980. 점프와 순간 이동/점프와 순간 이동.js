function solution(n)
{
    var ans = 1;
    
    while (n > 1) {
        let a = Math.trunc(n / 2)
        let b = n % 2
        n = a
        ans += b
    }

    return ans;
}