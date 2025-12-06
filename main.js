document.getElementById("send").addEventListener("click", async () => {

    const fileInput = document.getElementById("file");
    const file = fileInput.files[0];
    
    const formData = new FormData();
    formData.append("file", file);

    //production
    //const api = "https://sharrrkkk.pythonanywhere.com/api";
    //const embedded = "https://sharrrkkk.pythonanywhere.com/embedded";
    //let url = "";

    //development
    const api = "http://localhost:5000/api";
    const embedded = "http://localhost:5000/embedded";
    let url = "";

    const status = document.getElementById("status").value;
    document.getElementById("mode").textContet = status;

    if (status === "api") {
        url = api;
    } else {
        url = embedded;
    };

    console.log(url);

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
    }

});


document.getElementById("status").addEventListener("change", function() {
    const status = document.getElementById("status").value;
    document.getElementById("mode").textContent = status.toUpperCase();
});