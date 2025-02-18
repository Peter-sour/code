<?php
$file = 'webback.mp4'; // Ganti dengan nama file video Anda

// Mengecek apakah file ada
if (file_exists($file)) {
    // Mengatur header untuk memaksa download
    header('Content-Type: application/octet-stream');
    header('Content-Disposition: attachment; filename="' . basename($file) . '"');
    header('Content-Length: ' . filesize($file));

    // Membaca dan mengirim file
    readfile($file);
    exit;
} else {
    echo 'File tidak ditemukan!';
}
?>
