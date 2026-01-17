 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>YouTube Downloader</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #111;
            color: #fff;
            text-align: center;
            padding-top: 100px;
        }
        .box {
            width: 400px;
            margin: auto;
            padding: 20px;
            background: #222;
            border-radius: 10px;
        }
        input {
            width: 90%;
            padding: 10px;
            border: none;
            margin: 10px 0;
            border-radius: 5px;
        }
        button {
            padding: 10px 20px;
            background: #ff0000;
            border: none;
            color: #fff;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background: #cc0000;
        }
    </style>
</head>
<body>

<div class="box">
    <h2>YouTube Video Downloader</h2>
    <input type="text" id="url" placeholder="Enter YouTube URL">
    <button onclick="downloadVideo()">Download</button>
    <p id="status"></p>
</div>

<script>
async function downloadVideo() {
    const url = document.getElementById("url").value;
    document.getElementById("status").innerText = "Downloading... Please wait";

    const response = await fetch("/download", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({url: url})
    });

    const data = await response.json();

    if (data.file) {
        document.getElementById("status").innerHTML =
            `<a href="/get-video/${data.file}" download>Click here to download the video</a>`;
    } else {
        document.getElementById("status").innerText = "Error: " + data.error;
    }
}
</script>

</body>
</html>
