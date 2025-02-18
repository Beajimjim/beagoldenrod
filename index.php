<?php
// URL de la API que obtiene los mensajes
$api_url = "http://217.154.4.86:5000/mensajes";

// Obtener mensajes desde la API
$messages = file_get_contents($api_url);
$messages = json_decode($messages, true);
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat Cliente-Servidor</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        .chat-box { width: 60%; margin: auto; border: 1px solid #ccc; padding: 10px; }
        .message { background: #f1f1f1; padding: 5px; margin: 5px; border-radius: 5px; }
    </style>
</head>
<body>
    <h2>Mensajes del Servidor</h2>
    <div class="chat-box">
        <?php if (!empty($messages)) {
            foreach ($messages as $msg) {
                echo "<div class='message'><strong>{$msg['ip']}:</strong> {$msg['text']}</div>";
            }
        } else {
            echo "<p>No hay mensajes aún.</p>";
        } ?>
    </div>
</body>
</html>

