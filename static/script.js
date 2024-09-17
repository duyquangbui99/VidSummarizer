async function getResponse() {
    const videoUrl = document.getElementById('videoUrl').value;
    const query = "Please summarize this video for me!";
    const responseContainer = document.getElementById('responseOutput');

    if (!videoUrl.trim()) {
        responseContainer.textContent = 'Please enter a video URL.';
        return;
    }

    responseContainer.textContent = 'Loading...'; // Provide a loading message

    fetch('/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ video_url: videoUrl, query: query })
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            responseContainer.textContent = data.response;
        })
        .catch(error => {
            responseContainer.textContent = 'Error fetching response: ' + error.message;
        });
}
