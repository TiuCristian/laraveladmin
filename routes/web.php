<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\AuthController;
use App\Http\Controllers\AdminController;

Route::get('/', function () {
    return view('welcome');
});



Route::get('/login', [AuthController::class, 'showLogin'])->name('login');
Route::post('/login', [AuthController::class, 'login']);
Route::get('/register', [AuthController::class, 'showRegister'])->name('register');
Route::post('/register', [AuthController::class, 'register']);
Route::post('/logout', [AuthController::class, 'logout'])->name('logout');

Route::middleware(['auth', 'admin'])->prefix('admin')->group(function () {
    Route::get('/dashboard', [AdminController::class, 'index'])->name('admin.dashboard');
    
    // User routes
    Route::resource('users', \App\Http\Controllers\UserController::class);
    
    // Content routes
    Route::post('posts/bulk', [\App\Http\Controllers\PostController::class, 'bulk'])->name('posts.bulk');
    Route::post('categories/bulk', [\App\Http\Controllers\CategoryController::class, 'bulk'])->name('categories.bulk');
    Route::post('tags/bulk', [\App\Http\Controllers\TagController::class, 'bulk'])->name('tags.bulk');
    Route::post('pages/bulk', [\App\Http\Controllers\PageController::class, 'bulk'])->name('pages.bulk');
    Route::post('posts/{id}/restore', [\App\Http\Controllers\PostController::class, 'restore'])->name('posts.restore');
    Route::delete('posts/{id}/forceDelete', [\App\Http\Controllers\PostController::class, 'forceDelete'])->name('posts.forceDelete');
    Route::post('pages/{id}/restore', [\App\Http\Controllers\PageController::class, 'restore'])->name('pages.restore');
    Route::delete('pages/{id}/forceDelete', [\App\Http\Controllers\PageController::class, 'forceDelete'])->name('pages.forceDelete');
    Route::resource('posts', \App\Http\Controllers\PostController::class);
    Route::resource('pages', \App\Http\Controllers\PageController::class);
    Route::resource('categories', \App\Http\Controllers\CategoryController::class)->except(['show', 'create']);
    Route::resource('tags', \App\Http\Controllers\TagController::class)->except(['show', 'create']);
    
    Route::post('/upload/image', [\App\Http\Controllers\UploadController::class, 'uploadImage'])->name('admin.upload.image');
    Route::post('/upload/fetchUrl', [\App\Http\Controllers\UploadController::class, 'fetchUrl'])->name('admin.upload.fetchUrl');

    // Profile routes
    Route::get('/profile', [\App\Http\Controllers\ProfileController::class, 'edit'])->name('profile.edit');
    Route::post('/profile', [\App\Http\Controllers\ProfileController::class, 'update'])->name('profile.update');
});

// Frontend Catch-all Routes (Place these at the very bottom)
Route::get('/{category}/{slug}', [\App\Http\Controllers\FrontendController::class, 'post'])->name('frontend.post');
