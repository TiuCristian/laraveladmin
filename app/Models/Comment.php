<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Comment extends Model
{
    protected $fillable = [
        'post_id',
        'page_id',
        'name',
        'email',
        'website',
        'content',
        'status',
    ];

    public function post()
    {
        return $this->belongsTo(Post::class);
    }

    public function page()
    {
        return $this->belongsTo(Page::class);
    }
}
