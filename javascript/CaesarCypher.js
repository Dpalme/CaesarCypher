// El diccionario que se usa para comparar las frecuencias obtenidas. Se obtuvo contando los caracteres del Quijote.
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

// Esta función checa si el caracter que se va a analizar es una letra minúscula.
function isLetter(str) {
    return str.length == 1 && str.match(/[a-z]/i);
}


// Esta función regresa el mínimo de un conjunto de datos, en este caso se usa para encontrar el valor de la chi cuadrada.
function min(data) {
    var min = 9999999;
    for(numero in data){
        min = data[numero] < min ? data[numero] : min;
    }
    return min;
}


// Esta función regresa el máximo de un conjunto de datos, en este caso se usa para encontrar el valor de la chi cuadrada.
function max(data) {
    var max = 0;
    for(numero in data){
        max = data[numero] > max ? data[numero] : max;
    }
    return max;
}


// Esta funcion regresa el número de caracter en Unicode.
function num(char){
    return char.charCodeAt(0)-97;
}


// Regresa el caracter que se encuentra en la posición "number" del abecedario traducido a Unicode.
function character(number){
    return String.fromCharCode(97 + (26 + number) % 26);
}


// Codifica el mensaje usando la llave recibida y regresa el mensaje
function encode(key, message){
    cypheredMessage = "";
    for(char of message){
        // Junta todos los caracteres en un único string.
        // Es una condición que checa si el caracter está entre la "a" y la "z". 
        // Si es cierto regresa el caracter modificado con la llave.
        // Si la condición no se cumple solo añade el caracter (Esto para que los espacios se queden en su lugar y no cambiar puntos ni comas.
        //                  condicion        condicion verdadera          condicion falsa
        cypheredMessage +=  isLetter(char) ? character(num(char) + key) : char;
    }
    // Modifica la caja de texto de la página web
    document.getElementById('txtarea').value = cypheredMessage;
}


// Decodifica el mensaje con la llave que se le de
function decode(key, message){
    decypheredMessage = "";
    for(char of message){
        // Al igual que la codificacion, junta una cadena con las letras codificadas y los espacios en su lugar.
        decypheredMessage +=  isLetter(char) ? character(num(char) - key) : char;
    }
    // Modifica la caja de texto de la página web
    document.getElementById('txtarea').value = decypheredMessage;
}


// Funcion que intenta todas las llaves y regresa un mensaje con cada llave probada
// Esta funcion se usa cuando el mensaje es muy chico, porque el metodo de frecuencia no es eficaz.
function bruteForce(message){
    messages = "";
    // For que usa todas las diferentes llaves
    for(i = 1; i < 27; i++){
        msg = "";
        // For que crea los mensajes con cada llave y los añade a una sola cadena
        for(char of message){
            msg += isLetter(char) ? character(num(char) + 1) : char;
        }
        message = msg;
        messages += msg + ", key = " + (26-i) + ' | ';
    }
    // Cambia el area de texto a la cadena con los mensajes con las diferentes llaves
    document.getElementById('txtarea').value = messages;
}


// Funcion que descifra el mensaje con el uso de chi cuadrada
function keyWithChi(message){
    // Primero se crea un diccionario con todas las letras.
    var frequency = {};
    for(var x = 0; x < 26; x++){
        frequency[character(x)] = 0
    }
    // Este for recorre todos los caracteres del mensaje y los cuenta.
    // El conteo se modifica en el diccionario "frequency" y también cuenta el número total de letras
    var counter = 0;
    for(char in message){
        if(isLetter(message[char])){
            counter += 1;
            frequency[message[char]] = frequency[message[char]] + 1;
        }
    };
    // Compara las frecuencias esperadas (Quijote) con las obtenidas (usando lo anterior)
    expectedFrec = database["porcentajes"];
    potentialKeys = [];
    // este for recorre todas las llaves posibles
    for(var i = 0;i < 26; i++){
        var chisqrd = 0;
        // este for obtiene con cada llave todos los valores posibles de chi cuadrada
        for(var j = 0;j < 26; j++){
            var e = expectedFrec[character(j)]*counter;
            var o = frequency[character(i+j)];
            chisqrd += e != 0 ? ((e-o)**2)/e : 0;
        }
        // añade los valores de chi cuadrada donde la posición de la chi cuadrada es la llave utilizada
        potentialKeys.push(chisqrd);
    }
    var maximum = max(potentialKeys);
    for(i = 0; i < 26; i++){
        document.getElementById(character(i)).setAttribute('style', "height : "+ 5*potentialKeys[i]/maximum + "vw; width: 3%; margin-left: auto; margin-right: auto; background: var(--accent); bottom: 0;");
        document.getElementById(character(i)).setAttribute('style', "height : "+ 5*potentialKeys[i]/maximum + "vw; width: 3%; margin-left: auto; margin-right: auto; background: var(--accent); bottom: 0;");
    }
    // cambia la seed en la página al índice del valor mínimo de chi cuadrada.
    document.getElementById('seed').value = potentialKeys.indexOf(min(potentialKeys));
}


//Funcion que encuentra la llave
function keyFinder(message){
    // Este if es en caso de que el mensaje sea muy corto se utiliza el método de fuerza bruta.
    // De otra manera se puede hacer con el método de chi cuadrada.
    return message.length > 6 ? keyWithChi(message) : bruteForce(message);
}
