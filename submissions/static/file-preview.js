const inputElement = document.getElementById("id_attachment")
const previewBtn = document.getElementById("previewBtn");

const getLanguage = (extension) => {
    let language = 'clike';
    if (extension === 'css') {
        language = 'language-css';
    } else if (extension === 'html') {
        language = 'language-html';
    } else if (extension === 'js') {
        language = 'language-javascript';
    } else if (extension === 'py') {
        language = 'language-python';
    }

    return language
}

inputElement.addEventListener("change", (event) => {
    const file = inputElement.files[0];
    const fileExt = file.name.split('.').pop().toLowerCase();
    const previewElement = document.getElementById("preview");
    const previewUrl = URL.createObjectURL(file);
    if (file.type === "application/pdf") {
        previewElement.innerHTML = `<embed src="${previewUrl}">`;
    } else if (file.type.startsWith("image/")) {
        previewElement.innerHTML = `<img src="${previewUrl}" alt="Attachment">`;
    } else if (file.type.startsWith("text")) {
        if (file.name.endsWith(".txt")) {
            previewElement.innerHTML = `<iframe src="${previewUrl}"></iframe>`;
        } else {
            const language = getLanguage(fileExt)
            console.log('attachment file type',language)
            previewElement.innerHTML = `<iframe src="${previewUrl}"></iframe>`;

            fetch(previewUrl)
                .then(response => response.text())
                .then(code => {
                    const highlightedCode = Prism.highlight(code, Prism.languages.python, language);
                    previewElement.innerHTML = `<pre><code class="language-python">${highlightedCode}</code></pre>`;
                });
        }
    } else {
        previewElement.innerHTML = `<p>Preview not supported for <code>${fileExt}</code> files</p>`;
    }
});

// reset the preview if the user clears the file input
inputElement.addEventListener("click", () => {
    if (inputElement.value === "") {
        document.getElementById("preview").innerHTML = "";
    }
});