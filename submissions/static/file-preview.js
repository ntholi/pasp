const images = ["jpg", "gif", "png", "bmp", "svg", "webp", "tiff", "ico", "heic", "raw"];
const languages = ["py", "js", "java", "c", "cpp", "cs", "rb", "php", "html", "css", "swift", "go", "r", "sql", "pl", "sh", "kt", "dart", "m", "jl","lua","ts","scala","vb","asp","h","hs","clj","lisp","sas"];

const isImage = (fileExt) => {
    for (it of images){
        if (fileExt === it){
            return true;
        }
    }
    return false;
}

const isProgrammingLang = (fileExt) => {
    for (it of languages){
        if(fileExt === it){
            return true;
        }
    }
    return false;
}

const inputElement = document.getElementById("id_attachment")

const getLanguage = (extension) => {
    let language = 'clike';
    if (extension === 'sql') {
        language = 'language-sql';
    }if (extension === 'css') {
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
    if (file.name.endsWith(".pdf")) {
        previewElement.innerHTML = `<embed src="${previewUrl}">`;
    } else if (isImage(fileExt)) {
        previewElement.innerHTML = `<img src="${previewUrl}" alt="Attachment">`;
    } else if (file.name.endsWith(".txt")) {
        previewElement.innerHTML = `<iframe src="${previewUrl}"></iframe>`;
    }else if (isProgrammingLang(fileExt)){
        const language = getLanguage(fileExt)
        console.log('attachment file type',language)
        previewElement.innerHTML = `<iframe src="${previewUrl}"></iframe>`;

        fetch(previewUrl)
            .then(response => response.text())
            .then(code => {
                const highlightedCode = Prism.highlight(code, Prism.languages.python, language);
                previewElement.innerHTML = `<pre><code class="language-python">${highlightedCode}</code></pre>`;
            });
    } else {
        previewElement.innerHTML = `<p>Preview not supported for <code>${fileExt}</code> files</p>`;
    }
});

// // reset the preview if the user clears the file input
// inputElement.addEventListener("click", () => {
//     if (inputElement.value === "") {
//         document.getElementById("preview").innerHTML = "";
//     }
// });