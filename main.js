document.getElementById("send").addEventListener("click", async () => {

    const fileInput = document.getElementById("file");
    const file = fileInput.files[0];
    
    const formData = new FormData();
    formData.append("file", file);

    //https://sharrrkkk.pythonanywhere.com/api
    //https://sharrrkkk.pythonanywhere.com/embedded
    const res = await fetch("https://sharrrkkk.pythonanywhere.com/embedded", {
        method: "POST",
        body: formData,
        cache: "no-store"
    });

    //embedded method
    const data = await res.text();
    document.getElementById("container").innerHTML = data;
                
    //JSON API method
    /*const data = await res.json();
    
    document.getElementById("filename").textContent = "FileName: " + data.filename;
    document.getElementById("lines").textContent = "Total Lines: " + data.lines;
    document.getElementById("words").textContent = "Total Words: " + data.words;
    document.getElementById("bytes").textContent = "Total Bytes: " + data.bytes;
    document.getElementById("chars").textContent = "Total Chars: " + data.chars;*/

});
