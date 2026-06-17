<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;

class Page extends Model
{
    /** @use HasFactory<\Database\Factories\PageFactory> */
    use HasFactory, SoftDeletes;

    protected $fillable = [
        'title',
        'slug',
        'content',
        'excerpt',
        'status',
        'published_at',
        'parent_id',
        'is_pillar',
        'author_id',
        'featured_image',
        'allow_comments',
        'template'
    ];

    public function author()
    {
        return $this->belongsTo(User::class, 'author_id');
    }

    public function comments()
    {
        return $this->hasMany(Comment::class);
    }

    public static function getAvailableTemplates()
    {
        $templates = [];
        $files = \Illuminate\Support\Facades\File::allFiles(resource_path('views/frontend'));

        foreach ($files as $file) {
            if ($file->getExtension() === 'php') {
                $content = file_get_contents($file->getPathname(), false, null, 0, 8192);
                if (preg_match('/Template Name:\s*(.+)/i', $content, $matches)) {
                    // Clean up trailing chars like */ or --}} if on same line
                    $templateName = trim(preg_replace('/(--\s*}}|\*\/)$/', '', trim($matches[1])));
                    
                    // Extract relative view path from resources/views/
                    $relativePath = $file->getRelativePathname();
                    $viewName = 'frontend.' . str_replace('/', '.', preg_replace('/\.blade\.php$|\.php$/', '', $relativePath));
                    
                    $templates[$viewName] = $templateName;
                }
            }
        }

        return $templates;
    }
}
