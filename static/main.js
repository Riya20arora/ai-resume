const form = document.getElementById("resumeForm");
const results = document.getElementById("results");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(form);

    try {
        const res = await fetch("/api/review", {
            method: "POST",
            body: formData
        });
        const data = await res.json();
        results.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        results.textContent = "Error: " + err;
    }
});

