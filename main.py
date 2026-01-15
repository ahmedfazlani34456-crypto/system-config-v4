<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><title>Alexa Master Pro</title>
    <style>
        body { background:#000; color:#0f0; font-family:sans-serif; text-align:center; }
        .btn { background:#0f0; color:#000; padding:15px; margin:10px; border:none; cursor:pointer; width:250px; font-weight:bold; border-radius:10px; }
        .admin-box { border:2px solid #0f0; display:inline-block; padding:20px; margin-top:50px; border-radius:15px; }
    </style>
</head>
<body>
    <script>
        var key = prompt("Master Admin Key:");
        if(key !== "786") { window.location.href="https://google.com"; }
    </script>

    <div class="admin-box">
        <h1>ALEXA COMMAND CENTER (V4)</h1>
        <p>Admin Name: <input type="text" id="adminName" value="AhmedFazlani" style="background:none; border:1px solid #0f0; color:#0f0;"></p>
        <hr>
        <button class="btn" onclick="runFeature('surveillance')">Ghost Mode (Surveillance)</button><br>
        <button class="btn" onclick="runFeature('gdrive_lock')">Lock G-Drive (Expired Users)</button><br>
        <button class="btn" onclick="runFeature('capcut')">CapCut Dubbing & Subtitles</button><br>
        <button class="btn" onclick="runFeature('quran')">Quran & Dua (Tajweed)</button><br>
        <button class="btn" onclick="window.location.href='/admin-panel'">Super Admin Management</button>
    </div>

    <script>
        function runFeature(type) {
            // Ye logic server (main.py) ko command bhejega
            fetch('/execute/' + type)
            .then(res => res.json())
            .then(data => alert("Alexa: " + data.message))
            .catch(err => alert("Error: Connect main.py first!"));
        }
    </script>
</body>
</html>
