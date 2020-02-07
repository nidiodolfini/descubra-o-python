function vowelsAndConsonants(s) {
    var vogais = '';
    var consoantes = '';
  for (var i = 0; i < s.length; i++){
    if('aeiou'.includes(s[i])){
        vogais += s[i]
    }else {
        consoantes += s[i]
    }
    
  }
  var teste = vogais;
  teste += consoantes;
  for (i = 0; i < teste.length; i++){
    console.log(teste[i])
  }
}

vowelsAndConsonants('javascriptloops')