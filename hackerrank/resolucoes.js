function fatorial(n) {
    var fat = 0
    if (n > 1) {
        for (i = 0; i < n; i++){
            fat += fat * n 
        }
        return fat;
    }
    return 1;

}

console.log(fatorial(4))