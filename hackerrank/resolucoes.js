function getLetter(s) {
    let letter;
    switch (true){
        case 'aeiou'.includes(s[0]): return letter = "A";
        case "bcdfg".includes(s[0]): return letter = "B";
        case "hjklm".includes(s[0]): return letter = "C";
        default: return letter = 'D';
    }
    
    return letter;
}
let s = 'adfgt'
console.log(getLetter('knidio'));
console.log(getLetter(s));