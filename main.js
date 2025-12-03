document.getElementById("send").addEventListener("click", async () => {

    const fileInput = document.getElementById("file");
    const file = fileInput.files[0];
    
    const formData = new FormData();
    formData.append("file", file);

    //http://localhost:5000/api
    //http://localhost:5000/embedded
    const res = await fetch("http://localhost:5000/api", {
        method: "POST",
        body: formData
    });

    //embedded method
    //const data = await res.text();
    //document.getElementById("container").innerHTML = data;
                
    //JSON API method
    const data = await res.json();
    const raw = localStorage.getItem("results");
    localStorage.setItem("results", JSON.stringify(data));
    if (raw) {
        const data = JSON.parse(raw);
        document.getElementById("lines").textContent = "Total Lines: " + data.lines;
        document.getElementById("words").textContent = "Total Words: " + data.words;
        document.getElementById("bytes").textContent = "Total Bytes: " + data.bytes;
        document.getElementById("chars").textContent = "Total Chars: " + data.chars;
    };

});
