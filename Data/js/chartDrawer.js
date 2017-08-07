function ChartDrawer(tickerList) {
    tickerList.forEach(function (ticker) {
        ticker.GetDataFromGoogle();
    });

    let labels = tickerList.map(function (x) {
        return x.Symbol;
    });
    let prices = tickerList.map(function (x) {
        return x.Latest;
    });

    console.log(labels);
    console.log(prices);

    let chartElement = document.getElementById("myChart");
    let ctx = chartElement.getContext('2d');
    let myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Closing Price',
                data: prices,
                backgroundColor: [
                ],
                borderColor: [
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
}
