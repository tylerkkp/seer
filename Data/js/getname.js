let russelData;
$.get('js/Russell_3000_Intraday.txt', function(data) {
    russelData = data;
    //console.log(russelData);

    let dataArray = russelData.split('\n');

    let tickerListString = [];

    dataArray.forEach(function (line) {
        // hacky, but should only filter out non-ticker lines
        if (line.length > 50) {
            tickerListString.push(line);
        }
    });
    tickerListString.splice(0, 1);
    console.log(tickerListString);

    let tickerList = [];
    tickerListString.forEach(function (tickerString) {
        tickerList.push(CreateTickerFromString(tickerString));
    });
    console.log(tickerList);
});

function CreateTickerFromString(tickerString) {
    let arr = tickerString.split('\t');
    return new Ticker(arr[1], arr[2], arr[3], arr[4], arr[5], arr[6]);
}
