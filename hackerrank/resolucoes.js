function reverseString(s) {
    try {
        var splitString = s.split(''); //divide a palavra em um array letras 
        var reverseArray = splitString.reverse(); //inverter o array 
        var joinArray = reverseArray.join(''); // junta o array de palavras
        return joinArray;
    }
    catch (e) {
        console.log("s.split is not a function");
        console.log(s)
    }
        
    
}

reverseString(Number(1234));
console.log(reverseString('1234'));


function reverseString(str) {
    return str.split("").reverse().join("");
}
reverseString("hello");