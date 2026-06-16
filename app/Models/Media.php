<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Media extends Model
{
    use HasFactory;

    protected $fillable = [
        'user_id',
        'filename',
        'filepath',
        'url',
        'mime_type',
        'size',
        'alt_text',
        'title',
        'caption',
        'description',
        'dimensions'
    ];

    public function user()
    {
        return $this->belongsTo(User::class);
    }
}
