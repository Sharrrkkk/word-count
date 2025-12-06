document.getElementById("send").addEventListener("click", async () => {

    const fileInput = document.getElementById("file");
    const file = fileInput.files[0];
    
    const formData = new FormData();
    formData.append("file", file);

    let api = "";
    let embedded = "";

    if (window.location.hostname === 'localhost') {
        //development
        api = "http://localhost:5000/api";
        embedded = "http://localhost:5000/embedded";
    } else {
        //production
        api = "https://sharrrkkk.pythonanywhere.com/api";
        embedded = "https://sharrrkkk.pythonanywhere.com/embedded";
    };
    
    const status = document.getElementById("status").value;

    let url = "";

    if (status === "api") {
        url = api;
    } else {
        url = embedded;
    };

    const response = await fetch(url, {
        method: "POST",
        body: formData,
        cache: "no-store"
    });

    if (status=== "api") {
        //JSON API method
        const data = await response.json();
        document.getElementById("mode").textContent = data.mode;
        document.getElementById("filename").textContent = data.filename;
        document.getElementById("lines").textContent = data.lines;
        document.getElementById("words").textContent = data.words;
        document.getElementById("bytes").textContent = data.bytes;
        document.getElementById("chars").textContent = data.chars;
    } else {
        //embedded method
        const data = await response.text();
        document.getElementById("container").innerHTML = data;
    };

});


document.getElementById("status").addEventListener("change", () => {
    const status = document.getElementById("status").value;
    document.getElementById("mode").textContent = status.toUpperCase();
});