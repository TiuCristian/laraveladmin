<?php
require 'vendor/autoload.php';
$app = require_once 'bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

$media = \App\Models\Media::find(5);
$media->update([
    'alt_text' => 'test update alt',
    'title' => 'test update title',
]);
echo "Updated. DB Alt: {$media->fresh()->alt_text}, Title: {$media->fresh()->title}\n";
