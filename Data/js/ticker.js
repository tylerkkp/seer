class Ticker {
    constructor(symbol, startDate, description, exchange, industry, sector) {
        this.Symbol = symbol;
        this.StartDate = startDate;
        this.Description = description;
        this.Exchange = exchange;
        this.Industry = industry;
        this.Sector = sector;
    }

    LogTickerInformation() {
        console.log(this.Symbol + "\t" + this.StartDate + "\t" + this.Description + "\t" + this.Exchange + "\t" + this.Industry + "\t" + this.Sector + "\t" + this.Latest);
    }

    GetDataFromGoogle() {
        let url = "https://www.google.com/finance/info?q=" + this.Exchange + ":" + this.Symbol;
        let request = new XMLHttpRequest();
        request.open("GET", url, false);
        try {
            request.send(null);
            let response = request.responseText;
            response = response.substr("////".length);

            let responseArray = JSON.parse(response);
            let responseObject = responseArray[0];
            this.Latest = responseObject["l"];
        }
        catch (e) {
            console.log("error " + e);
        }
    }
}

let ticker = new Ticker("A", "11/18/1999", "Agilent Technologies, Inc.", "NYSE", "Biotechnology: Laboratory Analytical Instruments", "Capital Goods");
ticker.LogTickerInformation();
ticker.GetDataFromGoogle();
ticker.LogTickerInformation();
