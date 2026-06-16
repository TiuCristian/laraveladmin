<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Form extends Model
{
    protected $fillable = ['name', 'fields', 'submit_text'];

    protected $casts = [
        'fields' => 'array',
    ];
}
