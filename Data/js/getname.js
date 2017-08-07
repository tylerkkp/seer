

jQuery.get('http://www.kibot.com/Files/2/Russell_3000_Intraday.txt', function(data) {
var myvar = data;
});


var arrayLength = myvar.length;

for (i = 0; i < arrayLength; i++) {
  function isUpperCase(str) {
      return str === str.toUpperCase();
  }

  // initialize array
  var tickerlist = [];

  // append new value to the array
  tickerlist.push(i);
}

console.log(tickerlist);