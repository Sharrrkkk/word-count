/**
 * Handles file upload and sends it to the appropriate endpoint (API or embedded).
 * Updates the DOM with the response (JSON or HTML).
 *
 * @async
 * @function handleFileUpload
 * @returns {Promise<void>} No return, modifies DOM directly.
 */
document.getElementById("send").addEventListener("click", async () => {
     /** @type {HTMLInputElement} */
    const fileInput = document.getElementById("file");

    /** @type {File} */
    const file = fileInput.files[0];
    
    /** @type {FormData} */
    const formData = new FormData();
    formData.append("file", file);

    /** @type {string} */
    let api = "";
    /** @type {string} */
    let embedded = "";

    if (window.location.hostname === 'localhost') {
        // Development URLs
        api = "http://localhost:5000/api";
        embedded = "http://localhost:5000/embedded";
    } else {
        // Development URLs
        api = "https://sharrrkkk.pythonanywhere.com/api";
        embedded = "https://sharrrkkk.pythonanywhere.com/embedded";
    };
    
    /** @type {string} */
    const status = document.getElementById("status").value;

    /** @type {string} */
    let url = "";

    if (status === "api") {
        url = api;
    } else {
        url = embedded;
    };
    
    /** @type {Response} */
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


/**
 * Updates the mode display when the status selector changes.
 *
 * @function updateModeDisplay
 * @returns {void} No return, modifies DOM directly.
 */
document.getElementById("status").addEventListener("change", () => {
    const status = document.getElementById("status").value;
    document.getElementById("mode").textContent = status.toUpperCase();
});