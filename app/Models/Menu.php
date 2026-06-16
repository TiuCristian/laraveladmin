<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Menu extends Model
{
    protected $fillable = ['name', 'items', 'auto_add_pages'];

    protected $casts = [
        'items' => 'array',
        'auto_add_pages' => 'boolean',
    ];
}
