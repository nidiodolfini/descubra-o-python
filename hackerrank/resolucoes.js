function getLetter(s) {
    let letter;
    console.log(s.substring(1,-20))
    switch (s.substring(1,-20)){
        case "a": 
        letter = "A"
        return letter;
    }
    
    return letter;
}

console.log(getLetter('adfgt'))