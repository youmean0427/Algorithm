function solution(n)
{
    var ans = 0;
    
    while (n > 0) {
        let a = Math.trunc(n / 2)
        let b = n % 2
        n = a
        ans += b
    }

    return ans;
}