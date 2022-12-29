async function FetchResults() {
    res = await fetch("/search?q=" + document.getElementById("query").value);
    json = await res.json()
    document.getElementById("results").innerHTML = json.results.map(res => (`
        <div class='result'>${res}</div>
    `)).join("<br>")
}