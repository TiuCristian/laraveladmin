<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\AuthController;
use App\Http\Controllers\AdminController;

Route::get('/', [\App\Http\Controllers\FrontendController::class, 'index'])->name('home');
Route::post('/comments', [\App\Http\Controllers\FrontendController::class, 'storeComment'])->name('comments.store');

Route::get('/login', [AuthController::class, 'showLogin'])->name('login');
Route::post('/login', [AuthController::class, 'login']);
Route::get('/register', [AuthController::class, 'showRegister'])->name('register');
Route::post('/register', [AuthController::class, 'register']);
Route::post('/logout', [AuthController::class, 'logout'])->name('logout');

Route::middleware(['auth', 'admin'])->prefix('admin')->group(function () {
    Route::get('/dashboard', [AdminController::class, 'index'])->name('admin.dashboard');
    
    // User routes
    Route::resource('users', \App\Http\Controllers\UserController::class);
    
    // Media Library routes
    Route::get('/media', [\App\Http\Controllers\MediaController::class, 'index'])->name('media.index');
    Route::get('/media/create', [\App\Http\Controllers\MediaController::class, 'create'])->name('media.create');
    Route::post('/media', [\App\Http\Controllers\MediaController::class, 'store'])->name('media.store');
    Route::get('/media/{id}/edit', [\App\Http\Controllers\MediaController::class, 'edit'])->name('media.edit');
    Route::put('/media/{id}', [\App\Http\Controllers\MediaController::class, 'update'])->name('media.update');
    Route::delete('/media/{id}', [\App\Http\Controllers\MediaController::class, 'destroy'])->name('media.destroy');

    // Category & Tag Management routes
    Route::post('posts/bulk', [\App\Http\Controllers\PostController::class, 'bulk'])->name('posts.bulk');
    Route::post('comments/bulk', [\App\Http\Controllers\CommentController::class, 'bulk'])->name('comments.bulk');
    Route::post('categories/bulk', [\App\Http\Controllers\CategoryController::class, 'bulk'])->name('categories.bulk');
    Route::post('tags/bulk', [\App\Http\Controllers\TagController::class, 'bulk'])->name('tags.bulk');
    Route::post('pages/bulk', [\App\Http\Controllers\PageController::class, 'bulk'])->name('pages.bulk');
    Route::post('posts/{id}/restore', [\App\Http\Controllers\PostController::class, 'restore'])->name('posts.restore');
    Route::delete('posts/{id}/forceDelete', [\App\Http\Controllers\PostController::class, 'forceDelete'])->name('posts.forceDelete');
    Route::post('pages/{id}/restore', [\App\Http\Controllers\PageController::class, 'restore'])->name('pages.restore');
    Route::delete('pages/{id}/forceDelete', [\App\Http\Controllers\PageController::class, 'forceDelete'])->name('pages.forceDelete');
    Route::resource('posts', \App\Http\Controllers\PostController::class);
    Route::resource('pages', \App\Http\Controllers\PageController::class);
    Route::get('forms/messages', [\App\Http\Controllers\FormController::class, 'messages'])->name('forms.messages');
    Route::get('forms/messages/{id}/edit', [\App\Http\Controllers\FormController::class, 'editMessage'])->name('forms.messages.edit');
    Route::put('forms/messages/{id}', [\App\Http\Controllers\FormController::class, 'updateMessage'])->name('forms.messages.update');
    Route::delete('forms/messages/{id}', [\App\Http\Controllers\FormController::class, 'destroyMessage'])->name('forms.messages.destroy');
    Route::resource('forms', \App\Http\Controllers\FormController::class);

    Route::resource('comments', \App\Http\Controllers\CommentController::class)->except(['create', 'store', 'show']);
    Route::resource('categories', \App\Http\Controllers\CategoryController::class)->except(['show', 'create']);
    Route::resource('tags', \App\Http\Controllers\TagController::class)->except(['show', 'create']);
    
    Route::post('/upload/image', [\App\Http\Controllers\UploadController::class, 'uploadImage'])->name('admin.upload.image');
    Route::post('/upload/fetchUrl', [\App\Http\Controllers\UploadController::class, 'fetchUrl'])->name('admin.upload.fetchUrl');

    Route::resource('menus', \App\Http\Controllers\MenuController::class);
    Route::post('menus/locations', [\App\Http\Controllers\MenuController::class, 'locations'])->name('menus.locations');
    
    Route::get('widgets', [\App\Http\Controllers\WidgetController::class, 'index'])->name('widgets.index');
    Route::post('widgets', [\App\Http\Controllers\WidgetController::class, 'save'])->name('widgets.save');
    
    // Settings routes
    Route::get('/settings/general', [\App\Http\Controllers\SettingsController::class, 'general'])->name('settings.general');
    Route::post('/settings/general', [\App\Http\Controllers\SettingsController::class, 'updateGeneral'])->name('settings.general.update');
    Route::get('/settings/writing', [\App\Http\Controllers\SettingsController::class, 'writing'])->name('settings.writing');
    Route::post('/settings/writing', [\App\Http\Controllers\SettingsController::class, 'updateWriting'])->name('settings.writing.update');
    Route::get('/settings/reading', [\App\Http\Controllers\SettingsController::class, 'reading'])->name('settings.reading');
    Route::post('/settings/reading', [\App\Http\Controllers\SettingsController::class, 'updateReading'])->name('settings.reading.update');
    Route::get('/settings/discussion', [\App\Http\Controllers\SettingsController::class, 'discussion'])->name('settings.discussion');
    Route::post('/settings/discussion', [\App\Http\Controllers\SettingsController::class, 'updateDiscussion'])->name('settings.discussion.update');
    Route::get('/settings/media', [\App\Http\Controllers\SettingsController::class, 'media'])->name('settings.media');
    Route::post('/settings/media', [\App\Http\Controllers\SettingsController::class, 'updateMedia'])->name('settings.media.update');
    Route::get('/settings/permalinks', [\App\Http\Controllers\SettingsController::class, 'permalinks'])->name('settings.permalinks');
    Route::post('/settings/permalinks', [\App\Http\Controllers\SettingsController::class, 'updatePermalinks'])->name('settings.permalinks.update');

    // Profile routes
    Route::get('/profile', [\App\Http\Controllers\ProfileController::class, 'edit'])->name('profile.edit');
    Route::post('/profile', [\App\Http\Controllers\ProfileController::class, 'update'])->name('profile.update');
});

// Forms Submission
Route::post('/forms/{form}/submit', [\App\Http\Controllers\FormController::class, 'submit'])->name('forms.submit');

// Frontend Catch-all Routes (Place these at the very bottom)
$category_base = 'category';
$tag_base = 'tag';

try {
    if (\Illuminate\Support\Facades\Schema::hasTable('settings')) {
        $category_base = \App\Models\Setting::where('key', 'category_base')->value('value') ?: 'category';
        $tag_base = \App\Models\Setting::where('key', 'tag_base')->value('value') ?: 'tag';
    }
} catch (\Exception $e) {
    // Ignore DB errors during setup/migration
}

if ($category_base !== '.') {
    Route::get('/' . $category_base . '/{slug}', [\App\Http\Controllers\FrontendController::class, 'category'])->name('frontend.category');
}
if ($tag_base !== '.') {
    Route::get('/' . $tag_base . '/{slug}', [\App\Http\Controllers\FrontendController::class, 'tag'])->name('frontend.tag');
}

Route::get('/{category}/{slug}', [\App\Http\Controllers\FrontendController::class, 'post'])->name('frontend.post');
Route::get('/{slug}', [\App\Http\Controllers\FrontendController::class, 'page'])->name('frontend.page');
