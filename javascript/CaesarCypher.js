var database = {
    "porcentajes": {
        "a": 0.1222088397965167,
        "b": 0.014718162457500978,
        "c": 0.03622824458468901,
        "d": 0.053174824731535404,
        "e": 0.1396972862797493,
        "f": 0.004620797183514097,
        "g": 0.010499041219632018,
        "h": 0.012141706885054851,
        "i": 0.05490404272515491,
        "j": 0.0064182818021901395,
        "k": 0.0,
        "l": 0.054334747834058464,
        "m": 0.027220097694416644,
        "n": 0.06868292956469055,
        "o": 0.09905609200390583,
        "p": 0.02161674872883887,
        "q": 0.01979914983670867,
        "r": 0.061534438683770704,
        "s": 0.07663416281346266,
        "t": 0.03763746277335602,
        "u": 0.04849368472765883,
        "v": 0.010883650509013023,
        "w": 1.2190468760095233e-06,
        "x": 0.00022979033612779512,
        "y": 0.015308181145489588,
        "z": 0.003956416636088907
    }
};


function isLetter(str) {
    return str.length == 1 && str.match(/[a-z]/i);
}


function min(data) {
    var min = 9999999;
    for(numero in data){
        min = data[numero] < min ? data[numero] : min;
    }
    return min
  }


function num(char){
    return char.charCodeAt(0)-97;
}


function character(number){
    return String.fromCharCode(97 + (26 + number) % 26);
}


function encode(key, message){
    cypheredMessage = "";
    for(char of message){
        cypheredMessage +=  isLetter(char) ? character(num(char) + key) : char;
    }
    document.getElementById('txtarea').value = cypheredMessage;
}


function decode(key, message){
    decypheredMessage = "";
    for(char of message){
        decypheredMessage +=  isLetter(char) ? character(num(char) - key) : char;
    }
    document.getElementById('txtarea').value = decypheredMessage;
}


function bruteForce(message){
    messages = "";
    for(i = 1; i < 27; i++){
        msg = "";
        for(char of message){
            msg += isLetter(char) ? character(num(char) + 1) : char;
        }
        message = msg;
        messages += msg + ", key = " + (26-i) + ' | ';
    }
    document.getElementById('txtarea').value = messages;
}


function keyWithChi(message){
    var frequency = {};
    for(var x = 0; x < 26; x++){
        frequency[character(x)] = 0
    }
    var counter = 0;
    for(char in message){
        if(isLetter(message[char])){
            counter += 1;
            frequency[message[char]] = frequency[message[char]] + 1;
        }
    };
    expectedFrec = database["porcentajes"];
    potentialKeys = [];
    for(var i = 0;i < 26; i++){
        var chisqrd = 0;
        for(var j = 0;j < 26; j++){
            var e = expectedFrec[character(j)]*counter;
            var o = frequency[character(i+j)];
            chisqrd += e != 0 ? ((e-o)**2)/e : 0;
        }
        potentialKeys.push(chisqrd);
    }    
    document.getElementById('seed').value = potentialKeys.indexOf(min(potentialKeys));
}


function keyFinder(message){
    return message.length > 10 ? keyWithChi(message) : bruteForce(message);
}
