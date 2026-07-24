<?php
require 'vendor/autoload.php';
$app = require_once 'bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

$medias = \App\Models\Media::orderBy('id', 'asc')->get();
foreach ($medias as $media) {
    echo "ID: {$media->id}, Filename: {$media->filename}, Title: {$media->title}, Alt: {$media->alt_text}\n";
}
