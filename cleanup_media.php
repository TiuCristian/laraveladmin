<?php
require 'vendor/autoload.php';
$app = require_once 'bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

$medias = \App\Models\Media::all();
foreach ($medias as $media) {
    if ($media->filepath) {
        $expectedFilename = basename($media->filepath);
        if ($media->filename !== $expectedFilename) {
            $media->filename = $expectedFilename;
            $media->save();
            echo "Updated Media ID {$media->id} filename to {$expectedFilename}\n";
        }
    }
}
echo "Cleanup complete.\n";
